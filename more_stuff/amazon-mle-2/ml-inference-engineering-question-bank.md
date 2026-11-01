# ML and LLM inference engineering — cross-company question bank

**Engine-specific depth:** [vLLM/SGLang focus bank](inference-engines-question-bank.md), with current sources and small coding stages.

> **CURRENT STAGE — November 12, 2026, 2 PM EST (UTC−5):** 60-minute phone interview with Sathishkumar Sivashanmugam; live coding confirmed, recruiter says ML and LeetCode preparation. OA waived after a prior pass. Use the [current study plan](amazon-10587705-phone-study-plan.md) and [AWS research supplement](amazon-10587705-phone-research.md). Earlier OA-first schedules below are historical.

**Current daily schedule:** [Combined two-week study plan](amazon-10587705-two-week-study-plan.md). This supersedes earlier daily sequencing; question IDs remain unchanged.

**Researched:** October 28, 2026. **Audience:** mid-level ML/inference engineer, with optional deeper systems follow-ups. **Scope:** transformers, attention, serving, GPU kernels, and practical ML engineering across relevant AI companies. This is separate from the [Amazon OA bank](amazon-10587705-oa-question-bank.md); do not treat domain-loop questions as confirmed OA content.

## Evidence and use

There are **72 original practice exercises** below: 24 conceptual, 16 coding, 12 system design, 12 case studies and 8 ML-engineering exercises. Eight additional reported prompts/themes appear first. The original exercises include concrete requirements and answer checkpoints; they are not claimed verbatim interview questions.

- **Reported:** public candidate account, with company/round/date and limitations. A report is not independent confirmation that the company uses it today.
- **Original practice:** our prompt, informed by primary papers/documentation or an explicitly labeled reported theme. No company attribution is implied.
- **P0/P1:** training priority, not reported frequency. P0 targets the user's inference-optimization focus; P1 adds breadth/depth.

[Source ledger](ml-inference-engineering-sources.md) distinguishes firsthand accounts, promotional reposts and primary engineering references. Source IDs on each prompt resolve there. [Attempt tracker](ml-inference-engineering-attempts.csv) starts unattempted; the bank does not assert candidate readiness.

## What has actually been reported

| ID | Company / role / round | Reported question or theme, paraphrased | Evidence and practice connection |
|---|---|---|---|
| REP-01 | NVIDIA, Deep Learning Software Engineer—Inference, first technical phone screen | Explain CUDA kernels you worked on, optimizations, difficulties, and your own contribution. | R01; posted Jun 4, 2025; interview date/location/level unstated. Practice a truthful project deep dive, then CASE-02/12. |
| REP-02 | Same NVIDIA screen | Follow-ups on model serving and use of vLLM. | R01, same account, not independent corroboration. CON-08–12 are our expanded practice. |
| REP-03 | Same NVIDIA screen | Serialize and deserialize a binary tree. | R01; [LC297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) is the canonical practice analogue. Domain roles still test general coding. |
| REP-04 | Fireworks AI, Applied MLE | Reduce time to first token; discuss optimizations to a RAG take-home and past projects. | R02; posted Jul 31, 2026; exact interview date unstated. CASE-01 and DES-08 expand the theme. |
| REP-05 | Fireworks AI, AI Engineer, New York | Evaluate on a different dataset, justify model choice, and optimize latency following a text-to-SQL assignment. | R02; interviewed Aug 2026, posted Aug 17. ML-02/03/06 are original follow-ups. |
| REP-06 | Anthropic, SWE onsite, level unspecified | Implement a multiprocessing image pipeline, then reuse shared intermediate prefixes. | R03, recent Oct 2026 self-report, exact interview date unstated. Domain-adjacent caching exercise, not proof of kernel coding. |
| REP-07 | Same Anthropic onsite | Review an inference design; schedule models requiring one versus all eight GPU/compute units without starvation. | R03; practice batching, bounded queues and gang scheduling. DES-04 changes the scenario and is not a transcript. |
| REP-08 | Together AI, SWE onsite | Multi-cluster task scheduler; timestamped key-value lookup (LC981 analogue). | R04, Sep 17, 2026 promotional secondhand repost; LOW confidence. Useful optional practice, not verified process. |

No reliable exact attention/Triton coding transcript was found in this pass. Searches for Cerebras and other GPU/compiler roles yielded preparation requests or generic guides rather than attributable prompts. The original kernel/transformer exercises fill that practical gap transparently.

