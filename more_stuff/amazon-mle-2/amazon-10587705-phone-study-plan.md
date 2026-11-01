# Amazon AWS MLE II — November 12 live-interview study plan

**Current plan, updated October 28, 2026.** Replaces the OA-first schedule. The OA is waived because Suraj previously passed Amazon's online coding round (user-reported). Existing question banks remain practice resources; their OA format and deadline are historical.

## Confirmed interview and uncertainty

- **Thursday, November 12, 2026, 2:00 PM America/New_York — EST, UTC−5 (19:00 UTC).** Reserve at least 60 minutes.
- Interviewer: **Sathishkumar Sivashanmugam**. Scheduling contact: David Raj, as named in the invitation.
- Invitation calls this a **phone interview** and explicitly includes **live coding**. Suraj reports direct progression to the interview loop; whether this call is administratively a screen or a loop component is unresolved and does not change the preparation priority.
- Recruiter says prepare **ML coding and LeetCode-style coding**. Either could be selected; this does not confirm that both must fit in the same hour.
- Exact behavioral/coding split, problem count and available libraries are unconfirmed. Earlier recruiter guidance suggested 30 minutes behavioral plus 30 coding; use that as one rehearsal format, not a guarantee. Prepare a second 20/35/5 format as well.
- No evidence of AI-assisted coding in this round. Practice without assistance. Transcription consent is unrelated to coding-assistant permission.
- Meeting/coding credentials remain in the original invitation. **Do not open, test or inspect the live coding URL before interview time.** No private meeting links or passcodes are copied into research/automation artifacts.

## What changes now

Replace the 70/20/20/10 OA simulations and backend AI-debugging track with **spoken live coding, ML implementations and follow-up-heavy behavioral practice**. Keep domain system design as a short discussion block; full design rounds can expand after the November 12 call. Retain profiling, kernel tuning, precompiled Triton and fusion as the Director's strong team signal. Do not assume “ML coding” means only attention or CUDA: add K-means, basic training steps, evaluation and vector operations.

[Targeted research and six new ML coding specifications](amazon-10587705-phone-research.md) document the limited SageMaker-adjacent interview evidence and the Bedrock/HyperPod evidence gaps. AWS product discussion below is inferred practice, not a claimed exact question list.


## Current inference-engine emphasis — October 28 research update

Use the [engine focus bank](inference-engines-question-bank.md) and [research/readings](inference-engines-research.md) in the existing domain slots below. This replaces those slots, adding no study hours. DSA, ML coding and LP practice remain scheduled. In ML coding, start with small functions when the full implementation is unclear; do not assume the K-means walkthrough established independent mastery.

| Day | Replacement domain work |
|---|---|
| 1 | VLLM-01 and CON-04: request lifecycle and KV arithmetic. |
| 2 | VLLM-02/03 for 20 min; AWS-01 deployment choice for 10. |
| 3 | SGL-01/02: draw shared prefixes and explain eviction eligibility. |
| 4 | FlashAttention versus paging/prefix reuse; VLLM-04. |
| 5 | VLLM-05 and ECASE-03 for 20 min; AWS-02 caching for 10. |
| 6 | SGL-03 and PROJ-02: overlap versus queue-lifecycle correctness. |
| 7 | SGL-04/05 for 20 min; AWS-03 recovery for 10. |
| 8 | VLLM-06 and OPT-01: cold/warm paths and profiling. |
| 9 | ECODE-03 toy budget exercise for 20 min; AWS-04 placement for 10. |
| 10 | OPT-04: fair vLLM/SGLang experiment; connect to a real PR. |
| 11 | ECASE-01/05 and AWS-05: interference, attribution and release gates. |
| 12 | ECASE-02/04: routing and disaggregation tradeoffs. |
| 13 | PROJ-01/02 plus ECASE-06: metric invariants and cleanup. |
| 14 | Within the existing 15-minute domain review: request trace, KV formula and one tuning tradeoff. |

For the next learning block, complete ECODE-01 first and explain its input/output before attempting a scheduler. ECODE-02 connects directly to the SGLang lifecycle contribution; teach/test it one function at a time. These are substitutes within existing coding/review slots if needed, not extra mandatory exercises.

## Daily budget — three focused hours

Normal days: **45 min DSA + 55 min ML coding + 30 min behavioral/project defense + 30 min domain/AWS reasoning + 20 min review**. Use Python as the practice default; if another language is confirmed, adapt. For ML, annotate every tensor shape and know a loop-based fallback when libraries are unavailable.

DSA block: one primary problem, runnable solution and tests; use remaining time for the named follow-up. Follow-ups are optional if correctness is unfinished. ML block: 5 minutes contract/shapes, 35 implementation, 10 tests, 5 explanation. Review: record hint use and failure causes, then schedule a closed-book re-solve 48 hours later. Replace the next new follow-up with failed work; don't expand the daily budget.

**Today, Oct 28 — reset, 30–45 minutes:** read this plan and research supplement, set up a plain local Python file/test runner, locate the current resume and project audit, and write a 60-second introduction using confirmed facts. No full extra study day is required. Choose six truthful story angles: ownership, investigation, failure/learning, disagreement, ambiguity and delivery. Mark an angle missing if no real example is established.

