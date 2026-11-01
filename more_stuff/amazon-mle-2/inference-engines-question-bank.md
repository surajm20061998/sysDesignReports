# Inference engines — vLLM and SGLang interview focus

**Research date: October 28, 2026.** Supplement to the [cross-company domain bank](ml-inference-engineering-question-bank.md) for the November 12 Amazon MLE II interview. **32 targeted questions/exercises**: six vLLM, six SGLang, four optimization, six coding, six cases and four project defenses. These extend engine-specific follow-ups; existing general attention, quantization and design questions remain in the main bank.

All 32 prompts below are **original practice**, including prompts inspired by a candidate account or the user's own contributions. They are not claimed verbatim reported interview questions. Priority indicates training value, not frequency. [Research evidence and reading list](inference-engines-research.md) distinguishes public reports from technical sources. No complete exact-team vLLM/SGLang question set was found.

## Highest priority for November 12

Be able to trace a request, explain prefill/decode and metrics, calculate KV memory, distinguish paging from prefix reuse, reason through batching/cache pressure, and defend your actual vLLM/SGLang contributions. Kernel/profiling reasoning remains central given the Director's stated focus. Engine flags/defaults and source class names are version-dependent. Start with mechanisms; attach a pinned version when discussing an implementation.

**Answer structure:** requirement → state/data flow → bottleneck → proposed change → correctness risk → measurement. Coding: contract → tiny example → plain Python functions → tests → optional vectorization/optimization. Do not start by memorizing a whole production scheduler.

**Runnable starting point:** [Plain-Python engine lab](practice/engine_basics/README.md) provides starter functions, public checks and separate reference solutions for streaming metrics, queue waits and a token-budget scheduler.

## Small coding steps before full engine exercises

Since full from-scratch code was difficult to follow, use these stages; time boxes are practice suggestions, not interview predictions:

1. **15 min:** count token events and compute first/last valid event times (ECODE-01).
2. **20 min:** accumulate two queue intervals with explicit state (ECODE-02).
3. **20 min:** trace then implement one token-budget iteration (ECODE-03).
4. **20 min:** ceil-divide token counts into blocks; only then write pool allocation (ECODE-04).
5. **20 min:** find a common prefix using a loop; only then search several cached prefixes (ECODE-05).
6. **20 min:** score two workers from supplied synthetic measurements (ECODE-06).

For each stage, write one function without consulting the reference, print state after each operation, and explain a boundary case. Extend only when you can predict the output. Treat performance as unmeasured unless actually benchmarked.

## VLLM-01 — Trace a request through the engine

**P0 · Original practice · Evidence/reference: E01,E03**

Trace a streaming request from HTTP input to the first generated output and cancellation. Identify frontend, scheduler, cache manager, worker/model runner and output processing.

**Answer checkpoints:** Explain responsibilities and state ownership before naming classes. Include tokenization, admission, execution and streaming; distinguish CPU overhead from GPU work.

**Follow-up:** Where would you instrument a TTFT regression?

## VLLM-02 — Token-budget scheduling

**P0 · Original practice · Evidence/reference: E02**

A toy iteration has budget 12 tokens. Four active requests need one decode token each. Two waiting prompts have 10 and 6 uncached tokens. With decode-first scheduling and FCFS prefill, allocate this iteration.

**Answer checkpoints:** Four decode tokens leave eight for a partial first prompt; second prompt waits. State assumptions: no cache-pressure constraint, no speculation, one token per decode. This is a toy model, not complete runtime behavior.

**Follow-up:** What tradeoff changes when the token budget rises?

## VLLM-03 — Paged KV mapping

**P0 · Original practice · Evidence/reference: E04**

A request has 35 cached tokens and blocks hold 16 tokens. Show logical-to-physical mapping, internal slack and growth when one more token arrives.

**Answer checkpoints:** Three blocks with capacity 48 and 13 unused token slots; adding one token uses a current free slot. Paging bounds tail waste, not total cache growth. Block sharing changes physical allocation.

**Follow-up:** How do refcounts and copy-on-write change branching generation?

## VLLM-04 — Prefix reuse correctness

**P0 · Original practice · Evidence/reference: E05**

Two prompts share a long textual prefix but use different adapters. What must match before sharing cached KV?

**Answer checkpoints:** Check effective model/adapter, token identities, positions, relevant multimodal inputs and cache namespace. Textual similarity alone is insufficient. Explicitly state implementation/version assumptions.

**Follow-up:** Why can prefix reuse improve prefill yet leave long decode slow?

## VLLM-05 — Preemption and recomputation

**P0 · Original practice · Evidence/reference: E02**

Explain why an active request might be preempted despite successful model loading. How would you diagnose repeated recomputation?