## Suggested starting sequence

1. CON-01–08: shapes, masks, KV arithmetic, RoPE and online attention.
2. CODE-01–05: write correct CPU/PyTorch references before GPU optimization.
3. CON-17–24, then CODE-09–11/13/15: hardware reasoning, kernels and measurement.
4. CON-09–16 and DES-01–03/05/07: serving tradeoffs and failure handling.
5. CASE-01/02/06/07/09/12 and ML-01/02/04/08: diagnose evidence, quantify claims and protect correctness.

Until the OA is complete, use this as a supplementary domain track rather than replacing timed OA practice. No GPU is required for conceptual work, design, CPU references or numerical exercises. Actual kernel correctness/performance claims require a compatible device; no GPU benchmarks have been run as part of building this bank.

## Practice rubric

Score 0–2 each for correctness, explicit assumptions, implementation/mechanism, validation/evidence, and tradeoff reasoning (10 total). This is our feedback rubric, not a company pass threshold. Conceptual answers should include a small example or derivation. Coding requires tests and complexity. Design requires numbers, a bottleneck and a failure path. Cases require a falsifiable hypothesis and the next measurement.

For your own project answers, distinguish authored code, integration, tests, measurements and team decisions. Trace claims to your existing resume/evidence audit; do not adopt synthetic case-study numbers as your results.

## Conceptual deep dives

### CON-01 — Attention shapes

**P0 · Conceptual · 8–12 min · Original practice · Sources: T01**

Given X with shape [B,T,D], derive Q, K, V, attention-score and output shapes for H heads. Where does the 1/sqrt(d_head) factor come from?

**Answer checkpoints:** Track projections and head reshaping; scaling controls dot-product variance under standard assumptions. Explain which axis softmax normalizes.

### CON-02 — Causal and padding masks

**P0 · Conceptual · 8–12 min · Original practice · Sources: T01,T06**

Why do we need both causal and padding masks? What changes when decoding a single token against a cached prefix?

**Answer checkpoints:** Use absolute query/key positions; unequal query and key lengths need correct causal alignment. Define fully masked-row behavior explicitly.

### CON-03 — GQA versus MHA and MQA

**P0 · Conceptual · 8–12 min · Original practice · Sources: T02**

Keep 32 query heads but use 8 KV heads. What changes in model weights, cache memory, and head mapping? Can we just drop heads from a checkpoint?

**Answer checkpoints:** Four query heads share each KV group. Savings concern KV, not every activation or parameter. Architecture/checkpoint conversion can affect quality.

### CON-04 — KV-cache arithmetic

**P0 · Conceptual · 8–12 min · Original practice · Sources: T02,T04**

For B=4, T=8192, L=32, Hkv=8, d=128 and two-byte cache elements, derive total KV storage without tensor parallelism.

**Answer checkpoints:** 2*B*T*L*Hkv*d*bytes = 4 GiB. Add allocator overhead, weights, workspace and temporary buffers separately; replication/sharding changes per-device memory.

### CON-05 — RoPE during cached decoding

**P0 · Conceptual · 8–12 min · Original practice · Sources: T03**

How do rotations encode relative position? What breaks if you rotate a cached key twice or restart position IDs for each decode step?

**Answer checkpoints:** Track absolute positions and consistent rotation convention; explain the relative-angle dot product. Position encoding is not equivalent to a causal mask.

### CON-06 — FlashAttention mechanism

**P0 · Conceptual · 8–12 min · Original practice · Sources: T06**

Explain how exact dense attention avoids materializing the full score/probability matrix. Does this make dense attention linear-time?

**Answer checkpoints:** Tiling and online normalization reduce memory traffic/storage; dense attention arithmetic remains quadratic in sequence length. Exact mathematical formulation does not mean bitwise-identical floating point.

### CON-07 — Online softmax derivation

**P0 · Conceptual · 8–12 min · Original practice · Sources: T06**

Maintain a running maximum m, exponential sum l, and unnormalized weighted value accumulator o. Derive updates when a new score/value tile arrives.

**Answer checkpoints:** m_new=max(m,max(tile)); rescale old l and o by exp(m-m_new), add new exp(score-m_new) contributions, normalize o/l at the end. Handle initialization and all-masked tiles.

### CON-08 — Prefill versus decode

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04,T09**

