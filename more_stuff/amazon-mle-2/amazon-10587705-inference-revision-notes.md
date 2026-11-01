# AWS inference optimization: revision notes and spoken answers

**Prepared:** October 27, 2026. **Role:** Machine Learning Engineer II, AWS Inference Optimization, requisition 10587705.

**Purpose:** revise the selected Stanford CS336 Spring 2025 lectures and Baseten book sections, then connect them to your actual work. Sadaf offered a 30-minute informational phone chat. All questions below are **inferred from the JD and your CV**, not reported questions from her team. Technical follow-ups are preparation options; the call's exact technical depth is unconfirmed.

**Subsequent source audit, October 27:** read the [project/PR review](amazon-10587705-project-pr-review.md) before quoting results. The kernel report separates INT2's 5.24× long-context compression from INT4's +0.33% short-evaluation perplexity result; these are not one operating point. SGLang's final patch reuses existing `last_forward_entry_time` state, and a later PR comment identifies an uncovered PD decode caller path. The audit also distinguishes final code from intermediate PR descriptions and recorded test counts. These clarifications supersede broader interpretations of the summaries below.

**Evidence labels:** **Your work** means established in the current [master CV](../../cv.md). **Concept** means technical knowledge to understand. **Proposed approach** means how you would investigate a new problem, not an experiment you already performed. Numerical examples labeled **illustrative** are not your measurements. This document adds no new experience to the CV.

**Use:** read cards 1, 8, 9, 10, 12 and 13 first for the call. Work through the remaining cards before a technical interview. Rehearse each short answer, then explain the mechanism in your own words.

## 1. Your introduction and why this team

**Likely question:** “Tell me about yourself, and why inference optimization?”

> I have nearly four years of professional software-engineering experience at Oracle and Incture, and I completed my master's at NYU this May. My recent work focuses on GPU performance and LLM inference. I built Triton attention and KV-cache kernels, profiled them on H100, and contributed merged fixes to vLLM and SGLang around reliable serving measurements. This role connects those interests: kernel performance, inference engines, and the engineering needed to turn improvements into dependable customer-facing serving.

**Why your background matters:** kernels supply hands-on optimization evidence; upstream work supplies evidence of correctness and compatibility in existing systems; professional roles supply Java/backend/test-infrastructure experience. Keep those categories clear when discussing duration and ownership.

**If asked about professional GPU tenure:** your nearly four professional years are not four years of professional MLE/kernel work. State that the specialization is recent project/open-source work. Two years of qualifying professional architecture scope is not independently established by total employment duration.

## 2. Prefill, decode and the KV cache

**Revise:** CS336 Lecture 10; Baseten 2.2 and 2.4.

**Likely question:** “Why do you optimize prefill and decode differently?”

> Prefill processes the input positions together, which exposes larger matrix operations and opportunities for data reuse. Autoregressive decode adds one token per active sequence per step, often doing less arithmetic relative to weight and KV-cache movement. Those different resource profiles motivate different kernels and serving policies. The actual bottleneck still depends on batch size, context length, architecture and implementation.

**Concept:** caching avoids recomputing prior keys and values; each new token still needs to attend to the relevant cached context. A long KV history can make attention's data movement important. Feed-forward, projection, communication or launch overhead can dominate other regimes; “attention is always the bottleneck” is too broad.

**Your work:** connect prefill to FlashAttention-style tiling, and decode to split-KV/GQA/MQA. Connect queueing and TTFT to serving measurements, rather than describing TTFT as kernel time alone.

**Follow-up:** increasing batch size can amortize weight traffic, but consumes KV capacity and can worsen latency. There is no single batch size that is optimal for every service.