**Answer checkpoints:** Check growing KV demand, concurrency, context lengths and pool headroom. Change one setting at a time; extra memory or parallelism carries other costs. Current V1 documentation describes recompute as default.

**Follow-up:** What evidence would justify reducing admission rather than adding GPUs?

## VLLM-06 — Compilation and CUDA graphs

**P0 · Original practice · Evidence/reference: E01,E07**

What work can compilation and graph replay remove? Why might a fast warm engine still miss its cold-request SLO?

**Answer checkpoints:** Separate loading, compilation, autotuning, graph capture and warmed execution. Graph coverage, memory and dynamism impose constraints; prewarming should reflect the workload.

**Follow-up:** Design a cold/warm benchmark without hiding compilation cost.

## SGL-01 — Radix prefix reuse

**P0 · Original practice · Evidence/reference: E08**

Draw a token-prefix tree for [1,2,3,4], [1,2,3,5], and [1,2,6]. What can be shared, and what must remain request-specific?

**Answer checkpoints:** Trace exact common prefixes and associated KV state. Explain compressed edges conceptually; token generation and mutable tails retain request ownership. Radix reuse is not semantic answer caching.

**Follow-up:** How would a cache namespace prevent model/tenant mix-ups?

## SGL-02 — Eviction with live references

**P0 · Original practice · Evidence/reference: E08,E09**

A hot prefix has been unused recently but is referenced by an active request. Can a recency policy immediately free its storage?

**Answer checkpoints:** First determine what is reclaimable; popularity/recency policy operates within ownership constraints. Then compare LRU with workload-dependent alternatives.

**Follow-up:** How would you test that eviction cannot invalidate a running batch?

## SGL-03 — CPU/GPU overlap

**P0 · Original practice · Evidence/reference: E10**

Explain the SGLang v0.4 design of preparing a later batch while the GPU executes the current one. What dependency makes this harder for autoregressive generation?

**Answer checkpoints:** Track next-token dependency and asynchronous execution; speculative/future metadata and synchronization must preserve correctness. Zero overhead is a scoped design/measurement claim, not literal absence of CPU work.

**Follow-up:** Which timeline would show whether overlap actually hid scheduling cost?

## SGL-04 — Memory tuning by failure phase

**P0 · Original practice · Evidence/reference: E11**

Explain why raising the static memory fraction can help cache capacity but cause an activation-time OOM. How does prefill differ from decode here?

**Answer checkpoints:** Budget weights/cache separately from graphs/activations. Identify failing phase before changing chunk size or active-request limits. Do not transfer flag names or percentages mechanically from another engine.

**Follow-up:** Which measurements would distinguish cache exhaustion from activation peaks?

## SGL-05 — Prefill/decode transfer

**P0 · Original practice · Evidence/reference: E12**

Trace a disaggregated request from prefill completion to decode readiness. What state must transfer, and what if the destination fails halfway?

**Answer checkpoints:** Discuss KV layout/identity, readiness acknowledgment, capacity, retry cleanup and cancellation. Transfer and coordination can outweigh compute isolation benefits.

**Follow-up:** How would different tensor-parallel layouts complicate the transfer?

## SGL-06 — Queue timing state machine

**P0 · Original practice · Evidence/reference: P02**

A request waits, runs, retracts, waits again and resumes. Define cumulative queue time without counting running intervals or counting one wait twice.

**Answer checkpoints:** Use explicit lifecycle intervals or a carefully defined accumulator/sentinel. Handle serialization and reset. This is original practice connected to the candidate PR audit; no fresh fix is asserted.

**Follow-up:** What integration test catches a caller that forgets to stamp re-entry?

## OPT-01 — Select the optimization target

**P0 · Original practice · Evidence/reference: E03,E07,E13**

A service has high TTFT, normal token intervals and low GPU activity. Rank queueing, CPU preprocessing, compilation and attention arithmetic as hypotheses.

**Answer checkpoints:** Propose measurements before ranking conclusively. A service symptom alone does not identify a kernel bottleneck. Use an end-to-end latency breakdown and controlled workload.

**Follow-up:** What observation would make you abandon the kernel hypothesis?

## OPT-02 — Quantization operating point

**P1 · Original practice · Evidence/reference: E04,P01**

Compare weight, activation and KV quantization for short prompts versus long-context decode.

**Answer checkpoints:** State which bytes/compute each changes and evaluate quality on relevant slices. Kernel availability, conversion overhead and batch shape affect speed; memory savings alone are insufficient.

**Follow-up:** How do you avoid combining compression and quality results from different experiments?

## OPT-03 — Speculation and parallelism

**P1 · Original practice · Evidence/reference: E02,E14**

Why can high draft acceptance fail to improve latency, and why can larger tensor parallelism make a small-batch request slower?