Explain why a large prefill can benefit from GEMM throughput while small-batch decode can be bandwidth-limited. When does that rule stop being useful?

**Answer checkpoints:** Reason from shapes, bytes and reuse; long-context cache reads, large batches, communication and launch overhead can change the bottleneck. Measure instead of labeling every decode memory-bound.

### CON-09 — Serving metrics

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04,T10**

Define TTFT, inter-token latency, time per output token, request throughput, output-token throughput and goodput. How can a system improve one while hurting another?

**Answer checkpoints:** State timestamp boundaries and warm/cold treatment. Separate queueing, prefill and decode; goodput counts work meeting an explicit SLO. Avoid averaging away tail behavior.

### CON-10 — Continuous batching

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04**

Contrast static and iteration-level batching. What happens when one request ends, another arrives, and a third runs out of KV capacity?

**Answer checkpoints:** Discuss admission, removal, token budgets, preemption/recomputation and fairness. Scheduling policy and cache management are linked.

### CON-11 — Paged cache versus prefix cache

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04,T05**

What different problems do paging and shared-prefix caching solve? What is copy-on-write needed for?

**Answer checkpoints:** Paging manages allocation/fragmentation; prefix reuse avoids repeated work/storage for matching prefixes. Sharing mutable tails requires care; neither guarantees a hit on arbitrary similar text.

### CON-12 — RadixAttention deep dive

**P0 · Conceptual · 8–12 min · Original practice · Sources: T05**

What information does a radix prefix structure retain? Explain reuse and eviction while requests still reference a prefix.

**Answer checkpoints:** Walk token-prefix matching, reference ownership and reclaimable leaves. Do not claim every current SGLang behavior follows the original paper; identify a version before implementation-specific answers.

### CON-13 — Speculative decoding correctness

**P1 · Conceptual · 8–12 min · Original practice · Sources: T07**

Why is accepting a draft token only when it equals the target argmax not a general sampling algorithm? Derive the acceptance test for distributions p and q.

**Answer checkpoints:** For the classical exact method use min(1,p(x)/q(x)); rejection samples from normalized positive p-q. Explain support, draft cost and target verification.

### CON-14 — Quantization tradeoffs

**P1 · Conceptual · 8–12 min · Original practice · Sources: T08**

Compare weight-only, weight+activation and KV-cache quantization. Which storage or bandwidth cost does each attack?

**Answer checkpoints:** Discuss scales, group/channel granularity, calibration distribution and actual kernel support. Smaller tensors do not guarantee faster end-to-end serving.

### CON-15 — Parallelism choice

**P1 · Conceptual · 8–12 min · Original practice · Sources: T09**

Contrast tensor, pipeline, data and expert parallelism for serving. What would make doubling tensor parallelism slower?

**Answer checkpoints:** Identify what is sharded/replicated and where communication enters; topology, small messages, batch size and synchronization matter.

### CON-16 — MoE inference

**P1 · Conceptual · 8–12 min · Original practice · Sources: T09**

Why can a model with fewer active parameters still have poor latency? How do routing skew and all-to-all traffic affect it?

**Answer checkpoints:** Separate total weights from active compute; account for dispatch/combine, expert imbalance and small expert batches. Explain capacity and dropped/rerouted-token semantics.

### CON-17 — GPU execution and memory

**P0 · Conceptual · 8–12 min · Original practice · Sources: T11**

Map grid, block, warp and thread onto the memory hierarchy. Explain coalescing versus shared-memory bank conflicts.

**Answer checkpoints:** Distinguish address patterns, access granularity and memory spaces; state hardware assumptions. Coalesced global loads do not prove conflict-free shared accesses.

### CON-18 — Roofline reasoning

**P0 · Conceptual · 8–12 min · Original practice · Sources: T12**

A kernel does 2 GFLOP and transfers 1 GB on a hypothetical GPU with 100 TFLOP/s and 1 TB/s. Estimate a lower bound.

**Answer checkpoints:** Compute bound 20 microseconds, memory bound 1 millisecond: max is 1 ms assuming decimal units and ideal execution. It is a bound, not a measured prediction.

### CON-19 — Occupancy and registers

**P0 · Conceptual · 8–12 min · Original practice · Sources: T11,T12**

Why might higher occupancy be slower? What evidence distinguishes latency hiding from register spilling?

**Answer checkpoints:** Trade register/shared-memory use against active work; inspect spills, stalls and throughput. Occupancy alone is not the objective.

