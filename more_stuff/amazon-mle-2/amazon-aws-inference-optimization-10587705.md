# Amazon AWS MLE II — interview preparation guide

**Inference-engine research update:** [32 vLLM/SGLang questions](inference-engines-question-bank.md) and [evidence/readings](inference-engines-research.md). The current phone plan now assigns these within its existing domain blocks.

> **CURRENT STAGE — November 12, 2026, 2 PM EST (UTC−5):** 60-minute phone interview with Sathishkumar Sivashanmugam; live coding confirmed, recruiter says ML and LeetCode preparation. OA waived after a prior pass. Use the [current study plan](amazon-10587705-phone-study-plan.md) and [AWS research supplement](amazon-10587705-phone-research.md). Earlier OA-first schedules below are historical.

**Current preparation schedule:** [OA-first two-week plan with daily inference fundamentals](amazon-10587705-two-week-study-plan.md).

> **October 28, 2026 — current stage supersedes the October 27 plan below.** Suraj reports the recruiter conversation went well. Immediate priority is the online assessment, available within two weeks: **70 minutes LeetCode-style coding, 20 minutes AI coding, 20 minutes system design, 10 minutes behavioral**. Official documentation is pending; question count, platform, assistance rules and exact expiry remain unknown. Start with the [OA question bank](amazon-10587705-oa-question-bank.md), [scenario drills](amazon-10587705-oa-scenarios.md) and [research ledger](amazon-10587705-oa-sources.md). The earlier kernel-focused preparation remains relevant for later technical rounds but is not the current two-week OA plan.
>
> **Later stages, user-reported October 28:** telephone interview with 30 minutes behavioral and 30 minutes coding; then a four-hour loop with three coding rounds and one system-design round, with behavioral questions in every round. These are provisional until the official packet. No exact interview dates reported.

## Historical preparation — October 27

**Requisition:** [10587705 — AWS Inference Optimization](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization)  
**Updated:** October 27, 2026, after the Senior Director conversation.  
**Next conversation:** Sree Natarajan, Sr. Technical Recruiter, AWS Talent Acquisition; Wednesday **October 28 at 10:30 a.m. ET** (New York EDT; 7:30 a.m. Pacific). The pasted email proposes this time; acceptance and meeting details have not been independently checked.  
**Priority:** Suraj's sole current interview-preparation target, per his October 27 instruction.  
**Start with:** [Recruiter call brief](amazon-10587705-recruiter-brief.md).  
**Resume located:** [October 26 tailored PDF](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.pdf), with matching editable `.tex`. This is the role-specific artifact already linked in CareerOps; the portal upload itself was not inspected.  
**Supporting material:** [Project/PR evidence audit](amazon-10587705-project-pr-review.md), [technical revision notes](amazon-10587705-inference-revision-notes.md), [captured JD](supporting/aws-inference-optimization-10587705-2026-10-26.md).

## 1. What we know and how it changes preparation

Your report of today's call is our strongest team-specific preparation signal. The Senior Director liked the vLLM/SGLang work and said she would try to get interviews scheduled. That is positive support; technical rounds and dates remain pending. Her name was not specified in today's message, so this update does not assume she is the earlier contact named in the historical notes.

| Evidence | What it establishes | Preparation consequence |
|---|---|---|
| User-reported Director conversation, October 27 | Profiling, kernel tuning, precompiled Triton kernels for specific workloads, fusion, problem solving | Put GPU performance reasoning and implementation at the center. |
| Director's outline, as relayed by Suraj | Phone screen, then loop with likely standard/AI coding, domain coding, domain design | Prepare these tracks; exact number, durations, language, and AI policy are not confirmed. |
| Sree's pasted email | Wants to understand background and experience; proposes October 28, 10:30 ET | Treat tomorrow as recruiter fit/logistics preparation. Do not equate it automatically with the Director's technical phone screen. |
| Exact JD | Inference engines, kernels, benchmarking and customer-facing price-performance; speculative decoding/disaggregation also named | Connect microkernel work to measurable serving outcomes. |
| Public Amazon SDE II guidance | Coding, design, behavioral evidence, ownership and communication | Useful adjacent baseline; it is not this MLE team's interview packet. |

The JD supports an inference-systems emphasis. It does not establish that this is a Neuron/Trainium team. Do not redirect the plan toward NKI solely because neighboring AWS jobs mention it. Ask which hardware this team targets. [Exact posting](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization)

**Working mid-level bar [inferred]:** independently take a bounded optimization from problem definition through profiling, implementation, correctness checks, benchmark evidence and rollout reasoning. Explain alternatives and limitations clearly. Confirm the internal level with Sree rather than assuming MLE II means a specific level in every context.

## 2. Research findings: exact-team evidence versus adjacent accounts

Research performed October 27 across Amazon's official hiring pages, the exact requisition, AWS engineering publications, and public candidate accounts. Searches included the exact team title, inference/Triton interview combinations, Amazon MLE/II, AWS SDE II, Glassdoor, LeetCode and Blind. **No independently attributable interview account for requisition 10587705 or this exact inference-optimization team was found.** No exact-team question frequencies, pass rates or guaranteed loop blueprint can be supported.