Sources: [Stanford Lecture 10 code](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_10.py), [Baseten bottlenecks](https://www.baseten.co/inference-engineering/book/02-models/calculating-inference-bottlenecks/).

## 3. Resource accounting and a roofline explanation

**Revise:** CS336 Lecture 2; Baseten 2.4.

**Likely question:** “How would you identify whether a kernel is compute-bound or memory-bound?”

**Concept:** start with work and data movement, then verify the hypothesis with profiling.

```text
Arithmetic intensity I = floating-point operations / bytes transferred
Idealized throughput ceiling = min(compute ceiling, bandwidth × I)
Idealized execution-time bound ≈ max(FLOPs / compute rate, bytes / bandwidth)
```

These are bounds, not predictions that include every launch, dependency, cache effect or synchronization cost. Choose the relevant memory level and dtype-specific compute ceiling. Never combine sparse peak FLOPs with a dense workload or assume every H100 variant has the same bandwidth.

**Your work:** 433 TFLOP/s is a measured kernel result in a particular BF16 regime. It does not establish model tokens/second, a universal speedup, or a hardware-utilization percentage without a justified denominator.

**Likely follow-up:** “Would doubling compute make it twice as fast?” Answer conditionally: only if compute is the limiting resource and the rest of the system permits it.

Sources: [Lecture 2 code](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_02.py), [Baseten 2.4](https://www.baseten.co/inference-engineering/book/02-models/calculating-inference-bottlenecks/).

## 4. GPU execution, memory and occupancy

**Revise:** CS336 Lecture 5; Baseten 3.1 and 3.3.

**Likely question:** “What does register-pressure-limited occupancy mean?”

> Registers are a finite resource on each streaming multiprocessor. A kernel's per-thread or per-block register requirements can limit how much work is resident at once. That may reduce opportunities to hide latency. But forcing register use down can cause spills or reduce useful work, so the decision has to be judged by measured performance.

**Concept map:** threads execute in warps; blocks are assigned to SMs. Registers are thread-private, shared memory is shared within a block, caches service memory accesses, and HBM holds large tensors. Tensor cores accelerate supported matrix operations; kernel efficiency still depends on moving and scheduling the data.

**Your work:** the CV establishes Nsight Compute diagnosis of register-pressure-capped occupancy. Prepare an actual report and code/configuration change. Exact occupancy percentages, register counts, stall counters and a resulting speedup are not recorded in the CV, so do not manufacture them.

**Follow-up:** “Is maximum occupancy your target?” Your target is the best relevant latency/throughput under correctness constraints. Occupancy is diagnostic evidence, not the objective function.

Sources: [Baseten GPU architecture](https://www.baseten.co/inference-engineering/book/03-hardware/gpu-architecture/), [NVIDIA occupancy guidance](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy).

## 5. FlashAttention, tiling and stable online softmax

**Revise:** CS336 Lectures 5–6; Baseten 2.5 and 4.1.

**Likely question:** “Why does your attention implementation help?”

> The attention computation has large intermediate score and probability matrices if implemented directly. A tiled, fused implementation can avoid writing those full intermediates to global memory. It keeps the necessary running state while processing blocks of keys and values. The benefit comes from the mapping and memory traffic, with correctness checked against a reference.

**Concept:** FlashAttention does not turn dense attention's quadratic arithmetic into linear arithmetic. It changes the execution and storage strategy. FlashAttention-2 further improves work partitioning and reduces some overheads.

**Optional mathematical refresher:** for a score tile `s` and its values `V`, a generic stable streaming softmax update keeps a maximum `m`, normalization sum `l`, and unnormalized weighted sum `u`:

```text
m_new = max(m, max(s))
alpha = exp(m - m_new)
p = exp(s - m_new)
l_new = alpha*l + sum(p)
u_new = alpha*u + p @ V
final output = u / l
```

This is a conceptual recurrence, not a transcription of your kernel. Handle masks and initialization correctly. Base-2 exponentiation requires the appropriate change of scale. Different floating-point orderings need not be bit-identical.

**Your work:** online-softmax tiling, base-2 exp2 and Hopper autotuning; 1.1–1.3× SDPA at long sequences. Do not imply a newly invented attention algorithm.

Sources: [FlashAttention-2 paper](https://arxiv.org/abs/2307.08691), [Baseten attention optimization](https://www.baseten.co/inference-engineering/book/02-models/optimizing-attention/).

## 6. Split-KV decoding and GQA/MQA

**Revise:** CS336 Lecture 10; Baseten 2.5 and 5.3.

**Likely question:** “What is split-KV, and when can it lose?”

> Instead of assigning an entire KV history to one unit of work, split-KV processes portions in parallel and combines the partial attention results. That can help when the original mapping exposes too little parallelism. It also introduces partial-result storage, reduction and coordination work, which can outweigh the benefit for other shapes.

**Concept:** partial softmax outputs require normalization-aware merging; simply averaging the normalized outputs is generally wrong. GQA shares KV heads across groups of query heads; MQA uses one KV head. This reduces KV storage relative to otherwise comparable multi-head attention.

**Your work:** occupancy-aware split policy and tensor-core GQA/MQA path. Keep both baselines explicit: up to **13.6× versus naive decode**; **peak 1.29× versus SDPA in target GQA regimes**.

**Prepare:** one winning shape and one losing shape, plus the chosen split count and reduction cost. Those settings are not supplied in the master CV.

Sources: [Lecture 10](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_10.py), [Baseten attention](https://www.baseten.co/inference-engineering/book/02-models/optimizing-attention/).

## 7. KV capacity, quantization and cache behavior

**Revise:** Baseten 5.1 and 5.3; CS336 Lecture 10.

**Likely question:** “How much memory does the KV cache use?”

For a conventional uniform cache, a useful estimate is:

```text
KV bytes ≈ 2 × batch × layers × cached_tokens × KV_heads × head_dim × bytes_per_element
```

The factor two represents K and V. Real allocation also includes block rounding, metadata, quantization scales and other engine-specific overhead. Architectures such as latent-attention models need different accounting.

**Illustrative example, not your project configuration:** batch 1, 32 layers, 8,192 tokens, 8 KV heads, head dimension 128, and 2 bytes/value gives approximately **1 GiB** of raw K/V storage.

**Likely question:** “Why doesn't INT4 guarantee a 4× end-to-end speedup?”

> Lower precision can reduce storage and memory traffic, but unpacking, scale handling and dequantization have costs. Other operators can become limiting. I would evaluate numerical effects, kernel latency and complete serving behavior separately.

**Your work:** KIVI-inspired INT8/INT4/INT2 with in-kernel bit-unpacking, 5.2× compression, reference validation, and an INT4 perplexity result. Retrieve the model, dataset, baseline precision and interpretation of “+0.33%” before discussing that accuracy result in detail.

**Distinctions to explain:** KV quantization reduces representation size; prefix caching reuses previously computed prefixes; paging changes allocation/management; cache-aware routing seeks replicas holding useful cached state. These solve related but different problems.

Sources: [Baseten quantization](https://www.baseten.co/inference-engineering/book/05-techniques/quantization/), [Baseten caching](https://www.baseten.co/inference-engineering/book/05-techniques/caching/).

## 8. Benchmarking and profiling: your highest-priority defense

**Revise:** CS336 Lecture 6; Baseten 4.5.

**Likely question:** “How do you know your speedup is real?”

**Proposed method:** compare equivalent inputs, precision, masking and semantics; warm up both paths; exclude compilation from steady-state timing or report it separately; account for asynchronous GPU execution; repeat measurements and report variability. State whether the boundary includes allocations, transfers and reductions.

For SDPA, record its version and selected backend. An optimized reference must be compared fairly. CPU launch timing alone can miss GPU completion. GPU event timing and synchronized wall-clock measurements have different uses and boundaries.

**Profiling distinction:** Nsight Systems helps inspect the system timeline, launches and overlap; Nsight Compute provides detailed per-kernel resource and execution analysis. You used Nsight Compute in TritonAttn; other tools in Skills do not automatically establish their use in that project.

**Have this evidence sheet open:**

| Field | Your actual value to retrieve |
|---|---|
| Shape | Batch, Q/KV heads, head dimension, input/KV length |
| Hardware | H100 variant, GPU count and relevant environment |
| Software | PyTorch, Triton, CUDA and selected SDPA backend |
| Boundary | Warmup, compilation, allocation, transfers, reduction |
| Statistics | Repetitions, median/percentiles, variability |
| Correctness | Reference, tolerances, masking and edge cases |
| Limitation | A losing regime and its observed bottleneck |

**Boundary:** these are questions to answer from artifacts. They are not a statement that your existing benchmark used each recommended procedure.

Sources: [Lecture 6 code](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_06.py), [Baseten benchmarking](https://www.baseten.co/inference-engineering/book/04-software/performance-benchmarking-and-load-testing/), [NVIDIA correctness guidance](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#verification).

## 9. Latency metrics and your vLLM contribution

**Revise:** Baseten 1.4 and 4.5.

**Likely question:** “What did you change in vLLM?”

> I corrected inconsistent latency accounting across streaming benchmark endpoints. The first-token timestamp was not consistently reused, and tokenless usage trailers could extend the measured end time. I aligned the measurement windows and added deterministic regression tests. The benefit is comparable, trustworthy measurements for evaluating inference performance.

**Conceptual timeline:** `start → first token-bearing chunk → later token-bearing chunks → last token-bearing chunk → usage trailer → stream closure`.

```text
TTFT = first accepted token-bearing arrival - start
Measured E2E = last accepted token-bearing arrival - start
Post-first-token window = E2E - TTFT = sum(measured inter-arrival intervals)
TPOT = (E2E - TTFT)/(output_tokens - 1), for output_tokens > 1
```

The identity telescopes only when all terms use consistent boundaries. TPOT is an average; a multi-token streaming chunk does not expose each token's separate arrival time. Stream closure and delivery of the final token are also different events.

**Your implementation evidence:** reused timestamp; ignored tokenless usage trailers for the measured endpoint; rejected usage-only success; deterministic CPU-only tests with scripted/real clocks; 12 new and 8 sibling tests passed.

**If asked about impact:** no engine acceleration is claimed. The contribution makes comparisons meaningful and guards against regression. Keep total service response time separate from this benchmark's measured decode window.

**Follow-ups to rehearse:** Why use a scripted clock? Why an explicit first-chunk flag? What happens with zero/one output tokens? How would you show the test fails on the original bug?

Sources: [vLLM PR #55508](https://github.com/vllm-project/vllm/pull/55508), [Baseten latency metrics](https://www.baseten.co/inference-engineering/book/01-prerequisites/measuring-latency-and-throughput/), current CV. Definitions above describe this metric boundary, not all possible definitions of E2E.

## 10. Request lifecycles and your SGLang contribution

**Revise:** Baseten 4.3/4.5; connect request lifecycle reasoning to continuous batching.

**Likely question:** “Why could queue time become negative?”

> A request could run, be retracted or preempted, and re-enter the queue. The accounting mixed its original execution timestamp with its newer queue-entry timestamp. I accumulated each waiting interval, made closing a wait idempotent and handled process-clock rebasing while preserving scheduling decisions and the histogram contract.

**Illustrative timestamps:** queue at 1, run at 3, requeue at 8, resume at 10. `3 - 8 = -5` is invalid; total waiting is `(3 - 1) + (10 - 8) = 4`.

**Important distinctions:** an interval should close once even if chunked-prefill callbacks repeat. Elapsed durations must not be treated as absolute timestamps during clock rebasing. Preserve timestamps other scheduler code relies on; clamping a negative result to zero hides the faulty accounting. The existing histogram retained first-wait semantics, while total-wait accounting served other outputs.

**Your evidence:** six regression/contract tests, 303 related tests validated, 20,000 randomized lifecycles, 9,504 non-retracted compatibility cases. Broader testing included documented pre-existing platform failures; avoid saying every test passed. PD coverage was unit/randomized lifecycle validation, not an end-to-end deployment.

Sources: [SGLang PR #39312](https://github.com/sgl-project/sglang/pull/39312), current CV. This card summarizes the PR mechanism; the timestamps are invented solely for teaching.

## 11. Engines, batching, parallelism and multi-GPU tradeoffs

**Revise:** CS336 Lectures 7–8 and 10; Baseten 4.3 and 5.4.

**Likely question:** “How would you choose an inference engine?”

**Proposed approach:** start with supported model/hardware, correctness and required features; compare under the intended prompt/output distribution, concurrency and latency objectives; consider operation and debugging. No engine is automatically best for all workloads.

**Concept:** continuous batching admits new requests as capacity becomes available rather than waiting for every sequence in a static batch to finish. KV memory and scheduling influence achievable concurrency. Efficient GPU work can still sit behind a long queue.

**Your connection:** vLLM measurement correctness and SGLang lifecycle accounting sit around the engine's execution path; they do not establish changes to engine scheduling policy or upstream attention kernels.

**Parallelism refresher:** tensor parallelism divides operations/model tensors and introduces communication; pipeline parallelism divides layers/stages and faces scheduling/bubble tradeoffs; expert parallelism distributes MoE experts and routing traffic; data parallelism provides replicas for separate work. FSDP/ZeRO primarily address distributed training state/memory; mentioning them alone does not demonstrate a production serving design.

**Your boundary:** NCCL, RDMA, FSDP and DeepSpeed are in your established skills. Exact production topology, device count or collective optimization ownership is not established here.

Sources: [Baseten engines](https://www.baseten.co/inference-engineering/book/04-software/inference-engines/), [Baseten model parallelism](https://www.baseten.co/inference-engineering/book/05-techniques/model-parallelism/), [CS336 schedule](https://cs336.stanford.edu/spring2025/).

## 12. Speculative decoding: a knowledge gap to explain honestly

**Revise:** CS336 Lecture 10; Baseten 5.2.

**Likely question:** “What is speculative decoding, and when would it help?”

> A cheaper draft mechanism proposes several tokens, then the target verifies them. The goal is to emit more useful tokens per expensive target step. Benefit depends on acceptance, drafting/verification costs and workload utilization. Low acceptance or high overhead can make it slower.

**Concept:** standard exact speculative sampling needs correct acceptance/rejection and correction to preserve the target distribution in theory. Approximate variants may relax that goal; do not promise identical sampled text under every implementation and numerical setting.

**Proposed experiment:** compare with the same target model, quality checks and traffic; sweep draft depth/concurrency; measure emitted tokens per verification cycle, draft/verify overhead, TTFT/TPOT and useful throughput. This is a proposed benchmark, not existing project evidence.

**Your connection:** attention, quantization and measurement experience provides relevant foundations. The CV does not establish that you implemented speculative decoding.

Sources: [Baseten speculation](https://www.baseten.co/inference-engineering/book/05-techniques/speculative-decoding/), [vLLM lossless-guarantee discussion](https://docs.vllm.ai/en/latest/features/speculative_decoding/).

## 13. Disaggregated inference: another honest boundary

**Revise:** Baseten 5.5, 3.3 and 4.4.

**Likely question:** “Why separate prefill and decode?”

> Their different resource and latency requirements can justify independent workers and capacity allocation. Separation may reduce interference, but requires KV transfer, routing and coordination. It helps only when those costs are outweighed by improved utilization or latency for the workload.

**Concept:** estimate the KV payload, effective transfer bandwidth and added coordination delay. Then inspect prefill/decode queues, cache locality, capacity imbalance and failure recovery. Treat claims about benefit as workload-dependent.

**Your connection:** you understand both phases through kernel work; SGLang tests exercised relevant lifecycle modes. You did not establish an end-to-end PD deployment or author the disaggregation architecture. NCCL collective knowledge does not automatically prove a point-to-point KV-transfer implementation.

**Proposed question for the team:** “How do you decide which workloads benefit from disaggregation, and what is the biggest constraint in practice: transfer, routing or capacity balance?”

Source: [Baseten disaggregation](https://www.baseten.co/inference-engineering/book/05-techniques/disaggregation/).

## 14. Production: bridge kernel work to the LLM control plane

**Revise:** Baseten 7.2, 7.4 and 7.5.

**Likely question:** “How would you keep an inference optimization safe in production?”

**Proposed approach:** establish correctness and a representative performance baseline; test mixed traffic and failure behavior; deploy a canary with explicit acceptance criteria; watch errors, tail latency and useful throughput; roll back or hold if the evidence is negative or inconclusive. This is a design answer, not a claim of doing it on AWS products.

**Your work:** LLMCP deploys an OpenAI-compatible service, instruments streaming TTFT/errors/concurrency/queue depth, and separates scaling decisions from revision promotion. Its CPU p95-TTFT feasibility study supports that project's release gate; it does not establish production GPU-fleet scale.

**Autoscaling concept:** traffic growth, queueing, occupied request slots, KV capacity and cold-start time can matter more than CPU percentage. An aggressive scaling loop can still lose to slow model loading or poor capacity availability.

**Client concept:** timeouts, cancellation, retries and streaming completion semantics affect reliability and observed latency. Logging must remain useful and appropriately controlled; default/no-op behavior is relevant to your output-logging contribution.

Sources: [Autoscaling](https://www.baseten.co/inference-engineering/book/07-production/autoscaling/), [Testing/deployment](https://www.baseten.co/inference-engineering/book/07-production/testing-and-deployment/), [Client code](https://www.baseten.co/inference-engineering/book/07-production/client-code/), current CV.

## 15. Price-performance and what your results establish

**Likely question:** “How would you evaluate an improvement for AWS customers?”

> I would evaluate useful serving throughput at the required latency and quality, then relate it to the cost of the resources used. A microkernel speedup is valuable evidence, but the customer benefit depends on how much it improves the complete workload.

**Proposed framing:** compare accepted/completed useful output per unit cost under workload-specific TTFT/TPOT, error and quality constraints. Account for idle capacity, parallel workers and any extra draft/transfer resources. Do not present raw tokens/second as universal customer value.

**Illustrative Amdahl check:** if a component is 20% of total time and becomes twice as fast, total time becomes `0.8 + 0.2/2 = 0.9` of baseline: about 1.11× overall speedup. This is a teaching example, not a model-level result from your work.

| Confirmed CV result | What to qualify |
|---|---|
| 433 TFLOP/s BF16 | Particular kernel/shape; recover configuration and FLOP convention. |
| 1.1–1.3× SDPA | Long-sequence prefill regimes; not all workloads. |
| 13.6× naive decode | Different baseline from SDPA. |
| Peak 1.29× SDPA | Target GQA regimes. |
| 5.2× KV compression | Representation/storage result; not 5.2× model throughput. |
| +0.33% INT4 perplexity | Retrieve data/model and relative versus absolute interpretation. |
| 210 H100 tests | Evidence on covered cases, not proof of universal correctness. |
| Token-identical greedy integration | Particular tested settings; not universal floating-point identity. |
| Merged vLLM/SGLang fixes | Specific metrics, observability and regression contributions; kernels are a separate project. |

Sources: current CV; [NVIDIA assessment/Amdahl discussion](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#assess), [Baseten benchmarking](https://www.baseten.co/inference-engineering/book/04-software/performance-benchmarking-and-load-testing/). The cost framing is a proposed evaluation approach inferred from the JD.

## 16. Questions to ask and final rehearsal

Pick three for the informational conversation:

1. “Which is the immediate priority: kernels, inference-engine development, or AWS integration?”
2. “What evidence would the manager want beyond the projects and upstream work on my CV?”
3. “What do the next stages assess, and should I prepare Python, C++, CUDA/Triton, inference design or a combination?”
4. “How is the role leveled, and what architecture ownership does a successful mid-level engineer take on?”

**Sixty-minute revision:** 10 minutes on introduction/fit; 15 on one real kernel benchmark/profile; 15 on both PR mechanisms; 10 on speculation/disaggregation; 10 explaining the answers aloud without reading.

**Stop and verify rather than guessing:** exact H100 variant, tensor shapes, software/backend versions, test tolerances, benchmark repetitions, model/data behind perplexity, personal code change after profiling, current work authorization, start date, and whether the application was submitted.

**Avoid these overclaims:** four years of professional GPU work; production SageMaker/Bedrock/HyperPod ownership; authored speculative/disaggregated systems; upstream kernel acceleration from the metrics PRs; all 303 SGLang tests passed; universal SDPA superiority; retracted Oracle production-throughput claims.

## Source map

These are original role-focused coaching notes, not a chapter-by-chapter reproduction. The recommended videos are Spring 2025; some course pages now default to 2026.

| Revision material | Cards |
|---|---|
| CS336 Lecture 2, resource accounting | 3, 7 |
| CS336 Lecture 5, GPUs | 4, 5 |
| CS336 Lecture 6, kernels/Triton | 5, 8 |
| CS336 Lecture 10, inference | 2, 6, 7, 11, 12 |
| CS336 Lectures 7–8, parallelism | 11 |
| Baseten 1.4, metrics | 9 |
| Baseten 2.2/2.4/2.5, mechanics/bottlenecks/attention | 2, 3, 5, 6 |
| Baseten 3.1/3.3, hardware | 4, 13 |
| Baseten 4.1/4.3/4.4/4.5, software | 5, 8, 10, 11, 13 |
| Baseten 5.1–5.5, techniques | 7, 11, 12, 13 |
| Baseten 7.2/7.4/7.5, production | 14 |

Primary personal facts: current `cv.md` and profile. Conceptual explanations draw on the linked Stanford code, original FlashAttention-2 paper, NVIDIA documentation, Baseten sections and PR descriptions already reviewed. No new benchmark or implementation result has been inferred from those external sources.