### CON-20 — Fusion decision

**P0 · Conceptual · 8–12 min · Original practice · Sources: T13**

When is fusing residual addition, normalization and activation helpful, and when might splitting win?

**Answer checkpoints:** Estimate removed launches/intermediates versus register pressure, reuse and synchronization costs. Check supported shapes and numerical behavior.

### CON-21 — Triton tiling

**P0 · Conceptual · 8–12 min · Original practice · Sources: T14**

How would you choose BLOCK_M, BLOCK_N, BLOCK_K, warps and stages for a matrix multiplication family?

**Answer checkpoints:** Start with shapes/dtype/device constraints, then tune a bounded space and inspect resource use. Include tails and strides; one best tile need not generalize.

### CON-22 — JIT versus precompiled specialization

**P0 · Conceptual · 8–12 min · Original practice · Sources: T13,T14**

Design a precompiled Triton kernel catalog for known shape families. Which keys must dispatch consider, and what happens on a miss?

**Answer checkpoints:** Include target architecture, dtype/layout, shape constraints and compiler/build identity; bound variant growth, validate artifacts, and provide a correct fallback. Precompilation removes compilation cost, not inherently steady-state arithmetic.

### CON-23 — Numerical correctness

**P0 · Conceptual · 8–12 min · Original practice · Sources: T15**

Why can a fused reduction disagree with a framework reference? Define a validation strategy more useful than exact equality.

**Answer checkpoints:** Explain accumulation precision, ordering, error tolerance and extreme values. Use a high-precision reference where appropriate and evaluate model quality separately.

### CON-24 — Profiling method

**P0 · Conceptual · 8–12 min · Original practice · Sources: T12**

A kernel looks slow. What do you measure before changing code? Which questions belong to a timeline and which to kernel counters?

**Answer checkpoints:** First isolate launch gaps, synchronization and transfers; then inspect dominant kernels and relevant counters. Control warmup and instrumentation effects; profiler overhead can perturb timings.

## Coding exercises

### CODE-01 — Stable masked softmax

**P0 · Coding · 35–60 min · Original practice · Sources: T13**

Implement softmax(x, mask) over the last axis in NumPy/PyTorch primitives; forbidden: calling a built-in softmax. For this exercise a fully masked row returns zeros.

**Answer checkpoints:** Test huge logits, equal logits, one valid entry, all masked entries and noncontiguous input. Subtract the maximum and avoid invalid all-masked arithmetic.

### CODE-02 — Causal attention reference

**P0 · Coding · 35–60 min · Original practice · Sources: T01**

Implement attention(Q,K,V) for [B,H,T,D] tensors with explicit causal and padding masks; no scaled_dot_product_attention call. Return [B,H,T,Dv].

**Answer checkpoints:** Compare to a trusted reference; vary head/value dimensions, padding and dtype. State scale and dropout policy. Test that changing a future value cannot change an earlier output.

### CODE-03 — Decode with a KV cache

**P0 · Coding · 35–60 min · Original practice · Sources: T04**

Implement a one-token decode step that appends K/V and attends over the valid prefix. Cache capacity and valid length are explicit inputs; reject overflow.

**Answer checkpoints:** Cached results must match full recomputation with dropout disabled and consistent positions. Test capacity boundary, several steps and independent batch entries.

### CODE-04 — GQA attention mapping

**P0 · Coding · 35–60 min · Original practice · Sources: T02**

Extend the reference to Hq query heads and Hkv key/value heads where Hq is divisible by Hkv, without permanently duplicating the KV cache.

**Answer checkpoints:** Check Hq=Hkv, Hkv=1 and intermediate grouping against a repeat-based reference; verify output shapes and head mapping.

### CODE-05 — RoPE implementation

**P0 · Coding · 35–60 min · Original practice · Sources: T03**

Rotate even-dimensional query/key vectors using supplied positions and inverse frequencies; choose and document adjacent-pair layout.

**Answer checkpoints:** Position zero is identity; norms are preserved within tolerance; compare full-sequence and cached positions. Reject odd dimensions.

### CODE-06 — Top-p sampler

**P1 · Coding · 35–60 min · Original practice · Sources: Original algorithm exercise**

Given finite logits, temperature>0, p in (0,1], and a seeded RNG, implement nucleus sampling; keep the smallest sorted prefix whose mass reaches p.