| Source and date context | Visible report | Relevance and limitation |
|---|---|---|
| [Amazon SDE II official prep](https://amazon.jobs/content/en/how-we-hire/sde-ii-interview-prep), accessed Oct 27 | Describes coding, system design, LPs, and a four-interview loop; its public OA description is conventional coding/design/work-style content | High authority for its stated SDE process; adjacent role. Do not impose its timings or OA on this MLE opening. |
| [Amazon MLE II account](https://www.onsites.fyi/Amazon/Machine%20Learning%20Engineer/001DC8E474), date/location/team not exposed | Trees, monotonic stack, team-scenario design, ML breadth and behavioral questions | Correct public level label; anonymous, undated and not inference-team-specific. Useful evidence to retain general coding and ML basics. |
| [AWS SDE II candidate](https://www.reddit.com/r/leetcode/comments/1vz16fx/aws_sdeii_overall_experience_oa_loop/), retrieved page says “1mo ago”; search said two months | Author specifies Seattle/remote in comments; reports DSA plus AI-assisted repository debugging in OA, design/coding/LPs in loop | Adjacent AWS level; self-report, not verified. Relative publication labels disagree, so no exact date is asserted. |
| [Amazon MLE US remote account](https://www.tryexponent.com/experiences/amazon-machine-learning-engineer-interview-ab2bf7), interview displayed as two years ago; title says 2024 | Recruiter → OA → final; mentions monitoring, ML fundamentals and LPs; visible prompts concern KNN bias/variance and LLM evaluation | Older, level/team unknown; only accessible text used. |
| [Glassdoor junior/mid MLE](https://www.glassdoor.com/Interview/mid-level-machine-learning-engineer-interview-questions-SRCH_KO0%2C35.htm), May 25, 2025 | Short Python task and explaining the solution | Thin public snippet; team and location absent. Not a detailed interview review. |
| [LeetCode Amazon Applied Data Scientist](https://leetcode.com/discuss/post/6871782/amazon-online-1st-round-bengaluru-applie-uiwk/), May 2025, Bengaluru | Attention Q/K/V, causal masking, stochastic generation, bias/variance; further coding/project discussion expected | Different role and location. Fundamentals refresher only. |

Additional reports were screened, not promoted to primary evidence: a [self-described SDE-2/L5 account](https://www.reddit.com/r/FullStackDevelopers/comments/1u8y35h/amazon_sde2_l5_selected_full_loop_incl_the_new/) includes promotional links and unclear location; several other search results repeat the same account across forums. A [2024 MLE/L5 Reddit result](https://www.reddit.com/r/leetcode/comments/1eqqlj2) could not be opened, so its hidden details are excluded. Blind queries yielded no usable team-specific account. Glassdoor salary search did not yield a defensible requisition-level estimate.

**Research conclusion:** your Director's outline should outweigh generic candidate anecdotes. AI-assisted repository debugging exists in adjacent candidate reports, but neither those reports nor the phrase “Std AI Coding probably” confirms an AI-assisted loop for you. Ask whether it means AI-assisted debugging, AI/ML implementation, or conventional algorithms—and obtain the permitted-tool rules.

## 3. Tomorrow's recruiter conversation

Your objective is to turn the positive technical connection into a clearly specified next step. Be concise about fit, accurate about experience, and prepared on logistics.

### Opening: approximately 60–75 seconds

> I'm a software engineer with nearly four years of professional experience at Oracle and Incture, and I completed my master's at NYU in May. My recent work focuses on GPU performance and LLM inference. I've built Triton attention and KV-cache kernels on H100, and contributed merged fixes to vLLM and SGLang around inference measurement and request-lifecycle correctness. My earlier work gave me a foundation in backend performance, test infrastructure and automation. I spoke with the Senior Director yesterday, and the team's focus on profiling, kernel tuning and fusion aligned closely with the work I want to do. I'm excited to understand the next steps for this role.

Use “yesterday” on October 28. Avoid claiming four years of professional GPU optimization. Your kernel work and open-source contributions are recent project experience.

### Likely recruiter prompts [inferred from invitation/JD]

| Prompt | Answer direction |
|---|---|
| Why this team? | The combination of profiling, kernel implementation and serving-stack integration matches your actual work. You want to turn measured improvements into reliable customer-facing inference. |
| Strongest relevant project? | TritonAttn: prefill/decode/KV quantization, H100 correctness tests, Nsight diagnosis. One result and its workload boundary; technical details only if requested. |
| What did you contribute upstream? | vLLM: consistent streaming timing boundaries. SGLang: cumulative wait accounting across queue re-entry. Explain why trusted measurement matters before optimization. |
| Why the career transition? | Professional systems work → NYU master's → hands-on inference projects and upstream contributions. Master's completed May 2026; do not represent subsequent independent work as employment. |
| Have you deployed on Bedrock/SageMaker/HyperPod? | No established production ownership of those products. Adjacent evidence: cloud automation, inference internals and Kubernetes serving projects. |
| Architecture requirement? | Describe actual Incture service design and Oracle test-infrastructure decisions. Do not derive “two years of architecture” automatically from employment tenure. |
| Start date / other processes? | Exact truthful availability and genuine deadlines only. Current details need your own confirmation. |

**Compensation:** the posting lists Santa Clara base **$165,200–$223,600**, with sign-on and RSUs. Suggested wording: “Could you share the internal level and expected total compensation structure for this requisition? I'd like to calibrate to the scope and full package.” Your saved target/minimum are blank. Do not pre-commit to a range you have not chosen. [Posting](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization)

For context only, [Levels.fyi's US Amazon MLE page](https://www.levels.fyi/companies/amazon/salaries/machine-learning-engineer), updated October 12, shows about $287k L5 total compensation. It does not establish this role's level, Santa Clara offer band, or a suitable personal target. Ask about base, year-by-year sign-on, equity vesting and relocation separately.

**Work authorization:** saved profile says F-1. Prepare your actual current authorization category, expiration date and future sponsorship needs from your documents. Do not assume OPT/STEM dates or eligibility. This is a factual recruiter discussion, not an immigration determination.

**Location:** Santa Clara is the posted location. State your actual relocation preference, then ask about work arrangement. **Call logistics:** the email says “quick chat” without duration or platform. Check the invite/phone details; keep the resume and brief available.

### Ask these in priority order

1. “Following my conversation with the Senior Director, what is the next assessed round, and what will it cover? Is there an online assessment before the phone screen?”
2. “Could you share the round-by-round interview plan, durations and preparation material? For the coding round, is it conventional coding, AI-assisted repository work, or ML-specific implementation?”
3. “For domain coding, should I expect Python/PyTorch, Triton, CUDA/C++, or a choice? Will there be GPU execution, profiling output, or just an editor? What tools and documentation are permitted?”
4. “Does domain design emphasize an inference service, engine internals, or kernel compilation and deployment? Is there also a general ML breadth component?”
5. “How is this MLE II requisition leveled internally, and what timeline is the team targeting?”
6. Confirm location, authorization/sponsorship routing and compensation structure as time permits.

If time is short, prioritize 1–3 and necessary eligibility logistics. Ask the recruiter to obtain technical specifics from the team if she does not have them. Close: “I'm interested in moving forward. Is there anything about my background I should clarify before the technical screen, and what is the next action on each side?”

## 4. Evidence to defend from the submitted-role resume

Candidate claims below trace to current `cv.md` and the role-specific resume; caveats come from the existing October 27 source audit. The audit is not a rerun of benchmarks. The story-provenance script was run, but its success does not override explicit uncertainty in the Oracle evidence reset.

| Story | What you should be able to explain | Boundary |
|---|---|---|
| TritonAttn | Problem shape, mapping, numerical method, bottleneck, chosen change, correctness reference, comparison and losing regimes | 13.6× is versus naive decode; peak SDPA result is a different comparison. Never present either as universal. |
| vLLM #55508 | Why TTFT and inter-arrival timestamps disagreed; tokenless trailer handling; deterministic regression tests | Metric correctness, not engine acceleration. A streaming chunk is not necessarily one token. |
| SGLang #39312 | Retraction, repeated waits, accumulation, idempotent closure, serialization/clock rebasing, retained histogram contract | Did not change scheduling policy. Existing audit records a later caller-path caveat; randomized lifecycle tests do not prove all integration paths. |
| LLMCP | Reconciliation, revision state, canary gates, insufficient evidence, queue-based scaling, rollback | Project and CPU feasibility evidence; do not imply a production GPU fleet. |
| Oracle parallel tests | Shared interface-object setup, verification versus mutation, parallel/sequential grouping, TeamCity distribution | Approximate full then-existing test pipeline: 10–11 hours to within 3. No unchanged-compute or production-throughput claim. |
| Incture | SQL plans/indexing/pools and backend design | Resume metrics need a defensible recollection of baseline, workload, measurement window and personal action before detailed retelling. |

**Kernel numbers:** retain 210 H100 tests and shape-qualified prefill results when useful. The existing report audit records peak BF16 prefill at B=4, H=16, D=128, N=16,384, non-causal, H100 80GB; verify against the report before a technical discussion. Its decode comparison wins only 2/72 SDPA configurations. The approximately 5.24× compression is an INT2 experiment; +0.33% perplexity is a separate INT4 experiment. Do not combine them into one operating point. [Prior audit and original source links](amazon-10587705-project-pr-review.md)

For each main story, prepare a six-line evidence card: **problem; my change; why this choice; proof; limitation; next experiment**. Speak the one-minute version first. Keep a five-minute technical expansion available. We still need to elicit your actual discovery sequence and rejected alternatives rather than invent them from a patch.

## 5. Technical curriculum, ordered by the Director's signal

All exercises in sections 5–7 are **[inferred from Director/JD]**, not reported interview questions. Read for the specific task, then close the material and explain or implement it.

### A. Profiling: diagnose before optimizing

Practice a repeatable sequence: define the workload and latency objective; reproduce; separate cold compilation from warmed execution; find time on the critical path; isolate the relevant kernel; test one explanation; remeasure correctness and end-to-end performance.

Use Nsight Systems for CPU/GPU timelines, launch gaps, transfers and synchronization. Use Nsight Compute to investigate a selected kernel's execution and memory behavior. Verify the actual launch/name/shape—you have a concrete prior audit example where the wrong reduction kernel was selected. Treat profiler replay and collection overhead separately from benchmark timing. [Nsight Systems](https://docs.nvidia.com/nsight-systems/UserGuide/index.html), [Nsight Compute profiling guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)

**Exercise P1:** a kernel is faster but serving p99 is worse. Offer competing explanations: larger batching/queue delay, another critical-path stage, launch/transfer overhead, changed output lengths, cache behavior or measurement boundaries. State which trace or controlled experiment distinguishes them.

**Exercise P2:** low occupancy and high register usage. Explain a smaller tile or changed launch configuration as a hypothesis; predict possible spills, reduced reuse or extra work. High occupancy is not the objective—lower latency for equivalent correct work is. [CUDA best practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)

**Ready when:** you can interpret a real profile for ten minutes, separate observation from hypothesis, and propose a falsifiable next experiment.

### B. Kernel tuning and GPU fundamentals

Review coalescing, strides, tiling, register/shared-memory limits, warps, synchronization, tensor-core-friendly work and masked tails. In Triton, connect program IDs and pointer expressions to tensor coordinates; distinguish compile-time constants from runtime parameters. Tune tile sizes, warps and stages on a workload matrix rather than a single favorable shape. [Triton matmul tutorial](https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html)

**Exercise K1:** explain why a bigger tile can improve reuse yet reduce performance. **K2:** derive offsets for a strided batched tensor and handle partial tiles. **K3:** compare an under-parallelized low-batch decode kernel with a split-KV implementation, including the reduction cost.

**Ready when:** you can write and explain a small correct reduction kernel, identify its assumptions, and describe a tuning experiment without claiming a result you have not measured.

### C. Fusion

Start with stable row softmax or residual-add plus RMSNorm. Fusion can avoid intermediate global-memory traffic and launch overhead; it can also increase live values, resource use and implementation complexity. A good answer identifies the work removed and the constraints added. [Triton fused softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)

**Exercise F1:** implement row softmax, masking padded columns with negative infinity and defining behavior for entirely masked rows. Test odd widths, extreme values and dtype tolerances. **F2:** for a proposed fused normalization path, account for reads/writes and identify whether the residual output must also be retained. **F3:** give a workload where fusion is slower and a way to detect it.

**Ready when:** you can defend a fusion boundary using correctness and measured memory/launch savings, including a losing regime.

### D. Precompiled and workload-specialized Triton kernels

This is the most important newly identified study area. The Director's phrase could mean ahead-of-time compilation, prewarming a JIT cache, offline autotuning, or a library of specialized variants; those are related but distinct. Ask the team which they mean.

Triton's public AOT tool accepts typed signatures, specialization hints and compile-time values and produces launchable artifacts. Compilation before serving can remove request-path compilation work; it does not by itself improve the steady-state instructions of an identical kernel. [Triton AOT compiler source](https://github.com/triton-lang/triton/blob/main/python/triton/tools/compile.py)

**Proposed design exercise A1:** design a specialized-kernel registry. Define keys for operation, GPU target, dtype, shape/layout constraints, causal mode and code/compiler version. Use representative shape buckets, offline tuning, correctness checks and measured promotion. At runtime validate guards, choose a compatible variant and fall back safely on unsupported input. Track fallback frequency, cold-start time and service latency. Avoid compiling every possible combination: coverage, build cost and artifact size are competing objectives.

These registry choices are our design exercise, not a claim about Amazon's implementation. Discuss cache invalidation, version compatibility, rollout/rollback, and why an alignment assumption must be checked before dispatch. **Ready when:** you can explain cold versus warm behavior, specialization benefits, variant explosion and correctness-preserving fallback in five minutes.

### E. Attention, decode and numerical reasoning

Be able to derive stable softmax: subtract the maximum, exponentiate and normalize. For online attention, maintain running max `m`, normalization `l`, and unnormalized output `a`. Combining a new score tile uses `m_new=max(m,max(tile))`, rescales old `l` and `a` by `exp(m-m_new)`, adds the tile's contributions, then normalizes at the end. State how masking and empty tiles are handled. [Triton fused attention](https://triton-lang.org/main/getting-started/tutorials/06-fused-attention.html)

For split-KV, partial maxima and sums must be combined under a common normalization. Simply averaging normalized partial outputs is wrong. Explain GQA's shared KV heads and why query-head mapping changes reuse. For quantization, include scales/zero points, grouping, residual storage, unpacking and quality tests. Tie each concept back to actual project evidence.

**Practice arithmetic [hypothetical inputs]:** dense KV bytes ≈ `2 × layers × batch × cached_tokens × kv_heads × head_dim × bytes_per_element`, before allocator/metadata/replication overhead. For 32 layers, batch 1, 8192 tokens, 8 KV heads, dimension 128 and BF16, this is 1 GiB. Explain how batching and quantization change it; do not use query-head count in place of KV-head count.

### F. Serving design and broader ML coverage

Review continuous/chunked batching, KV allocation, prefix caching, prefill/decode interference, admission control, backpressure, cancellation and tail latency. Know TTFT, TPOT, throughput and request success boundaries. Compare equal work under explicit latency/quality limits.

For speculative decoding, reason about useful accepted tokens versus drafting, verification and bookkeeping cost. Distribution-preserving verification requires the appropriate sampling algorithm; “the output always matches” is too broad. [vLLM speculative decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/)

AWS's public [P-EAGLE article](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/) is a concrete parallel-drafting example. Its [llm-d article](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/) illustrates separate prefill/decode pools and the associated transfer/routing considerations. These are relevant AWS examples; exact ownership by your prospective team is unverified.

Keep a smaller fundamentals block: transformer blocks, causal masking, training versus inference, sampling, perplexity/task evaluation, quantization quality, bias/variance and overfitting. Increase this allocation only if Sree confirms ML breadth.

## 6. Coding practice pack

Use Python for general practice unless the team specifies otherwise. Practice kernels in Triton and read relevant CUDA/C++; do not assume a Python-only interview. Suggested durations below are training budgets, not Amazon round lengths.

| ID | Exercise | Time | What a strong solution demonstrates |
|---|---|---:|---|
| C1 | Streaming latency accumulator with token-bearing events and trailers | 35 min | Explicit state, one-event/empty/error cases, consistent boundaries and tests; explain chunk/token distinction. |
| C2 | Request waiting-time state machine with repeated re-entry | 40 min | Idempotent closure, accumulated duration, invalid transitions, terminal/cancel handling and clock assumptions. |
| C3 | Stable row softmax: reference then Triton mapping | 45 min | Correct reductions/masks, numeric reasoning, strides and valid timing plan. |
| C4 | Residual-add + RMSNorm fusion sketch | 45 min | Formula, output contract, accumulation precision, memory traffic and resource tradeoff. |
| C5 | Merge split-attention partial statistics | 40 min | Correct max-rescaling and weighted combination; handles empty splits. |
| C6 | Kernel dispatch table with guards and fallback | 35 min | Compatibility keys, unsupported shapes, deterministic selection and invalidation. |
| C7 | Token-budget batch scheduler simulation | 45 min | Explicit budget/invariants, fairness, cancellation, starvation prevention and complexity. |
| C8 | Unfamiliar repository with failing tests | 50 min | Reproduce, trace failure, form hypothesis, small fix, targeted/regression tests and explanation. |

C1/C2 are deliberate variants of your known work, not a claim Amazon will reuse your PRs. Add unfamiliar cases so this tests transfer rather than memorization.

For conventional DSA, rotate hash maps, intervals, heaps, binary search, trees/graphs, monotonic stacks and basic DP. Use a 35-minute solve plus 10-minute review. The adjacent AWS report names [median from a data stream and shortest unsorted subarray](https://www.reddit.com/r/leetcode/comments/1vz16fx/aws_sdeii_overall_experience_oa_loop/); these are useful pattern exercises, not predictions for this role.

For an AI-assisted practice round, first locate the failing behavior yourself, then ask the permitted assistant for bounded hypotheses or code navigation. Inspect every change and run tests; be able to explain the patch without the assistant. Practice the same workflow unaided. In the real assessment, use only the tools explicitly permitted for that round.

## 7. Domain design and behavioral preparation

### Design mock D1: inference service under latency and cost constraints

**Prompt [inferred]:** design a service for an open-weight LLM with interactive and batch traffic, variable prompt lengths and a latency objective.

Use a 45-minute practice structure: 5 minutes requirements; 5 estimates; 10 architecture; 15 bottleneck/deep dive; 5 failure/rollout; 5 summary and tradeoffs. Clarify model, workload distribution, output limits, quality, tenant isolation, throughput and percentile SLOs before choosing optimizations.

Start with routing/admission → queue/scheduler → engine/model workers → KV management → streaming response. Separate control-plane deployment from request execution. Explain when to batch, scale, shard, quantize or disaggregate. Include memory headroom, cancellation, overload, fairness, worker failure, model-version consistency, warmup, canary evaluation and rollback. Measure completed useful work at acceptable latency, rather than maximizing raw tokens/s alone.

**Follow-ups:** What changes for long prompts? What if transfers dominate disaggregation? How do you avoid a noisy tenant consuming KV memory? Why could average throughput improve while p99 worsens? How do you compare versions with changing prompt/output distributions?

### Design mock D2: kernel specialization and release pipeline

**Prompt [inferred]:** build a system that selects, validates, packages and deploys precompiled kernels for recurring model workloads.

Cover representative workload capture, candidate generation/tuning, numeric reference tests, hardware/version matrix, reproducible results, artifact manifests, dispatch guards, fallback, service-level validation and rollback. Explain how you prevent an optimized artifact from silently running on an incompatible layout or target. This mock directly addresses the Director's new specialization signal.

### Behavioral evidence

Amazon explicitly emphasizes Leadership Principles. Use concrete personal actions and results; prepare alternative angles without repeating one story for every question. [Official principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles)

| Principle / practice prompt [inferred] | Candidate evidence | Gap to close |
|---|---|---|
| Dive Deep: investigated a misleading symptom | vLLM timing mismatch or SGLang negative queue time | Actual initial observation and investigation chronology. |
| Insist on Highest Standards: prevented regression | Deterministic clocks, lifecycle tests, contract preservation | Explain why tests detect the old failure and what they do not cover. |
| Ownership / Deliver Results: improved a slow process | Oracle test execution redesign | Keep result scoped to tests and approximate timing. |
| Learn and Be Curious: learned a difficult domain | TritonAttn and inference projects | One real failed approach, revised hypothesis and lesson. |
| Earn Trust / disagreement | Open-source review or genuine workplace decision | Need your actual exchange; do not invent conflict. |
| Customer Obsession / prioritization | Customer-scenario tests at Oracle; dependable measurement | Concrete user consequence, not an invented business metric. |
| Failure / reflection | Oracle guidelines and suite-growth lesson; kernel losing regimes | Identify an actual decision you would change. |

Build at least six distinct factual incidents before the loop. Some rows above are currently alternate angles on the same incident, not six finished stories. Practice a two-minute STAR answer followed by five minutes of challenges: what did **you** do, what alternatives, who disagreed, how measured, what failed, what would change?

## 8. Preparation schedule and readiness gates

### October 27: 100 minutes for tomorrow

- 15 min: introduction and why-team answer, twice aloud.
- 25 min: three 60-second stories—TritonAttn, vLLM, SGLang—with one limitation each.
- 15 min: professional timeline and transition; Oracle result with accurate scope.
- 15 min: actual authorization dates, location preference, start date and compensation questions.
- 20 min: mock recruiter conversation, including concise answers to gaps.
- 10 min: select recruiter questions; check invitation details and resume.

If only 30 minutes remain: 10 pitch, 10 project stories, 10 logistics/questions. Tomorrow does not require cramming a GPU textbook.

### October 28 morning

Finish substantive study by about 9:00–9:30 ET. At 10:15, skim the brief, check call details and settle in. Be ready at 10:25. Record answers and next steps immediately afterward.

### Provisional 14-day technical plan

Assumption: approximately three focused hours a day after the recruiter call. This is a study proposal, not a scheduled automation or a known interview date. Adjust once Sree supplies timing. Default allocation: 60 min domain implementation, 45 min general coding, 45 min design/profiling, 30 min evidence/behavioral practice.

| Day | Main deliverable |
|---|---|
| 1 — Oct 28 | Recruiter debrief; confirm format; baseline one coding task and one technical explanation. |
| 2 — Oct 29 | A real project profile explained from timeline to kernel; two competing bottleneck hypotheses. |
| 3 — Oct 30 | Softmax reference and kernel reasoning; correctness/edge-case checklist. |
| 4 — Oct 31 | Fusion exercise and memory-traffic comparison; one reason not to fuse. |
| 5 — Nov 1 | Tiling/warps/stages experiment plan and a winning/losing shape explanation. |
| 6 — Nov 2 | AOT/JIT/cache distinctions; guarded variant-dispatch design. |
| 7 — Nov 3 | First technical-screen mock; record concrete misses. |
| 8 — Nov 4 | Online softmax and split-KV merge derivation from memory. |
| 9 — Nov 5 | Serving metrics, KV budgeting, batching and overload; C1/C2 variant. |
| 10 — Nov 6 | D1 inference-system design mock. |
| 11 — Nov 7 | D2 kernel-release design; speculative/disaggregated tradeoffs. |
| 12 — Nov 8 | Repository debugging plus general DSA; permitted AI variant if confirmed. |
| 13 — Nov 9 | Simulated loop blocks with technical and LP follow-ups. |
| 14 — Nov 10 | Repair only observed gaps; final evidence cards and rest. |

US daylight saving time changes during this plan; any later scheduled call should retain its named timezone. No exact later interview time is assumed here.

**If only seven days:** combine days 2/3, 4/5, 6/8 and 9/11; retain both design mocks and a timed coding mock. **If only 72 hours:** prioritize exact resume defense, one profiling case, softmax/fusion/dispatch reasoning, two DSA solves, one inference design and four factual LP stories. Ask for a preparation interval if necessary, stating your actual availability.

**Practice scorecard [our rubric, not Amazon's]:** score each dimension 0 (cannot explain), 1 (needs major prompting), 2 (independent with minor gaps), 3 (clear and robust). Dimensions: correctness; problem framing; implementation; measurement; tradeoffs; communication. A drill is ready when every dimension reaches 2 on an unseen variant, with no unsupported personal claims. Repeat a failed drill after review and again after a delay; do not count reading as readiness.

## 9. Next actions and open questions

- [ ] Confirm tomorrow's invitation/connection details.
- [ ] Rehearse the recruiter brief aloud.
- [ ] Capture Sree's exact round format, languages, allowed tools, dates and internal level.
- [ ] Build factual incident cards; recover genuine discovery/decision history for kernel and PR work.
- [ ] Retrieve original benchmark artifacts before quoting detailed performance figures.
- [ ] Start baseline timed practice after recruiter clarification.

The interview outcome remains an ongoing goal. This guide completes the initial research/preparation deliverable; it does not imply interview readiness has already been demonstrated or interviews scheduled.

---

## Historical preparation retained below

The following October 26–27 material is preserved for its evidence and source links. Its scheduling instructions and earlier stage assumptions are historical; the update above governs the October 28 recruiter call and subsequent preparation.

# Interview Intel: Amazon AWS — Machine learning engineer II, Inference Optimization

**URL:** https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization
**Requisition:** 10587705
**Legitimacy:** unknown formal evaluation tier; live title, full JD and Apply now verified at Amazon.jobs on October 26, 2026. Recruiter conversation supplied directly by Suraj; email headers were not independently inspected.
**Report:** N/A — standalone CV and interview preparation, no application submission or tracker status change.
**Researched:** 2026-10-26
**Sources:** 0 Glassdoor reviews, 0 Blind posts, public primary sources listed below and in the October 27 revision plan, current primary CV/profile, and the user-pasted recruiter thread. No team-specific interview reports established.
**Audiences covered:** recruiter-screen; hiring-manager and peer-tech follow-up preparation clearly labeled as inferred. No panel or later-round format confirmed.
**Candidate email:** sm12377@nyu.edu
**Revision notes:** [Lecture/book concepts, likely questions and project connections](amazon-10587705-inference-revision-notes.md) — added October 27, 2026.
**Project/PR audit:** [Highlights, final patches, review decisions and deep-dive order](amazon-10587705-project-pr-review.md) — October 27; includes later SGLang coverage caveat and separation of INT2 compression from INT4 quality results.
**Resume:** [Tailored PDF](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.pdf)
**JD archive:** [Captured posting](supporting/aws-inference-optimization-10587705-2026-10-26.md)

## Historical October 26 preparation for the October 27 informational call

Sadaf Fardeen offered a **30-minute informational phone chat**, then sent this requisition and asked you to apply. That is the confirmed format from your thread. Coding, a formal technical screen, internal level, remaining rounds, and hiring timeline are not confirmed. Prepare for fit and logistics, with a short technical explanation ready if she probes. Amazon's general guide describes initial screens as potentially covering qualifications, technical validation, behavior and compensation; it does not establish this team's agenda. [Amazon interview guide](https://www.aboutamazon.com/news/workplace/amazon-interview-guide)

**Time: Tuesday, October 27, 2026.** She wrote “2 PM PST.” On that date Los Angeles observes PDT, so **2 PM local Pacific = 5 PM New York EDT**. Literal PST would instead mean 6 PM EDT. This conversion was checked with Python's `zoneinfo` for America/Los_Angeles and America/New_York; her intended timezone needs confirmation.

Suggested manual confirmation:

> Hi Sadaf, thank you for sharing the opening. Just confirming our call tomorrow, Tuesday October 27, is at 2 PM Pacific / 5 PM Eastern. I look forward to speaking with you.

Phone provided in the thread: **+1 551-371-2172**. Keep it available, allow unknown callers, and have the job page, new PDF and your notes open. No meeting invite or calendar event was inspected or created.

## Your objective and best positioning

**Get Sadaf comfortable presenting you to the hiring manager as a software engineer with relevant GPU-inference evidence.** The differentiator is the combination of attention/KV-cache kernels, upstream measurement correctness, and professional software engineering. Avoid presenting yourself as someone with four years of professional GPU/MLE experience: the professional work was backend engineering, test infrastructure and automation; GPU/LLM work is recent project and open-source experience. [Primary source: current cv.md and profile]

The team explicitly needs vLLM/SGLang development, CUDA tuning, model servers, benchmarking and price-performance improvements for Qwen/Gemma/gpt-oss across SageMaker, Bedrock and HyperPod. Your kernel project and upstream contributions make this a credible conversation. They do not establish prior employment on those AWS products. [Exact JD](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization)

### 60–90-second introduction

> I'm a software engineer with nearly four years of professional experience at Oracle and Incture, and I completed my master's at NYU this May. My recent work has focused on GPU performance and LLM inference.
>
> I built Triton attention and KV-cache kernels covering prefill, split-KV decoding and quantization, with 210 tests passing on H100. The prefill kernel reached 433 TFLOP/s BF16 and 1.1–1.3 times PyTorch SDPA at long sequence lengths. I used Nsight Compute to investigate register-pressure and occupancy bottlenecks and checked integration through token-identical greedy generation.
>
> I've also contributed merged fixes to vLLM and SGLang, particularly around reliable inference latency and scheduler queue-time measurement. My earlier work gives me a foundation in backend performance, automation and testing. This role interests me because it connects the kernel and serving-stack work I've been doing to customer-facing inference performance at AWS.

All personal claims above trace to the current master CV. Practice the introduction aloud; leave a pause after each paragraph. Do not read every test count in the first answer.

### Why this role / why AWS? [inferred from JD]

> The work spans the layers I most want to work on: kernels, inference engines, and the measurement that tells us whether a change actually improves serving. I've worked on those layers through TritonAttn, vLLM, SGLang and my LLM control-plane project. I'm especially interested in taking that work into production, where an optimization has to improve price-performance while preserving correctness and latency expectations.

Optional research detail, after reading the articles: AWS has published work on parallel speculative drafting integrated into vLLM, and Kubernetes-based disaggregated inference with llm-d. Those are concrete examples of the JD's direction, **not proof that Sadaf's exact team authored or owns them**. [AWS P-EAGLE](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/), [AWS llm-d](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/)

## Requirements: what you can defend and what needs care

This is a manual evidence review. CareerOps' automated skill extractor found the requirements section but returned **no skill candidates**; empty results do not mean there are no gaps.

| Requirement / work area | Evidence in current CV | Assessment and discussion boundary |
|---|---|---|
| 3+ years professional software development | Incture Sept 2020–Dec 2021; Oracle Jan 2022–Aug 2024 | Strong duration evidence, nearly four years. Describe the actual development work. |
| 2+ years non-internship system design/architecture | Stateless services at Incture; JUnit execution/lifecycle redesign and suite distribution at Oracle | Relevant design evidence; **two years of qualifying design scope is not documented**. Reconstruct dates and decisions honestly; do not equate all tenure with architecture. |
| 1+ year SDE/related occupation | Professional roles above | Strong. |
| 1+ year developing applicable software in C#/C++/Java/Perl | Java/Spring Boot professional backend work; Java test infrastructure | Java is your clearest professional-language evidence. Do not turn C++ in Skills into a claim of years of professional CUDA/C++ work. |
| Bachelor's in relevant discipline | NIT Bhopal B.Tech Computer Science and Engineering | Strong. NYU master's adds ML coursework. |
| ML/transformer/training-inference fundamentals | TritonAttn, GRPO/PEFT work, transformer training, NYU coursework | Strong project evidence; explain attention and inference simply. |
| 3+ years full SDLC preferred | Backend delivery, Jenkins/Ansible, test infrastructure, TeamCity; recent upstream review/testing | Relevant breadth; be prepared to explain your own review, build and operational duties. Exact duration of every SDLC component is not separately established. |
| GPU kernels and profiling | Triton attention/KV kernels; H100 tests; Nsight Compute | Strong project evidence. No established years of production kernel ownership. |
| vLLM / SGLang development | Three merged vLLM PRs and one merged SGLang PR | Strong upstream evidence in metrics, observability and regression testing. **These PRs are not kernel implementations.** |
| Speculative decoding | No implemented speculative decoder established in CV | Implementation gap. Learn the mechanism and evaluation tradeoffs; say so directly. |
| Disaggregated inference | SGLang lifecycle tests cover unified and disaggregated modes | Relevant adjacent exposure, **not ownership of a disaggregated serving system**. |
| SageMaker / Bedrock / HyperPod | General cloud/inference/Kubernetes skills | Product-specific production gap. Do not add these to experience as accomplished work. |

## Prepare three evidence stories

### October 26 rehearsal cards: short answer first, depth on request

These are proposed spoken explanations grounded in the current CV. They do not establish additional implementation details or production experience. Likely questions remain inferred from the JD and recruiter context.

**Kernel work — approximately 45 seconds**

> I built attention and KV-cache kernels in Triton for both prompt processing and token generation. The engineering problem was how to map that work onto the GPU efficiently while preserving correctness. I worked on FlashAttention-style prefill, split-KV decoding and cache quantization, and used Nsight Compute to investigate register-pressure and occupancy limits. The library passed 210 tests on H100. In long-sequence prefill cases, my kernel was 1.1–1.3 times PyTorch SDPA. I also integrated the kernels with Hugging Face Transformers and checked token-identical greedy outputs.

If asked what is technically interesting, explain one tradeoff at a time:

- **Prefill:** avoid materializing the full attention-score matrix in GPU global memory; process tiles with online softmax. Better work partitioning and GPU data reuse are central ideas in FlashAttention-2. This is conceptual background; identify your own code choices separately. [FlashAttention-2 paper](https://arxiv.org/abs/2307.08691)
- **Decode:** splitting the KV sequence exposes additional parallelism, but requires combining partial outputs with consistent softmax normalization. Explain when extra parallelism outweighs reduction overhead using your actual data. [CV's split-KV work; inferred technical follow-up]
- **Quantization:** cache compression trades memory savings against unpacking/dequantization cost and numerical change. Your established results are 5.2× KV compression and +0.33% INT4 perplexity; retrieve the exact evaluation setup and percentage interpretation before quoting the latter in detail. [Current CV]
- **Profiling:** register pressure can constrain resident work. Increasing occupancy is not automatically faster; reduced registers can introduce spills, and other resources can become limiting. Present the profile and measured latency for a change you actually made rather than inventing a before/after optimization. [NVIDIA CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy)

**vLLM #55508 — approximately 45 seconds**

> I corrected inconsistent latency accounting in vLLM's streaming benchmark clients. Different endpoints were measuring slightly different windows: the first-token timestamp wasn't consistently reused, and tokenless usage trailers could extend the reported end time. I aligned those boundaries and added deterministic tests checking that end-to-end latency minus time to first token equals the sum of inter-token intervals. The value is comparable, regression-tested measurements across endpoints, which makes optimization decisions more trustworthy.

The PR and diff confirm two mechanisms: an additional clock read for TTFT creates an offset relative to the inter-arrival chain; a trailing usage chunk moves the endpoint without adding a corresponding token interval. These are benchmark-client changes, not a faster attention implementation. The review discussion asks whether the tests fail without the patch; be ready to explain how you checked regression sensitivity. [vLLM PR](https://github.com/vllm-project/vllm/pull/55508)

Useful definitions: TTFT is measured start to first accepted token-bearing chunk; the corrected endpoint is the last such chunk for this benchmark metric. TPOT is `(E2E - TTFT)/(output_tokens - 1)` when more than one output token exists. Streaming chunks can contain more than one token; this fix does not establish perfect per-token arrival timestamps. Distinguish this measured token-delivery window from HTTP connection closure. [Same PR]

**SGLang #39312 — approximately 45 seconds**

> I fixed a request-lifecycle accounting bug in SGLang. A request could start running, be retracted or preempted, and return to the waiting queue. The accounting mixed the original execution timestamp with the newer queue-entry timestamp, producing a negative queue time. I changed the accounting to accumulate each waiting interval and made closing an interval idempotent, so repeated callbacks didn't count the wait twice. I preserved scheduling decisions and the existing Prometheus histogram behavior, then validated the lifecycle changes with regression and randomized tests.

Teaching example, **invented timestamps, not an experimental result**: queue entry at t=1, first execution at t=3, re-entry at t=8, resume at t=10. `3 - 8` gives an impossible -5; actual total waiting is `(3 - 1) + (10 - 8) = 4`. The separate Prometheus histogram intentionally keeps its original first-wait semantics. Do not claim every exposed metric was changed to total accumulated waiting. [SGLang PR](https://github.com/sgl-project/sglang/pull/39312)

**Verification boundary discovered in PR review:** SGLang's disaggregated paths were covered by unit/randomized lifecycle validation, not a complete end-to-end PD deployment. Its description also notes two pre-existing macOS-related failures in the broader test run; say “validated 303 related tests,” not “303 tests all passed.” These are source-audit caveats, not new CV accomplishments. [Same PR]

**Depth questions to rehearse [inferred from JD]**

1. Why do your prefill and decode kernels need different parallelization strategies?
2. When does split-KV lose despite higher parallelism?
3. Which profile showed register pressure, and what code/configuration change did you actually test?
4. Was your SDPA comparison using its optimized backend with matching inputs and dtype?
5. How were warmup, compilation, asynchronous GPU execution and timing boundaries handled?
6. Which tests establish numerical correctness, and what does token-identical greedy output not prove?
7. Why is an explicit first-chunk flag safer than inferring state from a timestamp value?
8. Why must a queue-wait close be idempotent during chunked prefill?
9. Why preserve scheduler timestamps and histogram semantics instead of simply suppressing negative values?
10. How would you demonstrate service-level price-performance benefit beyond a faster microkernel?

Do not memorize an answer for an unknown benchmark parameter. Retrieve the artifact, or state what you need to verify.

### 1. H100 kernel work: the lead technical story

**Headline:** “I built attention and KV-cache kernels, profiled the limiting resources, and validated correctness against references and model outputs.”

**Effect:** faster attention in the measured workload regimes and reduced KV-cache footprint. The project does not establish a customer deployment or measured dollar savings.

**Rationale/mechanism to explain:** online softmax avoids materializing the whole attention matrix; tiling and data reuse matter; split-KV decoding exposes parallelism but adds partial-result reduction work; quantization saves memory while adding unpacking/dequantization work. These are conceptual explanations to review, not additional claims about undocumented experiments.

**Your established actions/results:** FA2 prefill 433 TFLOP/s BF16, 1.1–1.3× SDPA at long sequences; split-KV peak 1.29× SDPA in target GQA regimes; up to 13.6× against **naive decode**, a different baseline; 5.2× cache compression; +0.33% INT4 perplexity; 210 H100 tests; Nsight diagnosis and token-identical greedy integration. [Current cv.md, TritonAttn]

**The most important homework:** recover the benchmark configuration from your own artifacts before the call. The master CV does not record all of it, so this brief does not invent it.

| Item | Have ready / verify from artifacts |
|---|---|
| Shape | Batch, query/KV heads, head dimension, input/KV length for the headline result |
| Hardware | Exact H100 variant and GPU count; only H100 sm_90 is established here |
| Software | PyTorch, Triton, CUDA versions; SDPA backend selection |
| Measurement | Warmup, compilation exclusion, event timing/synchronization, repetitions, summary statistic |
| Comparison | Same dtype, causal mask, shape, inputs and timing boundary for both implementations |
| Limits | A case where you did not beat SDPA, what resource limited it, and what you tried |
| Correctness | Reference, tolerances, mask/shape coverage, and scope of token-identical integration checks |
| Quantization | Which model/data produced the perplexity result; relative versus absolute interpretation of +0.33% |

Do not give an invented answer if a detail is unavailable: “I can share the exact configuration after checking my benchmark artifact.” Distinguish kernel throughput from end-to-end model tokens/sec.

### 2. vLLM and SGLang: make trustworthy measurement the story

**Headline:** “An inference optimization is only useful if the latency accounting is correct.”

For [vLLM #55508](https://github.com/vllm-project/vllm/pull/55508), explain the first-token timestamp, tokenless usage trailers, and the invariant **E2E − TTFT = sum of inter-token intervals** for the measured decode window. You added 12 new tests and validated 8 siblings. This was measurement correctness; do not claim it made the model intrinsically generate faster.

For [SGLang #39312](https://github.com/sgl-project/sglang/pull/39312), explain how retraction/preemption creates multiple waiting intervals. You accumulated those waits, handled idempotent closure/chunked prefill and process-clock rebasing, and preserved scheduling behavior and the histogram contract. Evidence: six new tests, 303 related tests, 20,000 randomized lifecycles and 9,504 non-retracted compatibility cases. **No scheduling-policy change.**

Keep [vLLM #62205](https://github.com/vllm-project/vllm/pull/62205) as the serving-debuggability example: correlated delta/full/final output logging, 53 focused and 281 broader tests. [#62204](https://github.com/vllm-project/vllm/pull/62204) documents/tests existing retry byte-budget behavior; it is not a claim of inventing a security mechanism. [Current cv.md, open-source projects]

Prepare one genuine maintainer-review decision from memory or the PR, including the change you made and why. No specific disagreement or review incident has been established in this brief.

### 3. Oracle: professional ownership and a real tradeoff

**Headline:** “I redesigned test execution and object lifecycles, reducing execution of the then-existing full pipeline from approximately 10–11 hours to within three hours.”

Explain shared setup for dependent interface objects, verification versus state-mutating tests, parallel/sequential grouping in JUnit 5, and suite distribution with TeamCity. Saved time enabled more testing. This is **test execution improvement**, not production database throughput; unchanged compute cost/hardware is not established. [Current cv.md; story bank O1]

Useful challenge/reflection: interleaved logs became harder to investigate, so you researched attribution-capable Java logging and wrote a class-based log organization script. The work took roughly five to six months while tests grew. You would establish authoring guidelines earlier and account for growing compute needs. [Current profile and story bank O1/O2]

Backup automation example: you adapted existing Terraform scripts and personally wrote readiness, artifact-collection and cleanup scripts. Cleanup ran despite earlier failures. Discuss the tradeoff honestly: deleting an instance after artifact-copy failure can lose local diagnostics; guaranteed artifact preservation, successful deletion under every failure, and a retry/fallback mechanism are not established. [Current profile; story bank O3]

## Likely recruiter prompts and concise answers

All prompts below are **[inferred from JD / recruiter context]**, not reported questions from this team.

**“How much professional ML/GPU experience do you have?”**

> My nearly four years of professional experience are in backend engineering, infrastructure automation and test systems. My GPU/LLM experience comes from recent hands-on projects and merged contributions, particularly H100 attention/KV-cache kernels and vLLM/SGLang. I'm targeting the mid-level role where that software-engineering foundation and recent specialization are relevant.

**“Have you used speculative decoding or built a disaggregated engine?”**

> I haven't established an implemented speculative-decoding project in my work. My strongest hands-on areas are attention, split-KV decode, quantization, profiling, and serving metrics. My SGLang lifecycle validation covered disaggregated modes, but I didn't build the disaggregation architecture. Those are areas I want to deepen in this role.

**“Have you shipped on SageMaker, Bedrock or HyperPod?”**

> I haven't owned production deployments on those specific products. My adjacent experience is cloud automation, Kubernetes-based LLM serving and inference-stack contributions. I'd be interested in how much the role focuses on engine and kernel development versus AWS service integration.

**“Do you meet the architecture requirement?”**

> My professional design work includes stateless Spring Boot services at Incture and test-execution/lifecycle redesign at Oracle. I can walk through the decisions I personally made in each. I'd like to understand the scope of architecture ownership the team expects for this opening.

Do not claim a precise two-year design duration without reconstructing it. If asked for a numeric duration, answer from actual project dates, not total employment duration.

**“Why leave Oracle / what have you done since?”**

> I went to NYU for my master's to move deeper into ML. Since then I've built hands-on evidence around inference kernels, serving infrastructure and open-source contributions. The progression is from reliable software systems toward ML inference performance.

The master's finished May 2026; describe the post-graduation projects accurately. Do not label them salaried employment unless they were.

**“Compensation expectations?”**

The exact posting lists **$165,200–$223,600 annual base in Santa Clara**, plus sign-on and RSUs. [Exact job](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization)

> I saw the published base range. I'm comfortable continuing the conversation within that framework, depending on level, responsibilities and the overall package. Could you share the expected total-compensation structure for this requisition?

Use that script only if it matches your actual preferences; your saved target/minimum are blank. For context, Levels.fyi's US Amazon MLE page displays about $287k L5 total compensation, updated October 12, 2026. It is self-reported, not Santa Clara/req-specific; sample size and exact role mapping are not established. Do not adopt it as your target or infer this req's internal level from it. [Levels.fyi](https://www.levels.fyi/companies/amazon/salaries/machine-learning-engineer)

**Location, work authorization, start date, other processes:**

- Role location is Santa Clara; no remote/onsite schedule was confirmed. Have a truthful relocation answer and a realistic earliest start date ready.
- Saved profile says F-1; exact current OPT/STEM OPT/EAD dates are not established here. Bring the actual dates and answer current authorization and future sponsorship separately. Ask whether the req supports your situation; do not infer eligibility from general company practice.
- Give only real deadlines or competing processes. Your historical “90-day clock” is not a verified current deadline and should not be reused automatically.
- Do not invent a notice period, offer deadline, or immediate start commitment.

## Five useful questions for Sadaf

Suggested questions **[inferred from JD / recruiter context]**; pick three or four if time is short.

1. “How is this MLE II opening leveled internally, and what distinguishes a strong mid-level candidate from the senior profile in your post?”
2. “What is the balance between hands-on kernels, vLLM/SGLang engine development, and AWS service integration? Which is the biggest immediate need?”
3. “Would my kernel projects plus merged inference-stack work be relevant to the manager's current priorities? Where would they want stronger evidence?”
4. “What would the next stages assess: general coding, CUDA/Triton, C++/Python, inference/system design, and Leadership Principles? Is there an assessment before a technical conversation?”
5. “Could we confirm the Santa Clara work arrangement, work-authorization/sponsorship eligibility and expected hiring timeline? If the fit looks promising, what should I send for the manager review?”

Optional technically specific question if she knows the team: “AWS has published work on P-EAGLE and llm-d. Does this team focus on related problems, or a different part of the serving stack?” Do not ask her to disclose confidential details. [AWS P-EAGLE](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/), [AWS llm-d](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/)

Closing line:

> Based on what we've discussed, do you see a fit worth taking to the hiring manager? Is there anything in my background you'd want me to clarify before that review?

## Technical refresher: enough for tomorrow, deeper for a later round

All exercise prompts are **[inferred from JD]**. These are preparation topics, not a claim that tomorrow includes coding.

### Speculative decoding

A drafter proposes several tokens; the target verifies them. Standard exact speculative sampling uses acceptance/rejection and correction to preserve the target distribution in theory; greedy equality and numerical behavior need validation. Gains depend on accepted tokens per target pass versus drafting, verification and bookkeeping overhead. It can lose when acceptance is low or the baseline is already well utilized. vLLM distinguishes standard rejection-sampling guarantees from relaxed-verification variants. [vLLM documentation](https://docs.vllm.ai/en/latest/features/speculative_decoding/)

AWS's P-EAGLE article describes generating multiple draft tokens in one pass, rather than a serial drafter forward pass per token, plus fused Triton work for draft-batch preparation. Read for the principle and tradeoffs; do not memorize its headline speedup as if workload-independent. [AWS P-EAGLE](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/)

**Practice:** “When could speculative decoding make serving slower, and how would you isolate why?”

### Disaggregated prefill/decode

Separate prompt processing and token generation so they can be provisioned and scaled independently. Review the different resource profiles, KV-cache transfer overhead, queue imbalance and routing/cache locality. AWS's llm-d example connects vLLM, Kubernetes, NIXL and EFA/libfabric; do not treat NCCL collectives and point-to-point KV transfers as interchangeable abstractions. Whether this team's implementation uses that stack is unknown. [AWS llm-d](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/)

**Practice:** “When does separating prefill and decode help, and when could transfer or coordination costs outweigh the benefit?”

### Kernels, measurement and product impact

- Explain online softmax, tiling and shared/register/global memory tradeoffs using your actual attention implementation. [CV; inferred follow-up]
- Explain split-KV's extra parallel work and reduction overhead. Show a winning and a losing regime from your real measurements. [CV; inferred follow-up]
- Explain why lowering register pressure or raising occupancy is not automatically a performance win: measure the effect on spills, memory traffic, work per block and kernel duration. [Inferred technical exercise from profiling requirement]
- Walk from request arrival through queueing, prefill, first token, decode, finish and tokenless trailers; define the timing boundaries you corrected. [vLLM CV evidence]
- Propose a benchmark matrix across model, prompt/output length, concurrency, dtype, backend and latency targets. Keep warmup/compilation separate and compare equivalent work. This is a proposed method, not a claim about undocumented past runs. [Inferred from JD]
- Translate kernel speed into useful completed requests/tokens per dollar under TTFT/TPOT/tail-latency and quality constraints. A faster microkernel can fail to improve the whole service. [Inferred from JD's price-performance ownership]
- Refresh transformer inference versus training, KV-cache scaling, GQA/MQA and the memory/accuracy tradeoff of cache quantization. Have GRPO/LoRA available as secondary evidence of training fundamentals, not the lead story. [CV; inferred from JD]

## Behavioral story routing

Amazon recommends specific personal actions, results and structured STAR answers; the public SDE II page also describes coding, design and Leadership Principles. It is **adjacent guidance**, not proof that this MLE role uses the SDE II loop. [Amazon interview guide](https://www.aboutamazon.com/news/workplace/amazon-interview-guide), [SDE II prep](https://amazon.jobs/content/en/how-we-hire/sde-ii-interview-prep)

| Audience / likely topic [inferred] | Best supported material | Fit / gap |
|---|---|---|
| Recruiter: strongest relevant achievement | TritonAttn plus one merged PR headline | Strong; keep it under two minutes. |
| Recruiter: professional ownership | Story bank O1, parallel test execution | Strong; use corrected metric and scope. |
| Manager: quality and measurement | vLLM timing invariant; SGLang lifecycle accounting | Strong project evidence; no customer impact metric established. |
| Manager: mistake and learning | O1's delayed authoring guidelines / underestimated suite growth | Supported reflection; do not invent an outage. |
| Peer: diagnosis and correctness | Triton profiling and reference/model checks | Strong; benchmark configuration needs retrieval. |
| Peer: debugging concurrency consequences | O2, attribution/log organization within O1 | Supporting story; not a separate large project. |
| Manager: disagreement / influencing others | No detailed conflict example established in current sources | Gap. Retrieve one real review or workplace decision; do not fabricate it. |
| Peer: production GPU incident or multi-node deployment ownership | No complete incident story established | Gap. State project versus production boundary. |

The provenance checker ran, but its automated pass does not override the October 23–26 Oracle reset. The numerical coverage claims it recognizes are uncertain in current primary notes and were not used. Old production-throughput, fleet retry-budget and petabyte-architecture ownership narratives were excluded.

## Tonight: a focused two-hour plan

This is a suggested study sequence, not a scheduled task.

1. **15 min:** Practice the introduction and “why this role” aloud twice. Aim for clarity before adding numbers.
2. **35 min:** Recover the H100 benchmark configuration, one profile and one honest limitation. Be able to explain what the measured speedup does and does not establish.
3. **20 min:** Review vLLM #55508 and SGLang #39312: failure, personal change, invariant, tests and scope boundary. Have the other two vLLM PRs ready as backups.
4. **20 min:** Review speculative decoding and disaggregated inference from the linked primary sources. Practice the two “when does it lose?” questions.
5. **20 min:** Rehearse Oracle O1 and one genuine challenge using personal actions and the corrected test-runtime metric.
6. **10 min:** Confirm timezone, phone, relocation, exact work-authorization dates, start date and your three best questions. Apply with the new resume if you choose to proceed, and retain the application confirmation.

**If you have only 45 minutes:** 10 minutes pitch, 15 minutes benchmark evidence, 10 minutes one PR, 10 minutes logistics/questions. The informational call does not justify substituting hours of unrelated algorithm practice for these basics.

## After you apply / after the call

Only use the following once the application is actually submitted:

> Hi Sadaf, I've applied for Machine Learning Engineer II, AWS Inference Optimization, requisition 10587705, using sm12377@nyu.edu. I've attached an updated resume with more detail on my H100 attention/KV-cache kernels and merged vLLM/SGLang contributions. Thank you for sharing the opportunity; I look forward to our conversation.

After the call, record the confirmed level, team scope, format of next round, timeline, location and authorization guidance here. If the next round is technical, build a separate practice session from what Sadaf confirms rather than assuming a generic Amazon loop.

## Public sources and limits

### Revision resources — October 27, 2026

Recommended order is tailored to this inference-optimization role, not a claim about confirmed interview questions. The video links below are the **Spring 2025 Stanford Online offering**; the main Stanford course site now describes Spring 2026. Keep editions consistent. [Official 2025 schedule](https://cs336.stanford.edu/spring2025/)

1. [Lecture 10: Inference](https://www.youtube.com/watch?v=fcgPYo3OtV0) — first revision priority: connect prefill/decode, KV cache, batching and inference optimizations to the team's serving goals.
2. [Lecture 6: Kernels, Triton](https://www.youtube.com/watch?v=E8Mju53VB00) — benchmark/profiling discipline and kernel implementation; connect each concept to actual TritonAttn code and artifacts.
3. [Lecture 5: GPUs](https://www.youtube.com/watch?v=6OBtO9niT00) — refresh memory hierarchy, compute/data-movement bottlenecks and GPU execution concepts.
4. [Lecture 2: PyTorch, Resource Accounting](https://www.youtube.com/watch?v=msHyYioAyNE) — refresh FLOPs/memory accounting; prioritize the parts needed to defend measured performance.
5. Later technical preparation: [Lecture 7: Parallelism 1](https://www.youtube.com/watch?v=l1RJcDjzK8M) and [Lecture 8: Parallelism 2](https://www.youtube.com/watch?v=LHpr5ytssLo). Connect parallelism and communication costs to multi-GPU reasoning; distinguish training parallelism from serving design.

Baseten's book is **Inference Engineering by Philip Kiely**. Use its current official online section names, not guessed PDF page numbers:

- [Chapter 1](https://www.baseten.co/inference-engineering/book/01-prerequisites/): **1.4 Measuring Latency and Throughput** first; skim 1.2 About Your App for workload requirements.
- [Chapter 2](https://www.baseten.co/inference-engineering/book/02-models/): **2.2 LLM Inference Mechanics; 2.4 Calculating Inference Bottlenecks; 2.5 Optimizing Attention**.
- [Chapter 3](https://www.baseten.co/inference-engineering/book/03-hardware/): **3.1 GPU Architecture**, then 3.3 Instances. Review Hopper-specific material in 3.2 selectively.
- [Chapter 4](https://www.baseten.co/inference-engineering/book/04-software/): **4.1 CUDA; 4.3 Inference Engines; 4.5 Performance Benchmarking and Load Testing**. Add 4.4 NVIDIA Dynamo for distributed-serving context.
- [Chapter 5](https://www.baseten.co/inference-engineering/book/05-techniques/): read all five subsections before a deeper technical interview. Prioritize **5.2 Speculative Decoding and 5.5 Disaggregation** for knowledge gaps; use **5.1 Quantization, 5.3 Caching and 5.4 Model Parallelism** to connect your existing work to serving tradeoffs.
- [Chapter 7](https://www.baseten.co/inference-engineering/book/07-production/): **7.2 Autoscaling; 7.4 Testing and Deployment; 7.5 Client Code**, connecting to LLMCP and streaming benchmark work. Lower immediate priority than chapters 2–5.

For today's informational call, a suggested **two-hour selective revision budget**, not video runtimes or timestamps: 20 min on 1.4/4.5; 30 min on selected Lecture 10 concepts; 25 min on selected Lecture 6 concepts; 25 min on 5.2/5.5; 20 min explaining your actual benchmark and PRs aloud. A complete viewing of all recommended lectures takes substantially longer. Save a full course pass for later rounds.

Finish with five spoken checks: explain a prefill/decode bottleneck; explain one actual kernel tradeoff; defend a fair SDPA comparison; derive the vLLM timing invariant; explain SGLang repeated waiting intervals and idempotent closure. New reading does not become past implementation experience.

1. [Exact Amazon requisition 10587705](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization) — live page read October 26; role, qualifications, location and base pay. Posting date absent.
2. [Amazon interview guide](https://www.aboutamazon.com/news/workplace/amazon-interview-guide) — general screening and behavioral guidance; not team-specific.
3. [Amazon SDE II prep](https://amazon.jobs/content/en/how-we-hire/sde-ii-interview-prep) — adjacent technical/behavioral preparation only. Do not transplant its exact stage count/timings to MLE.
4. [AWS llm-d disaggregated inference](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/) — March 16, 2026; architectural concepts and a public AWS implementation example.
5. [AWS P-EAGLE](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/) — March 13, 2026; parallel drafting and vLLM integration example.
6. [vLLM speculative decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/) — current documentation read October 26; mechanism and correctness caveats.
7. [Levels.fyi Amazon MLE](https://www.levels.fyi/companies/amazon/salaries/machine-learning-engineer) — US, self-reported; page says updated October 12, 2026; sample/req mapping unknown, contextual only.
8. [FlashAttention-2 paper](https://arxiv.org/abs/2307.08691) — original work-partitioning and memory-efficiency explanation; read October 26 for technical coaching.
9. [NVIDIA CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy) — resource/occupancy tradeoffs and reference-based correctness checks; read October 26.
10. [vLLM #55508](https://github.com/vllm-project/vllm/pull/55508) — merged metadata, description, patch and discussion fetched through the connected GitHub tool October 26; technical mechanism verified. No new personal performance numbers imported into the CV.
11. [SGLang #39312](https://github.com/sgl-project/sglang/pull/39312) — merged page, mechanism, histogram contract and test-coverage limitations read October 26. No new personal accomplishments imported into the CV.

Candidate facts: current `cv.md`, `modes/_profile.md`, `config/profile.yml`; story-bank structure only where consistent with those primaries. Optional article-digest file absent. No interview success probability, exact team headcount, hiring urgency, unpublished process or future sponsorship outcome was inferred as fact.