**Answer checkpoints:** Account for total draft/verify cost and interconnect/synchronization. Measure comparable token work and request latency; compare against a non-speculative baseline at the same load.

**Follow-up:** When would an extra replica beat increasing tensor parallelism?

## OPT-04 — Choose an engine experimentally

**P0 · Original practice · Evidence/reference: E13,E15**

How would you select vLLM or SGLang for a mixed workload of short chats, repeated system prefixes and long documents?

**Answer checkpoints:** Build a feature/compatibility shortlist, then matched tests over request mix and SLO-constrained goodput. Pin versions, hardware, model, dtype, sampling and cache warmness. No universal winner assumed.

**Follow-up:** How do you report a workload where each engine wins a different regime?

## ECODE-01 — Measure streaming events

**P0 · Original practice · Evidence/reference: P01**

Implement first_positive_event(events), last_positive_event(events), then TTFT/E2E from supplied start and event times. Each event has a nonnegative token count.

**Answer checkpoints:** Use MC-06 contract in phone research. Unit-check tokenless trailers, empty streams and multi-token chunks. Do not label event gaps as per-token intervals inside a chunk.

**Follow-up:** Why can an extra call to the clock break a metric identity?

## ECODE-02 — Accumulate queue waits

**P0 · Original practice · Evidence/reference: P02**

Implement QueueWait.start(t), admit(t), and reset(). start opens an interval; admit closes it. Reject repeated start while open, repeated admit while closed and decreasing timestamps.

**Answer checkpoints:** Use an injected clock/input times. Trace start(1), admit(4), start(8), admit(10) => total 5; reset clears sum/state. Define serialization before adding it.

**Follow-up:** What changes if completion or cancellation occurs while waiting?

## ECODE-03 — Budget one scheduler iteration

**P0 · Original practice · Evidence/reference: E02**

Implement choose_batch(active_decode_ids, waiting_prefills, budget). Serve one token per active decode first, then FCFS prefill chunks; reject budget below decode count. Return allocations and new remaining prefill counts.

**Answer checkpoints:** Start with lists/dicts, a pure function and the VLLM-02 example. Do not mutate input; test budget zero with no decodes, exact fit, partial prompt and no waiting work.

**Follow-up:** Add a finite cache-capacity admission check as a separate function.

## ECODE-04 — Allocate KV blocks

**P0 · Original practice · Evidence/reference: E04**

Implement blocks_needed(token_count, block_size), then a fixed pool with allocate(n) and release(ids). Allocation failure leaves the pool unchanged; reject double release.

**Answer checkpoints:** First test ceil division at 0,1,16,17. Then capacity exhaustion, rollback and reuse. Extend to refcounts only after basic invariants hold.

**Follow-up:** How do shared blocks change cancellation cleanup?

## ECODE-05 — Find reusable token prefixes

**P0 · Original practice · Evidence/reference: E08**

First implement common_prefix_length(a,b) using plain Python. Then search a list of cached token sequences for the longest prefix match; ties use insertion order.

**Answer checkpoints:** Test empty sequences, total mismatch, exact match and divergence after several tokens. This linear baseline is sufficient before a trie/radix optimization. No fuzzy text matching.

**Follow-up:** What is the cost, and when is a radix structure worth its complexity?

## ECODE-06 — Route with cache and queue cost

**P0 · Original practice · Evidence/reference: E10**

Given workers with queue_ms and reusable_prefix_tokens, choose minimum queue_ms + (prompt_len-hit_tokens)*ms_per_uncached_token. Reject impossible hit counts; tie by worker ID.

**Answer checkpoints:** Use supplied synthetic costs; test that an overloaded cache-hot worker can lose to a cooler worker. This is an educational heuristic, not the SGLang production routing algorithm.

**Follow-up:** What runtime measurements would improve this model?

## ECASE-01 — Long prompts stall chat

**P0 · Original practice · Evidence/reference: E02,E11**

Synthetic observation: short-chat p95 token interval doubles only when 32k-token prompts arrive. Present a diagnosis and two controlled experiments.

**Answer checkpoints:** Inspect iteration mix and scheduling; compare chunk budgets or isolation while preserving request mix and offered load. Report TTFT and token intervals together.

**Follow-up:** How would you distinguish GPU interference from queue-only delay?

## ECASE-02 — Cache hits rise but goodput falls

**P0 · Original practice · Evidence/reference: E05,E10**

Synthetic observation: cache hits rise after routing changes, but SLO-compliant throughput falls. Explain three distinct causes.

**Answer checkpoints:** Inspect skew/hot workers, longer waits, memory pressure/eviction and useful tokens saved. Hit percentage and saved compute are different quantities.

**Follow-up:** What would you log per request and per worker?

## ECASE-03 — Cache memory settings appear contradictory