**Answer checkpoints:** Keep at least one token, renormalize retained mass, test p=1, peaked/uniform distributions and deterministic sorting ties. Specify temperature=0 separately as greedy mode.

### CODE-07 — Tiny continuous-batch scheduler

**P1 · Coding · 35–60 min · Original practice · Sources: T04**

Implement a deterministic simulator. Each request has arrival tick, remaining prefill tokens and decode tokens; each tick has a token budget and active-sequence limit.

**Answer checkpoints:** Declare prefill/decode accounting, deterministic tie breaking, admission and completion rules. Test idle periods, cancellations, zero-length phases and a starvation bound. This is a simulator, not vLLM internals.

### CODE-08 — Paged block allocator

**P1 · Coding · 35–60 min · Original practice · Sources: T04**

Implement allocate, retain and release for fixed-size KV blocks; request block tables map logical blocks to physical IDs. Refcounts are explicit.

**Answer checkpoints:** No double allocation, no negative references, freed blocks reusable, shared blocks remain live until last owner releases. Define failure atomicity and zero-token behavior.

### CODE-09 — Row softmax in Triton

**P0 · Coding · 35–60 min · Original practice · Sources: T13**

Write a row-wise stable softmax kernel for rows fitting on-chip, with a mask for padded lanes. Support widths 1,127,128,129 and 1025.

**Answer checkpoints:** Use a framework reference, warm benchmarks and dtype-specific tolerances; separate compile time. Include a fallback for unsupported row sizes.

### CODE-10 — RMSNorm kernel

**P0 · Coding · 35–60 min · Original practice · Sources: T15**

Implement y=x*rsqrt(mean(x*x)+eps)*weight along the final dimension, using FP32 reduction for low-precision input.

**Answer checkpoints:** Test non-power-of-two widths, all-zero and large-magnitude input, epsilon semantics and output dtype. Compare separate versus fused residual variants only after correctness.

### CODE-11 — Tiled matrix multiplication

**P0 · Coding · 35–60 min · Original practice · Sources: T14**

Implement C=A@B in Triton with explicit strides and tail masks. Start FP16 input/FP32 accumulation; no cuBLAS call inside your implementation.

**Answer checkpoints:** Test rectangular and odd dimensions and transposed views; benchmark against a library baseline. Explain tile reuse before tuning.

### CODE-12 — Transpose and coalescing

**P1 · Coding · 35–60 min · Original practice · Sources: T11**

Write a CUDA or Triton transpose for a large rectangular matrix; compare naive and tiled strategies.

**Answer checkpoints:** Check non-square tails, exact indexing and alias restrictions. Explain read/write transaction patterns; avoid claiming a faster result without device measurements.

### CODE-13 — Fused residual and activation

**P0 · Coding · 35–60 min · Original practice · Sources: T13**

Implement y=SiLU(x+bias)+residual, with row-broadcast bias. Preserve stated dtype and strides or reject unsupported layouts.

**Answer checkpoints:** Compare numerical output and bytes moved with separate operators. Test saturation regions and tails. Report both small launch-bound and large bandwidth-sensitive shapes.

### CODE-14 — Online attention accumulator

**P1 · Coding · 35–60 min · Original practice · Sources: T06**

Implement a CPU reference for tiled online softmax attention using running (m,l,o); do not construct the full score matrix.

**Answer checkpoints:** Match dense attention across tile sizes and adversarial logits. Test masked initial tiles and tail tiles. Explain why averaging independently normalized tile outputs is wrong.

### CODE-15 — Benchmark harness

**P0 · Coding · 35–60 min · Original practice · Sources: T12,T15**

Implement a harness reporting compile/cold latency separately from warmed median and p95, plus correctness checks and a shape matrix.

**Answer checkpoints:** Synchronize GPU measurement appropriately, preserve raw samples, record device/software/dtype, and reject empty sample sets. Compare equivalent work; avoid timing only enqueue cost.

### CODE-16 — Prefix-cache lookup

**P1 · Coding · 35–60 min · Original practice · Sources: T05**

Implement longest token-prefix matching with reference counts and an eviction policy that never deletes pinned entries. Use integer token arrays, not raw-text substring matching.

**Answer checkpoints:** Test shared prefixes, diverging suffixes, empty input and pinned-cache exhaustion. Return matched length and ownership handle. Document tenant/model isolation in the cache key.

## System design

### DES-01 — Interactive LLM serving

**P0 · System design · 40–50 min · Original practice · Sources: T04**

