# Two-week plan — Amazon OA first, inference fundamentals daily

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](amazon-10587705-phone-study-plan.md).

**Created October 28, 2026.** Day 1 is October 28; Day 14 is November 10. If starting later, shift dates only within the actual assessment window. November 11 is an estimate from “two weeks,” not a confirmed expiry. The invitation controls the deadline and test rules.

This is the current combined schedule, superseding the earlier OA-only daily sequence. All tracker entries remain unattempted; the plan assumes no demonstrated mastery. Keep this scope stable during source refreshes unless official instructions or actual practice results justify a change.

## Time budget and method

**Normal day: 3 focused hours**, plus breaks. Allocate 70 minutes coding, 20 AI coding, 20 distributed-system scenarios, 10 behavioral/workstyle, 40 ML/inference, and 20 review. That is 140 minutes on OA practice/review and 40 on domain fundamentals. Day 14 is a lighter 90-minute review or the actual assessment if scheduled.

For two coding problems: 5 minutes reading, about 25 minutes on the first, 30 on the second and 10 testing. Three-problem days use 20 minutes each plus 10 testing. On learning days, log a blocker before consulting an explanation; on mock days, finish the entire timed block without hints. The mock's two-question format is a training choice, not a confirmed assessment question count.

In each 20-minute design block, answer four named scenarios in five minutes each: requirement → choice → failure mode → tradeoff. Hide the answer checkpoints first. AI practice uses the specified small bug/task with an assistant; inspect its patch and run tests yourself. Standard coding practice is unassisted. The official packet governs actual assessment tool use.

**Fixture setup:** AI drills are specifications, not prebuilt repositories. Before Day 1, allow up to 20 additional minutes to have a helper create a tiny local app, test runner and the AI-01 defect without showing you its solution. Use the same scaffold thereafter; let the helper seed the next bounded defect outside the timed attempt. Do not build a complete backend during a 20-minute drill. If setup cannot be made ready, use the day's AI block to establish it, log that as setup, and carry the missed drill to the next review block rather than pretending it was a timed solve.

**Review block:** record actual time, hint use, failing cases and cause in the trackers. Choose one highest-impact miss for a short closed-book repair; schedule a full re-solve 48 hours later. If re-solves accumulate, replace the day's second new coding question with the oldest failed P0 question. Do not add hours to catch up. For domain exercises, end with a small derivation, tested function or a five-bullet explanation.

## Day-by-day assignments

### Day 1 — Wed Oct 28 · Baseline and attention shapes

- **Coding 70:** LC 560 Subarray Sum Equals K + LC 994 Rotting Oranges (bank LC-04/13). Record independent baseline before seeing solutions.
- **AI 20:** AI-01, created movie cannot be retrieved. Trace route → service → persistence; test create/read and missing ID.
- **Design 20:** SD-01–04: audience counter, last inventory item, payment retry, duplicate delivery.
- **Behavioral 10:** write three truthful examples of taking ownership; outline one with your personal action and observed result. No invented metrics.
- **Domain 40:** CON-01/02/04. Draw attention tensor shapes, explain causal versus padding masks, and derive the KV example to **4 GiB** without looking at checkpoints.
- **Review 20:** record the baseline and one next action per weakness.

### Day 2 — Thu Oct 29 · Hashing and stable softmax

- **Coding 70:** LC 3 Longest Substring Without Repeating Characters + LC 49 Group Anagrams (LC-01/02). Explain window invariants and frequency signatures.
- **AI 20:** AI-02, route collision and null-result handling.
- **Design 20:** SD-05–08: cache expiry, read-after-write, retry storm, worker backlog.
- **Behavioral 10:** one example of learning an unfamiliar system; explain how you verified understanding.
- **Domain 40:** CODE-01 stable masked softmax in NumPy/PyTorch primitives; test extreme logits, padding and all-masked rows returning zero.
- **Review 20:** test boundaries and log hint use.