## Exact daily schedule

All LC numbers are canonical LeetCode IDs. CODE/CON/CASE/ML/DES identifiers refer to the existing domain bank; MC/AWS refer to the new research supplement. Days 1–14 run October 29–November 11, leaving interview day light.

| Day | DSA — 45 min | ML coding — 55 min | Behavioral/project — 30 min | Domain/AWS — 30 min |
|---|---|---|---|---|
| **1 · Thu Oct 29** | **560 Subarray Sum Equals K**; follow-up: why a positive-only sliding window fails with negatives. | **MC-01 K-means** with supplied initialization, empty-cluster policy and final reassignment. | Ownership: outline one actual project; distinguish personal implementation from team architecture. | **CON-01/03/04:** attention shapes, GQA and KV arithmetic. Derive the 4 GiB example. |
| **2 · Fri Oct 30** | **56 Merge Intervals**; follow-up: touching endpoints and empty input. | **CODE-01 stable masked softmax + ML-08 cross entropy**, reusing logsumexp reasoning. Finish softmax before extending. | Dive Deep: vLLM measurement work; explain the invariant, failing event sequence and regression test from the project audit. | **AWS-01:** SageMaker inference deployment choice, queueing and cold start. |
| **3 · Sat Oct 31** | **347 Top K Frequent Elements**; follow-up: heap versus bucket costs. | **MC-02 logistic-regression gradient step**; finite-difference check and extreme logits. | Failure/learning: a real unsuccessful approach; state what evidence changed your decision. No invented incident. | **CON-08/09:** prefill/decode, TTFT/ITL/throughput; separate metric definitions from serving bottlenecks. |
| **4 · Sun Nov 1** | **102 Binary Tree Level Order Traversal**; follow-up: explain **236 Lowest Common Ancestor** recursively. | **CODE-02 causal attention** in primitives; single head first, then batches/masks; test future-token isolation. | Triton project: one shape-specific result, baseline and remaining limitation. Consult audit; do not combine unrelated best-case numbers. | **CON-06/07:** FlashAttention and online normalization, with a two-tile numerical example. |
| **5 · Mon Nov 2** | **Mock A, 60 min total:** 20 behavioral + 35 DSA + 5 questions. Helper picks an unread **200 Number of Islands** variant; use a reserve if familiar. | **MC-03 linear-regression step**, then verbal comparison with logistic regression. | Included in mock; use **15 min afterward** to inspect vague claims and long answers. | **AWS-02:** Bedrock latency, stable prompt prefixes and cache observability. |
| **6 · Tue Nov 3** | **739 Daily Temperatures**; follow-up: equal temperatures and stack invariant. | **CODE-03 KV-cache decode**; compare multiple steps with uncached attention. | SGLang contribution: explain actual changed path, semantics and tests; separate it from broader RadixAttention knowledge. | **CON-10/11/12:** batching, paged allocation and prefix reuse. |
| **7 · Wed Nov 4** | **64 Minimum Path Sum**; follow-up **22 Generate Parentheses** approach and invariants. SageMaker-adjacent report, not MLE-II prediction. | **MC-04 classification metrics**, then **MC-05 cosine top-k** if metrics complete. | Disagree and Commit: use a real disagreement with alternatives and decision; if none is recalled, record the gap rather than fabricate. | **AWS-03:** HyperPod worker failure, cluster recovery versus application state. |
| **8 · Thu Nov 5** | **207 Course Schedule**; follow-up: return a valid order or detect a cycle. | **CODE-04 GQA mapping + CODE-05 RoPE**. Prioritize a tested GQA mapping; RoPE may remain a small reference function. | Oracle O1/O2: test infrastructure and useful logs; keep the retracted production-throughput claim out. | **CON-17/18/24:** memory hierarchy, roofline and profiling; derive the 1 ms hypothetical bound. |
| **9 · Fri Nov 6** | **875 Koko Eating Bananas**; explain binary-search boundaries and monotonicity. | **Mock B, 60 min total:** 30 behavioral/project + 30 ML coding. Helper chooses a changed **MC-01 or MC-02** task without revealing it before the timer. | Included in mock; use **25 min afterward** for implementation and story critique. | **AWS-04:** topology-aware GPU scheduling, gang admission and fairness. |
| **10 · Sat Nov 7** | **146 LRU Cache**; follow-up: O(1) operations, capacity one and update semantics. | **MC-06 streaming metrics**; handle tokenless trailers and multi-token events correctly. | Explain one performance claim: workload, baseline, measurement boundary and what did not improve. | **CON-19/20/22:** occupancy, fusion and precompiled dispatch. **CASE-12:** end-to-end speedup bound. |
| **11 · Sun Nov 8** | **322 Coin Change**; follow-up **139 Word Break** state/transition comparison. | **CODE-10 RMSNorm CPU reference**, then sketch a Triton mapping. Check zero input, epsilon and accumulation dtype; GPU run optional. | Customer impact/quality: use a real test or contribution; connect correctness to users without inventing a customer incident. | **AWS-05 + CASE-02:** release gates for a fused kernel and shape-dependent regressions. |
| **12 · Mon Nov 9** | **215 Kth Largest Element**; compare heap/selection and duplicate behavior. | **CODE-06 top-p sampling**; test boundary p, ties and seeded randomness. | Deliver Results: rehearse two examples with specific actions and honest limitations; five follow-ups each. | **DES-01** abbreviated: sketch serving architecture, KV budget, overload and cancellation in 20 min; **CON-13/14** verbal overview in 10. |
| **13 · Tue Nov 10** | **Mock C, 60 min total:** 20 LP/project + 35 coding + 5 questions. Helper secretly chooses DSA or ML; reserve options below. | **45 min:** repair the two largest mock errors; if coding went well, re-solve the oldest ML failure. | **25 min:** audit story consistency and practice short follow-up answers. | **30 min:** **CASE-01/06/07**, TTFT regression, benchmark timing and OOM diagnosis. |
| **14 · Wed Nov 11** | **Light review only, 90 min total:** 20 min coding error log and Python APIs. | 25 min: write softmax, K-means loop and attention shapes from memory; no new hard implementation. | 20 min: introduction + two strongest stories; 10 min: questions for interviewer. | 15 min: TTFT, KV arithmetic, fusion tradeoffs. Device checks outside this study budget. |