Design a service for 100 requests/s, median 2k input and 300 output tokens, p95 TTFT<1s and inter-token latency<50ms. GPU throughput is unknown; request measurements instead of guessing fleet size.

**Answer checkpoints:** Separate gateway, queues, scheduler, workers and streaming. Budget KV and throughput, define admission/cancellation, load tests and failure handling.

### DES-02 — Prefill/decode disaggregation

**P0 · System design · 40–50 min · Original practice · Sources: T10**

Long prompts cause interactive decode stalls. Design separate prefill and decode pools and explain when transfer cost makes it a bad choice.

**Answer checkpoints:** Account for KV transfer volume, routing, backpressure, topology and state ownership. Compare against colocated chunked-prefill baseline.

### DES-03 — Multi-tenant prefix reuse

**P0 · System design · 40–50 min · Original practice · Sources: T05**

Customers share common system prompts but require isolation. Design cache identity, routing, eviction and accounting.

**Answer checkpoints:** Include model/tokenizer/adapter versions, tenant boundary and token identity. Quantify benefit against memory pressure; cancellation must release ownership.

### DES-04 — Multi-cluster scheduler

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

Design placement for jobs requesting 1,2,4 or 8 GPUs across two clusters with different interconnects. Include priority, deadlines and gang allocation.

**Answer checkpoints:** Avoid partial gang deadlock and starvation. Define leases, stale-worker detection, retries and topology-aware placement. Inspired by weak report R04; details are ours.

### DES-05 — Precompiled kernel service

**P0 · System design · 40–50 min · Original practice · Sources: T14**

Build a pipeline that compiles, validates, benchmarks and distributes Triton variants for known production workloads.

**Answer checkpoints:** Artifact keys, reproducibility, correctness gates, shape coverage, versioned rollout and fallback; limit autotuning cost and prevent silently selecting incompatible binaries.

### DES-06 — Quantized model launch

**P1 · System design · 40–50 min · Original practice · Sources: T08,T16**

Roll out an INT8/INT4 serving variant under a quality floor and cost target. What artifacts, evaluations and rollback conditions are required?

**Answer checkpoints:** Pin calibration and evaluation sets; test workload slices, kernels, latency tails and memory; shadow/canary deployment and versioned rollback.

### DES-07 — Benchmark platform

**P0 · System design · 40–50 min · Original practice · Sources: T04,T05**

Design fair comparisons among vLLM, SGLang and another engine for a specific workload.

**Answer checkpoints:** Pin model/tokenizer/dtype/device and request distributions; report SLO-constrained goodput, cold/warm costs and quality. Vary concurrency and prompt lengths; preserve reproducible configs.

### DES-08 — RAG inference path

**P0 · System design · 40–50 min · Original practice · Sources: R02,T16**

Design a document assistant with citations and a strict TTFT budget. Explain retrieval, reranking, context construction and generation tradeoffs.

**Answer checkpoints:** Instrument stage latencies and quality separately; use bounded context, provenance and evaluation by document/query slice. Do not assume a larger model repairs retrieval failure.

### DES-09 — LoRA serving

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

Serve many tenant adapters over one base model. Design admission, adapter residency and batch formation.

**Answer checkpoints:** Key caches by adapter identity, bound adapter-loading latency, prevent tenant mixups, and compare shared batching versus dedicated pools.

### DES-10 — Long-running batch inference

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

Process a large offline corpus with restartability and a completion deadline while sharing capacity with online traffic.

**Answer checkpoints:** Durable tasks/checkpoints, idempotent output writes, priority/preemption, token-aware estimates and cost accounting; protect online SLOs.

### DES-11 — Streaming API failure

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

A client disconnects after receiving some tokens and retries. Design request identity, cancellation and replay semantics.

**Answer checkpoints:** Separate transport disconnect from computation lifecycle. Define at-most-one active generation if required, bounded replay storage and billing; do not promise identical stochastic continuation without retained state.

### DES-12 — GPU fleet rollout

**P0 · System design · 40–50 min · Original practice · Sources: T12,T15**

Deploy a new attention kernel to mixed GPU architectures without silently changing outputs or taking down serving.

**Answer checkpoints:** Compatibility matrix, offline differential tests, shadow/canary, per-shape regression gates and fast rollback; watch compilation misses and tail latency.

## Performance and debugging cases

### CASE-01 — TTFT regresses after batching