### Day 3 — Fri Oct 30 · Prefix/suffix and head sharing

- **Coding 70:** LC 238 Product of Array Except Self + LC 347 Top K Frequent Elements (LC-03/05).
- **AI 20:** AI-03, validation boundaries and null input.
- **Design 20:** SD-09–12: rate limiter, partition key, upload consistency, AZ failure.
- **Behavioral 10:** one disagreement: explain the evidence, decision and how you worked with the other person.
- **Domain 40:** CON-03/05/08: GQA/MQA/MHA, RoPE positions and prefill versus decode. Draw 32 query heads mapped to 8 KV heads; compare cache memory with 32 KV heads.
- **Review 20:** closed-book repair of a Day 1 miss; if it needs more time, apply the replacement rule.

### Day 4 — Sat Oct 31 · Partitioning, intervals and attention code

- **Coding 70:** LC 75 Sort Colors + LC 56 Merge Intervals (LC-06/07).
- **AI 20:** AI-04, shipment events with ordering and deadline boundaries.
- **Design 20:** SD-13–16: event ordering, transactional outbox, search lag, inference overload.
- **Behavioral 10:** one decision made with incomplete information; separate assumptions from facts.
- **Domain 40:** CODE-02, implement single-batch/single-head causal attention first, then add batched heads if time permits. Validate a future-token perturbation test. Log incomplete padding support explicitly.
- **Review 20:** repair a Day 2 miss and inspect attention shape/mask errors.

### Day 5 — Sun Nov 1 · Greedy, stacks and cache correctness

- **Coding 70:** LC 435 Non-overlapping Intervals + LC 739 Daily Temperatures (LC-08/09).
- **AI 20:** AI-05, sequential idempotent create and conflicting payloads.
- **Design 20:** SD-17–20: deadline budgets, recovery targets, config rollout, leaderboard.
- **Behavioral 10:** describe a mistake, its impact and the correction you personally made.
- **Domain 40:** CODE-03, a one-token KV-cache decode reference. Compare several cached steps against full recomputation; keep dropout disabled and positions consistent.
- **Review 20:** repair a Day 3 miss; distinguish failing code from an unclear invariant.

### Day 6 — Mon Nov 2 · Binary search and performance reasoning

- **Coding 70:** LC 875 Koko Eating Bananas + LC 1011 Capacity To Ship Packages Within D Days (LC-10/11). State and prove each monotone feasibility predicate.
- **AI 20:** AI-06, fixed-window rate limiter boundaries.
- **Design 20:** SD-21–24: pagination, observability, poison messages, partition/inventory invariant.
- **Behavioral 10:** a time you prioritized competing requests; explain the customer impact and tradeoff.
- **Domain 40:** CON-17/18/24: GPU memory hierarchy, roofline arithmetic and profiling workflow. Derive the hypothetical **1 ms** bound and name what could make measured time longer.
- **Review 20:** repair a Day 4 miss. Reserve tomorrow's coding pair unread.

### Day 7 — Tue Nov 3 · Full mock 1

- **OA 120, continuous:** coding **LC 215 Kth Largest Element + LC 763 Partition Labels** (70); AI-07 pagination (20); SD-02/07/10/14 (20); behavioral below (10). Use no hints during coding; AI only in its practice section. Coding pair is unseen only if you have not already solved it.
- **Behavioral inside mock:** five brief workplace scenarios: conflicting deadlines, a suspected bug, disagreement, incomplete requirements, and a missed commitment. Give the next action plus rationale; this is practice, not a prediction of the test UI.
- **Domain 40:** CON-09/10/11: TTFT and token metrics, continuous batching, paging versus prefix reuse. Explain why throughput can improve while TTFT gets worse.
- **Review 20:** score correctness, time lost and failure causes. Pick the top two repair priorities. Previously studied design prompts measure recall/application, not unseen performance.