**Mock-day accounting:** Days 5/9/13 total 180 minutes including the separate 20-minute review. Day 5 = 60+55+15+30+20; Day 9 = 45+60+25+30+20; Day 13 = 60+45+25+30+20. No extra normal-day behavioral block is added.

### Mock reserves and protocol

Reserve DSA: **973 K Closest Points**, **33 Search in Rotated Sorted Array**, **994 Rotting Oranges** with changed constraints. Reserve ML: **MC-05 cosine top-k**, a changed **CODE-01 mask contract**, or **MC-06 event handling**. A familiar item tests fluency; mark it familiar, not evidence of unseen problem solving. A helper can select from these and alter inputs without giving hints. If practicing alone, draw the prompt at random and record yourself.

Use a plain local editor, not the actual interview session. No AI-generated code, solution hints or hidden auto-completion during timed practice. Narrate decisions, not every keystroke. Explain one sensible approach, implement it fully, and test before chasing a more sophisticated variant. Don't assume the environment can execute code: practice both tests and manual dry runs.

## Story and project rehearsal contract

Start with the current [story bank](../story-bank.md), [role project/PR audit](amazon-10587705-project-pr-review.md) and current CV. Existing draft narratives cannot establish unsupported personal facts. Six useful angles can come from fewer projects, but say when two stories concern the same project. A disagreement/failure story must come from recollection; no generic fictional scripts.

For every story answer: what was the problem, what did you personally do, why that choice, how did you verify it, what happened, what would you change? For every kernel result: which shape/device/dtype, which baseline, which timing method, where did it lose? For vLLM/SGLang: exact scope and tests before describing engine-wide architecture.

## Interview day — Thursday November 12

- **Morning:** 20–30 minutes relaxed recall only. No new kernels, papers or difficult problems.
- **Before 1:45 PM EST:** device, microphone, headset, network and screen-sharing ready; resume and water available. The separate Zoom test page from the invitation can be used in advance; no need to enter the real meeting.
- **2:00 PM EST:** join the actual call. The email's specific waiting-room instruction says join at interview start; be ready early without entering the waiting room early. Open the coding link at interview time, as instructed.
- The confirmation says allow at least 60 minutes. Keep a buffer afterward. Refer to the original invitation if connection issues arise.
- Useful interviewer questions: “Which inference bottlenecks are most important for the team now?” and “How does the team validate and roll out workload-specific kernel optimizations?”

## Adaptation and priorities

If time drops to two hours: DSA 35 + ML coding 40 + LP/project 25 + domain 10 + review 10. Keep all three 60-minute mock sessions intact and reduce other blocks. If a library or exact split is later confirmed, adjust the mock, not the entire bank. Do not replace coding time with cloud-console tutorials.

Core readiness: complete a representative medium DSA solve with tests in about 30–35 minutes; implement a small ML routine with correct shapes, stable arithmetic and edge cases; handle probing follow-ups on two real projects; distinguish measured facts from hypotheses. These are practice targets, not Amazon scoring thresholds. No current pass/readiness judgment is made without actual attempts.

**Deferred:** OA AI-backend drills, workstyle-rating simulations, exhaustive AWS service trivia, full 45-minute system-design sessions and advanced custom-GPU implementations. Those can resume if later-round instructions warrant them.

## Navigation and update policy

- [New AWS research + MC/AWS prompts](amazon-10587705-phone-research.md)
- [Existing DSA bank](amazon-10587705-oa-question-bank.md) — retain questions, ignore superseded OA timing
- [Existing ML/inference bank](ml-inference-engineering-question-bank.md)
- [Interview practice log](amazon-10587705-phone-attempts.csv)

Three-day research refresh should now target this interview and the relevant banks, never restore OA assignments, and preserve actual practice outcomes. Notify only material changes. After the November 12 interview, await the user's debrief/next schedule rather than inventing new dates.