**P0 · Case study · 15–20 min · Original practice · Sources: R02,T04**

Synthetic measurements: p95 TTFT rises from 0.8s to 2.1s; output-token throughput rises 25%; decode interval is unchanged. What do you measure and change?

**Answer checkpoints:** Separate queue delay and prefill duration; inspect admission/window and prompt mix. Throughput improvement alone does not meet the latency SLO. Propose one controlled experiment.

### CASE-02 — Fusion loses in production

**P0 · Case study · 15–20 min · Original practice · Sources: T12,T13**

A fused kernel wins 30% at width 4096 but loses 20% at 8192. The numbers are hypothetical. Explain plausible mechanisms and a dispatch decision.

**Answer checkpoints:** Inspect registers/spills, occupancy and memory traffic; validate benchmarks and numerical behavior. Gate by measured shape/device regimes rather than declare fusion universally better.

### CASE-03 — Higher cache hit rate, worse latency

**P0 · Case study · 15–20 min · Original practice · Sources: T05**

Prefix-cache hit rate increases from 40% to 80%, but p99 latency doubles. What could explain it?

**Answer checkpoints:** Check definition of hit rate, saved tokens/work, KV pressure, routing imbalance, eviction and queueing. Cache-hit percentage is not saved compute or end-to-end latency.

### CASE-04 — Quantization fails one slice

**P1 · Case study · 15–20 min · Original practice · Sources: T08,T15**

Aggregate accuracy is stable after quantization, but long-context extraction loses 8 percentage points. What is your investigation plan?

**Answer checkpoints:** Verify statistical support and preprocessing; isolate weights/activations/cache quantization, calibrate on representative inputs, compare logits/layers and consider selective precision.

### CASE-05 — Four GPUs do not beat two

**P1 · Case study · 15–20 min · Original practice · Sources: T09**

Tensor-parallel degree doubles from 2 to 4 but median decode latency worsens. Give three falsifiable hypotheses.

**Answer checkpoints:** Communication/topology, smaller GEMMs, or synchronization/placement; profile collectives versus compute and hold batch/context constant. Quantify memory benefit separately.

### CASE-06 — Impossible benchmark speedup

**P0 · Case study · 15–20 min · Original practice · Sources: T12**

A GPU operation allegedly completes in 0.5 microseconds while the reference takes 100 microseconds. What invalidates the comparison?

**Answer checkpoints:** Check asynchronous timing, warmup, output use, shapes, dtype, graph capture and synchronization; preserve raw samples. Do not reject a result solely because it is surprising.

### CASE-07 — OOM with apparently free memory

**P0 · Case study · 15–20 min · Original practice · Sources: T04**

The dashboard shows several GB free, yet a long request fails allocation. Walk through diagnosis.

**Answer checkpoints:** Distinguish device memory, engine cache pool, allocator fragmentation, reservation, graph/workspace peaks and concurrent growth. Estimate request KV before changing limits.

### CASE-08 — Speculation is slower

**P1 · Case study · 15–20 min · Original practice · Sources: T07**

Draft acceptance is high but wall-clock latency worsens. How can that happen?

**Answer checkpoints:** Draft generation, verification cost, batch/context regime, communication and scheduling overhead can exceed saved steps. Measure accepted tokens per total cost, not acceptance alone.

### CASE-09 — Cold start misses SLO

**P0 · Case study · 15–20 min · Original practice · Sources: T14**

Warm requests are fast; the first request for a shape takes several seconds. Design a remedy and proof.

**Answer checkpoints:** Separate model loading, compilation, autotuning and graph capture. Prewarm or precompile bounded hot variants, retain fallback and measure cold paths explicitly.

### CASE-10 — Tail shapes are wrong

**P0 · Case study · 15–20 min · Original practice · Sources: T06,T15**

Attention outputs pass tests at lengths 128 and 256 but fail at 129. What do you inspect first?

**Answer checkpoints:** Tail masks, strides, block bounds, causal alignment and uninitialized lanes. Use smallest failing case and differential tests before changing arithmetic.

### CASE-11 — GPU utilization is low

**P1 · Case study · 15–20 min · Original practice · Sources: T12**

A service has low reported GPU utilization and high end-to-end latency. Would you buy more GPUs?

**Answer checkpoints:** Inspect CPU tokenization, request arrival, batching, copies, launch gaps and synchronization before scaling. Utilization aggregates cannot identify the bottleneck.