### Day 8 — Wed Nov 4 · Graphs and numerical validation

- **Coding 70:** LC 200 Number of Islands + LC 207 Course Schedule (LC-12/14); replace the second if Mock 1 exposed a more urgent failed P0 skill.
- **AI 20:** AI-08, timezone-aware deadline comparison.
- **Design 20:** SD-03/04/13/23: idempotency, redelivery, ordering and poison messages.
- **Behavioral 10:** explain a quality issue you caught and how you established its impact.
- **Domain 40:** CON-23 + ML-04/05: tolerances, training-serving skew and NaN localization. Write a numerical test checklist for your attention reference.
- **Review 20:** repair a Day 6 miss; retain actual failing inputs.

### Day 9 — Thu Nov 5 · DP foundations and FlashAttention

- **Coding 70:** LC 198 House Robber + LC 322 Coin Change (LC-15/16). State state, transition, base case and iteration order before coding.
- **AI 20:** AI-09, bounded retries and nonretryable errors.
- **Design 20:** SD-01/05/06/15: counts, caching, read consistency and search freshness.
- **Behavioral 10:** one example of investigating beyond the initial symptom.
- **Domain 40:** CON-06/07: derive online softmax updates; explain why FlashAttention saves memory traffic but does not make dense attention linear-time. Use two small score tiles to check the recurrence numerically.
- **Review 20:** re-solve a Mock 1 miss, choosing correctness issues before micro-optimization.

### Day 10 — Fri Nov 6 · DP/greedy and measured fusion

- **Coding 70:** LC 139 Word Break + LC 55 Jump Game (LC-17/18).
- **AI 20:** AI-10, duplicate processing and transactional failure.
- **Design 20:** SD-08/09/16/17: backlog, quotas, overload and deadlines.
- **Behavioral 10:** a time you simplified a process or implementation; identify what improved without overstating scope.
- **Domain 40:** CON-19/20/21 + CASE-12. Explain occupancy, fusion tradeoffs and tiling; derive the **1.111×** end-to-end speedup bound for a 2× optimization of a 20% component.
- **Review 20:** repair a Day 8 miss; review regression-test coverage in the AI patch.

### Day 11 — Sat Nov 7 · Finish core coverage and ML evaluation

- **Coding 70:** LC 134 Gas Station + LC 300 Longest Increasing Subsequence (LC-19/20). For LIS, implement O(n²) DP correctly before discussing the O(n log n) alternative if needed.
- **AI 20:** AI-11, TTL expiry and falsy cached values.
- **Design 20:** SD-11/12/18/19: storage, failover, recovery and rollout.
- **Behavioral 10:** rehearse two previously written examples in 90 seconds each, then answer “what did you personally do?”
- **Domain 40:** ML-01/02/06: leakage, text-to-SQL evaluation and cost per successful task. Make a small comparison table with quality, latency and total cost; do not use invented production results.
- **Review 20:** repair a Day 9 miss. Keep tomorrow's mock problems unread.

### Day 12 — Sun Nov 8 · Full mock 2 and readiness decision

- **OA 120, continuous:** coding **LC 973 K Closest Points to Origin + LC 621 Task Scheduler** (70); AI-12 batch lookup/N+1 fix (20); SD-06/12/16/24 (20); behavioral (10).
- **Behavioral inside mock:** repeat the five Day 7 scenario categories with changed constraints. Evaluate consistency and practical action, not a memorized “ideal personality.”
- **Domain 40:** CASE-01/06: diagnose TTFT regression and critique a suspicious GPU timing claim. For each, write three hypotheses and a measurement that could disprove each.
- **Review 20:** apply the readiness checks below. If ready and the invitation permits, schedule/take the OA on Day 13 or 14; the plan never authorizes starting a live assessment through an assistant.

### Day 13 — Mon Nov 9 · Repair and consolidate, or assessment