**P0 · Original practice · Evidence/reference: E02,E11**

vLLM advice suggests increasing memory utilization for preemption; SGLang advice may suggest decreasing its static fraction for an OOM. Reconcile them.

**Answer checkpoints:** The flags govern resource budgets whose pressure can occur in different places. Cache-capacity exhaustion and total allocation/activation OOM require different responses. Identify engine version and failing phase.

**Follow-up:** How would you demonstrate the limiting budget experimentally?

## ECASE-04 — Disaggregation hurts short requests

**P0 · Original practice · Evidence/reference: E12**

Prefill and decode pools increase hardware use but short-request latency gets worse. What could dominate?

**Answer checkpoints:** Transfer, routing, synchronization, imbalance and extra queue boundaries. Establish whether the workload has enough prefill interference to justify separation.

**Follow-up:** Estimate transfer time as bytes/bandwidth plus fixed overhead.

## ECASE-05 — Microkernel win disappears

**P0 · Original practice · Evidence/reference: E07,E13**

A new attention kernel is 20% faster in isolation, but the service barely changes. What do you measure next?

**Answer checkpoints:** Determine fraction of critical-path time, workload coverage and new overhead. Apply Amdahl-style reasoning and inspect changed batching/caching.

**Follow-up:** Which two baselines distinguish a kernel regression from a harness artifact?

## ECASE-06 — Cancellation leaks capacity

**P0 · Original practice · Evidence/reference: Original lifecycle exercise**

Requests disconnect; completed-request count looks healthy but free cache blocks steadily fall. Trace likely ownership errors.

**Answer checkpoints:** Follow request ID, cancellation propagation, in-flight work and last-reference release. Avoid freeing buffers still used by a GPU operation. Test retries and double cleanup.

**Follow-up:** Design a deterministic test without requiring a real GPU.

## PROJ-01 — vLLM timing contribution

**P0 · Original practice · Evidence/reference: P01**

Explain the timing invariant your benchmark fix protected, the exact event boundaries, and how a regression test makes an extra clock read visible.

**Answer checkpoints:** Use recorded PR evidence. Identify tokenless trailers and endpoint behavior. Describe benchmark correctness; do not assert engine acceleration.

**Follow-up:** Why are scripted clocks useful but insufficient for every integration question?

## PROJ-02 — SGLang retraction contribution

**P0 · Original practice · Evidence/reference: P02**

Explain how a first-forward timestamp minus a later queue-entry timestamp could become negative, and why clamping the number loses information.

**Answer checkpoints:** Trace multiple admissions and accumulation, serialization/reset and the existing sentinel in the merged patch. Separate known caller-path limitation from tested behavior.

**Follow-up:** What would you change in the test strategy based on the later PD-path report?

## PROJ-03 — Triton tuning contribution

**P0 · Original practice · Evidence/reference: P01**

Choose one actual winning shape and one losing regime. Explain mapping, precision, baseline, bottleneck hypothesis and next experiment.

**Answer checkpoints:** Use project audit and verified personal knowledge. Keep INT2 compression and INT4 quality experiments separate; state unreproduced measurements as reported artifacts.

**Follow-up:** What evidence would show your split strategy pays for its reduction overhead?

## PROJ-04 — Observability and resource judgment

**P0 · Original practice · Evidence/reference: P01**

Explain either completion output logging or retry-budget clarification: requirement, code path, compatibility, tests and scope.

**Answer checkpoints:** Use the final merged behavior in the audit. Logging is not a proven speedup; retry-budget work preserved restrictive accounting rather than creating a new budget mechanism.

**Follow-up:** What did review change about your initial approach?

## Applied engine comparison — avoid slogans

| Dimension | What to establish before comparing |
|---|---|
| Request processing | Pin the version and trace frontend, scheduling and worker boundaries. |
| Cache management | Understand vLLM's block-based KV/prefix mechanisms and SGLang's radix reuse; both cover more than a single headline technique. |
| Scheduling | Identify token budgets, admission, mixed-phase handling and retraction/preemption behavior for the deployed configuration. |
| Optimization | Match model/hardware/kernel backend, dtype, graph/compile mode and sampling semantics. |
| Evaluation | Same offered load, length distribution and quality target; report cold/warm and percentile metrics. |

No engine is designated universally faster. Prefix caching, paging, FlashAttention and continuous batching address related but distinct costs; none substitutes for all the others.

## Current progress and maintenance

No independent answers or timed engine exercises have been evaluated yet. [Engine attempt log](inference-engines-attempts.csv) starts unattempted. Preserve IDs and source confidence as research improves. Existing broad CODE-03/07/08/15/16 and DES-01/02/03/07 remain useful later-stage extensions; do not duplicate them as newly reported questions.