### CASE-12 — Kernel claim versus service gain

**P0 · Case study · 15–20 min · Original practice · Sources: Original quantitative exercise**

Your kernel is 2x faster and originally consumed 20% of request time. Estimate ideal total speedup; explain what makes reality worse.

**Answer checkpoints:** Amdahl bound is 1/(0.8+0.2/2)=1.111x, about 10% latency reduction. Changed overhead, contention or workload mix can reduce it. State sequential-fraction assumptions.

## ML engineering fundamentals

### ML-01 — Data leakage

**P0 · ML engineering · 15–30 min · Original practice · Sources: T16**

Validation quality is excellent but live performance is poor. How do you detect duplicates, temporal leakage and label contamination?

**Answer checkpoints:** Audit data lineage and split by deployment unit/time, then test on a genuinely held-out distribution. Distinguish leakage from serving skew.

### ML-02 — Evaluation design

**P0 · ML engineering · 15–30 min · Original practice · Sources: R02**

Compare two models for text-to-SQL across unseen database schemas. What do you score besides exact-string match?

**Answer checkpoints:** Execution correctness and semantic equivalence, schema-generalization splits, latency/cost and error categories. Handle invalid/unsafe queries in a sandbox; report uncertainty.

### ML-03 — Distribution shift

**P1 · ML engineering · 15–30 min · Original practice · Sources: T16**

A new customer has different prompt lengths, terminology and language. How do you decide between retrieval changes, prompting, fine-tuning and a different model?

**Answer checkpoints:** Build a representative labeled sample and baseline; localize failure before choosing intervention. Measure quality/latency per slice.

### ML-04 — Training-serving skew

**P0 · ML engineering · 15–30 min · Original practice · Sources: T16**

Offline embeddings improve retrieval but online quality degrades. Where could the mismatch be?

**Answer checkpoints:** Check preprocessing, model/tokenizer versions, index refresh, normalization and similarity metric. Make artifacts reproducible and compare actual served inputs.

### ML-05 — Numerical ML debugging

**P1 · ML engineering · 15–30 min · Original practice · Sources: T15**

Loss becomes NaN after moving to lower precision. How do you localize the first invalid tensor and evaluate a fix?

**Answer checkpoints:** Trace a minimal batch, inspect activations/gradients and optimizer state, review overflow/underflow and scaling; compare an appropriate higher-precision run.

### ML-06 — Cost-quality model selection

**P1 · ML engineering · 15–30 min · Original practice · Sources: Original ML exercise**

A smaller model costs half as much per token but emits longer answers and retries more often. How do you compare it with a larger model?

**Answer checkpoints:** Use cost per successful task under quality and latency constraints, including retries, input/output lengths and failure cost; compare representative workloads.

### ML-07 — Canary evaluation

**P1 · ML engineering · 15–30 min · Original practice · Sources: T16**

A new model improves a benchmark but customer complaints rise. Design a rollout and investigation strategy.

**Answer checkpoints:** Use baseline comparison, task slices, operational metrics and delayed feedback; preserve rollback and examine whether the benchmark represents customer needs.

### ML-08 — Loss and perplexity coding

**P0 · ML engineering · 15–30 min · Original practice · Sources: T15**

Implement stable token-level cross entropy and perplexity from logits and target IDs with an ignore mask. No built-in cross-entropy function.

**Answer checkpoints:** Use logsumexp; average over valid tokens only; define no-valid-token behavior. Test extreme logits and padding; compare to a trusted implementation.

## Mock rounds

- **Transformer coding, 60 minutes:** CODE-02 (35), CON-03/04 (15), test review (10).
- **Kernel engineering, 60 minutes:** CODE-09 (35), CON-18/19 (15), benchmark critique (10). Implement a CPU reference if a compatible GPU is unavailable; do not mark the GPU portion tested.
- **Inference systems, 60 minutes:** DES-01 (40), CASE-01 (15), explicit unknowns (5).
- **Project defense, 45 minutes:** one real Triton/vLLM/SGLang contribution (15), implementation/correctness follow-ups (15), performance attribution and limits (15).

### Change log

- 2026-10-28: Initial cross-company bank with 72 original exercises and 8 reported prompts/themes. All attempt statuses unattempted. Kept separate from the Amazon OA bank. Company evidence strongest for a specific NVIDIA screen and Fireworks applied-ML themes; exact kernel interview transcripts remain sparse.