- **Coding 70:** re-solve the two highest-impact failures from the mocks, closed book. If neither mock had coding failures, solve **R-05 prefix adjustments to zero + LC 128 Longest Consecutive Sequence**. R-05 is not LC1526; the operation differs.
- **AI 20:** repeat the lowest-scoring AI drill with changed inputs; tie-break by earliest ID. If all passed, repeat AI-04 with shuffled/duplicate events.
- **Design 20:** repeat the four lowest-scoring scenarios; tie-break by earliest ID. If no scores exist, use SD-02/04/08/16.
- **Behavioral 10:** review factual consistency of the examples; remove claims you cannot substantiate.
- **Domain 40:** CON-12/22 + CASE-09: SGLang prefix reuse, precompiled dispatch keys and cold-start diagnosis. Finish with a two-minute explanation tying one concept to a real contribution, without inventing measurements.
- **Review 20:** verify the actual deadline, allowed language/tools, environment instructions and required identification from the official packet. No new hard topics.
- **If taking the real OA today:** it replaces all study blocks; do not do a three-hour cram session first.

### Day 14 — Tue Nov 10 · Light review or assessment

**90 minutes maximum if not taking the OA:** 25 minutes reviewing your coding error log and standard-library APIs; 15 minutes AI debugging workflow; 15 minutes SD-02/04/16; 10 minutes truthful behavioral examples; 15 minutes attention shapes/KV arithmetic/TTFT recall; 10 minutes invitation/environment check. No new problems or kernels.

If the OA is scheduled today, it replaces this review. Its actual duration and rules come from the official packet. Leave a buffer before the verified expiry; do not rely on an assumed November 11 deadline. If practice is still weak, focus remaining time on the two biggest error categories rather than trying to finish either entire question bank.

## Readiness checks and adaptation

These are preparation heuristics, not Amazon's passing criteria:

- Coding: both mock solutions correct with stated complexity and boundary tests, within the 70-minute practice block. If a problem was familiar, mark it familiar; use an unseen reserve instead to assess transfer.
- AI: diagnose and fix a bounded issue, review the assistant's diff and run meaningful regression tests within 20 minutes.
- Design: four defensible decisions in 20 minutes, each with a failure mode and tradeoff.
- Behavioral: honest, consistent responses grounded in actual actions; don't memorize assessment answers.

**Unseen coding reserves:** LC 33 Search in Rotated Sorted Array; LC 15 3Sum; LC 1561 Maximum Number of Coins You Can Get; LC 743 Network Delay Time. Use them only if a mock pair is already familiar. Difficulty/time vary; failure is diagnostic, not a predicted hiring outcome.

**If you have only two hours:** coding 70 + AI 15 + design 15 + behavioral 5 + domain recall 10 + log 5. The 15-minute AI practice is a shortened study drill; retain full 120-minute uninterrupted mocks on Days 7/12 and omit domain work those days if necessary. Cut fresh domain coding and P1/stretch questions before core OA work. Do not compress sleep to complete the bank.

**Defer until after OA:** full GPU GEMM/attention-kernel implementation, advanced speculative-decoding proofs, MoE deep dives and 45-minute domain system-design mocks. In this fortnight, learn their foundations without displacing coding practice. A compatible GPU is not required for this plan's domain assignments.

## Materials and records

- [OA bank: LC IDs and links](amazon-10587705-oa-question-bank.md)
- [OA design and AI drill specifications](amazon-10587705-oa-scenarios.md)
- [ML/inference bank: CON, CODE, CASE, ML IDs](ml-inference-engineering-question-bank.md)
- [OA attempts](amazon-10587705-oa-attempts.csv) · [Domain attempts](ml-inference-engineering-attempts.csv)

Keep one row of factual outcomes per item, adding attempt detail in notes or a separate dated practice log when repeating. This document is a schedule, not evidence that any work has been completed. Existing three-day research refreshes should preserve the schedule and only change it for stronger evidence, official instructions or observed weaknesses.
