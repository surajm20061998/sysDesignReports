# Amazon MLE II — complete interview preparation

**Consolidated October 31, 2026** for Suraj Mishra. **Role:** Machine Learning Engineer II, AWS Inference Optimization, req 10587705.

**Next confirmed interview:** Thursday, **November 12, 2026, 2:00 PM Eastern / EST (UTC−5)**, at least 60 minutes, with Sathishkumar Sivashanmugam. Live coding is confirmed; recruiter guidance covers ML-based and LeetCode-style coding. The OA is waived based on the user's prior pass. Exact time split and library availability remain unconfirmed.

This file brings together the interview-specific plans, question banks, research, project notes, practice code and progress trackers created in this conversation. Current materials come first. Earlier recruiter and OA plans are retained under historical labels; use the November 12 plan for present assignments. Source-date and evidence limitations inside each document still apply.

**Navigation:** use the contents below. The engine reference solutions are later in the practice section so you can attempt the starter first. Source links point back to the original files; included cross-document links jump within this compilation. The embedded source snapshots and CSVs reflect October 31; future practice should be recorded in the original trackers until this compilation is refreshed.

**Role artifacts:** [Resume PDF](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.pdf) · [Editable resume TeX](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.tex). The archived JD and resume's Markdown source are included below. Private meeting/coding access credentials remain in the original invitation.

## Contents

1. [Current interview study plan](#material-01) — current
2. [AWS research and ML coding supplement](#material-02) — current
3. [Inference-engine question bank](#material-03) — current
4. [Inference-engine research and resources](#material-04) — current
5. [ML, attention and inference question bank](#material-05) — current
6. [Cross-company research sources](#material-06) — current
7. [Project and PR evidence audit](#material-07) — current
8. [Technical revision notes](#material-08) — reference
9. [Interview practice log](#material-09) — progress
10. [Inference-engine practice tracker](#material-10) — progress
11. [ML and inference practice tracker](#material-11) — progress
12. [Plain-Python engine lab guide](#material-12) — practice
13. [Engine lab starter exercises](#material-13) — practice
14. [Engine lab public checks](#material-14) — practice
15. [K-means teaching implementation](#material-15) — practice
16. [Engine lab reference solutions — spoilers](#material-16) — solutions
17. [Historical full interview dossier](#material-17) — historical
18. [Historical recruiter-call brief](#material-18) — historical
19. [DSA/OA question bank — OA stage waived](#material-19) — historical
20. [OA system-design and AI exercises — historical format](#material-20) — historical
21. [OA research ledger](#material-21) — historical
22. [Historical OA-first combined schedule](#material-22) — historical
23. [Historical OA practice tracker](#material-23) — historical
24. [Archived role description](#material-24) — supporting
25. [Role-specific resume source](#material-25) — supporting
26. [Current STAR rehearsal stories — relevant excerpt](#material-26) — supporting


---

<a id="material-01"></a>

## 01. Current interview study plan

**Source:** [amazon-10587705-phone-study-plan.md](amazon-10587705-phone-study-plan.md) · **Section:** current

### Amazon AWS MLE II — November 12 live-interview study plan

**Current plan, updated October 28, 2026.** Replaces the OA-first schedule. The OA is waived because Suraj previously passed Amazon's online coding round (user-reported). Existing question banks remain practice resources; their OA format and deadline are historical.

#### Confirmed interview and uncertainty

- **Thursday, November 12, 2026, 2:00 PM America/New_York — EST, UTC−5 (19:00 UTC).** Reserve at least 60 minutes.
- Interviewer: **Sathishkumar Sivashanmugam**. Scheduling contact: David Raj, as named in the invitation.
- Invitation calls this a **phone interview** and explicitly includes **live coding**. Suraj reports direct progression to the interview loop; whether this call is administratively a screen or a loop component is unresolved and does not change the preparation priority.
- Recruiter says prepare **ML coding and LeetCode-style coding**. Either could be selected; this does not confirm that both must fit in the same hour.
- Exact behavioral/coding split, problem count and available libraries are unconfirmed. Earlier recruiter guidance suggested 30 minutes behavioral plus 30 coding; use that as one rehearsal format, not a guarantee. Prepare a second 20/35/5 format as well.
- No evidence of AI-assisted coding in this round. Practice without assistance. Transcription consent is unrelated to coding-assistant permission.
- Meeting/coding credentials remain in the original invitation. **Do not open, test or inspect the live coding URL before interview time.** No private meeting links or passcodes are copied into research/automation artifacts.

#### What changes now

Replace the 70/20/20/10 OA simulations and backend AI-debugging track with **spoken live coding, ML implementations and follow-up-heavy behavioral practice**. Keep domain system design as a short discussion block; full design rounds can expand after the November 12 call. Retain profiling, kernel tuning, precompiled Triton and fusion as the Director's strong team signal. Do not assume “ML coding” means only attention or CUDA: add K-means, basic training steps, evaluation and vector operations.

[Targeted research and six new ML coding specifications](#material-02) document the limited SageMaker-adjacent interview evidence and the Bedrock/HyperPod evidence gaps. AWS product discussion below is inferred practice, not a claimed exact question list.


#### Current inference-engine emphasis — October 28 research update

Use the [engine focus bank](#material-03) and [research/readings](#material-04) in the existing domain slots below. This replaces those slots, adding no study hours. DSA, ML coding and LP practice remain scheduled. In ML coding, start with small functions when the full implementation is unclear; do not assume the K-means walkthrough established independent mastery.

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

#### Daily budget — three focused hours

Normal days: **45 min DSA + 55 min ML coding + 30 min behavioral/project defense + 30 min domain/AWS reasoning + 20 min review**. Use Python as the practice default; if another language is confirmed, adapt. For ML, annotate every tensor shape and know a loop-based fallback when libraries are unavailable.

DSA block: one primary problem, runnable solution and tests; use remaining time for the named follow-up. Follow-ups are optional if correctness is unfinished. ML block: 5 minutes contract/shapes, 35 implementation, 10 tests, 5 explanation. Review: record hint use and failure causes, then schedule a closed-book re-solve 48 hours later. Replace the next new follow-up with failed work; don't expand the daily budget.

**Today, Oct 28 — reset, 30–45 minutes:** read this plan and research supplement, set up a plain local Python file/test runner, locate the current resume and project audit, and write a 60-second introduction using confirmed facts. No full extra study day is required. Choose six truthful story angles: ownership, investigation, failure/learning, disagreement, ambiguity and delivery. Mark an angle missing if no real example is established.

#### Exact daily schedule

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

##### Mock reserves and protocol

Reserve DSA: **973 K Closest Points**, **33 Search in Rotated Sorted Array**, **994 Rotting Oranges** with changed constraints. Reserve ML: **MC-05 cosine top-k**, a changed **CODE-01 mask contract**, or **MC-06 event handling**. A familiar item tests fluency; mark it familiar, not evidence of unseen problem solving. A helper can select from these and alter inputs without giving hints. If practicing alone, draw the prompt at random and record yourself.

Use a plain local editor, not the actual interview session. No AI-generated code, solution hints or hidden auto-completion during timed practice. Narrate decisions, not every keystroke. Explain one sensible approach, implement it fully, and test before chasing a more sophisticated variant. Don't assume the environment can execute code: practice both tests and manual dry runs.

#### Story and project rehearsal contract

Start with the current [story bank](#material-26), [role project/PR audit](#material-07) and current CV. Existing draft narratives cannot establish unsupported personal facts. Six useful angles can come from fewer projects, but say when two stories concern the same project. A disagreement/failure story must come from recollection; no generic fictional scripts.

For every story answer: what was the problem, what did you personally do, why that choice, how did you verify it, what happened, what would you change? For every kernel result: which shape/device/dtype, which baseline, which timing method, where did it lose? For vLLM/SGLang: exact scope and tests before describing engine-wide architecture.

#### Interview day — Thursday November 12

- **Morning:** 20–30 minutes relaxed recall only. No new kernels, papers or difficult problems.
- **Before 1:45 PM EST:** device, microphone, headset, network and screen-sharing ready; resume and water available. The separate Zoom test page from the invitation can be used in advance; no need to enter the real meeting.
- **2:00 PM EST:** join the actual call. The email's specific waiting-room instruction says join at interview start; be ready early without entering the waiting room early. Open the coding link at interview time, as instructed.
- The confirmation says allow at least 60 minutes. Keep a buffer afterward. Refer to the original invitation if connection issues arise.
- Useful interviewer questions: “Which inference bottlenecks are most important for the team now?” and “How does the team validate and roll out workload-specific kernel optimizations?”

#### Adaptation and priorities

If time drops to two hours: DSA 35 + ML coding 40 + LP/project 25 + domain 10 + review 10. Keep all three 60-minute mock sessions intact and reduce other blocks. If a library or exact split is later confirmed, adjust the mock, not the entire bank. Do not replace coding time with cloud-console tutorials.

Core readiness: complete a representative medium DSA solve with tests in about 30–35 minutes; implement a small ML routine with correct shapes, stable arithmetic and edge cases; handle probing follow-ups on two real projects; distinguish measured facts from hypotheses. These are practice targets, not Amazon scoring thresholds. No current pass/readiness judgment is made without actual attempts.

**Deferred:** OA AI-backend drills, workstyle-rating simulations, exhaustive AWS service trivia, full 45-minute system-design sessions and advanced custom-GPU implementations. Those can resume if later-round instructions warrant them.

#### Navigation and update policy

- [New AWS research + MC/AWS prompts](#material-02)
- [Existing DSA bank](#material-19) — retain questions, ignore superseded OA timing
- [Existing ML/inference bank](#material-05)
- [Interview practice log](#material-09)

Three-day research refresh should now target this interview and the relevant banks, never restore OA assignments, and preserve actual practice outcomes. Notify only material changes. After the November 12 interview, await the user's debrief/next schedule rather than inventing new dates.

---

<a id="material-02"></a>

## 02. AWS research and ML coding supplement

**Source:** [amazon-10587705-phone-research.md](amazon-10587705-phone-research.md) · **Section:** current

### November 12 phone interview — targeted AWS research and ML coding supplement

**Researched October 28, 2026.** Exact role: MLE II, AWS Inference Optimization, req 10587705. Research targets: SageMaker, Bedrock and HyperPod. These are relevant AWS product areas; neither the invitation nor public evidence establishes that the role belongs to all three teams. No verified question set for the exact role/interviewer was found.

#### Evidence ranked by relevance

| Source | What is established | Limit and preparation consequence |
|---|---|---|
| User-supplied invitation | November 12, 2026, 2 PM Eastern (UTC−5), at least 60 minutes, interviewer Sathishkumar Sivashanmugam, phone/video call with live coding | Strongest scheduling evidence. Calls it a phone interview; user describes direct progression to interview loop. Do not resolve stage naming by guessing. |
| Recruiter guidance relayed by Suraj | Prepare both ML-based and LeetCode-style coding | Strongest content signal. No library availability, language, exact split, number of problems or AI assistance permission specified. |
| [SageMaker-adjacent candidate report](https://leetcode.com/discuss/post/6361672/Amazon-or-SDE-1-Fresher-or-India-or-Interview-Experience/) | SDE I fresher, India; Jan 16, 2025 DSA interview conducted by an SDE II from SageMaker: Minimum Path Sum and Generate Parentheses. Jan 23 machine-coding round and LPs. | Firsthand anonymous account, not MLE II. Interviewer's level is not candidate's level; interviewer team is not proof of hiring team. Add DP/backtracking coverage, not chess-game preparation. |
| [Amazon MLE II account](https://www.onsites.fyi/Amazon/Machine%20Learning%20Engineer/001DC8E474) | Onsite report labels MLE II and describes trees, monotonic stack, design, ML breadth and behavioral questions | Curated site, date/location/team unknown. Supports breadth only; do not label SageMaker/Bedrock/HyperPod. |
| [Amazon MLE phone/onsite account](https://prachub.com/interview-experiences/amazon-machine-learning-engineer-interview-experience-phone-screen-ml-deep-dive-then-a-five-round-onsite) | Described interview Dec 2025, published Aug 25, 2026. ML project/evaluation discussion and K-means in the screen; intervals/frequency coding later | Commercial curated/edited account, original author/team/level not established. Lower confidence. K-means merits practice; its claim that runnable code was unnecessary does NOT override your live-coding preparation. |
| [Official Amazon SDE II preparation](https://www.amazon.jobs/content/en/how-we-hire/sde-ii-interview-prep) | Technical problem solving and Leadership Principles both matter in adjacent engineering interviews | Official but SDE II, not this MLE packet. Do not restore OA requirements or assume its loop layout. |
| [Official Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) | Behavioral framework | Practice actual decisions, evidence and lessons; no invented stories or metrics. |

##### Search coverage and exclusions

Searched public LeetCode, Reddit, Glassdoor, 1point3acres-indexed material and niche candidate-report sites for SageMaker/MLE II, Amazon Bedrock and HyperPod interviews, including Chinese search terms. **No attributable, sufficiently specific Bedrock or HyperPod MLE II coding report was located.** Glassdoor/Reddit results often concerned engineers using AWS at other employers, general advice, or candidates asking what to expect. Some “Bedrock” results were unrelated companies, including robotics/property businesses. All excluded from AWS interview evidence. 1point3acres search-visible listings did not yield a usable complete exact-team prompt; hidden content was not reconstructed.

Do not treat a service tutorial, role advertisement or commercial “top questions” page as proof of an interview question. No frequencies or pass thresholds are supported. No interviewer background or question preferences inferred from their name.

#### What to learn from the AWS products

These are **practice topics inferred from primary engineering documentation**, not reported interview questions. Spend bounded discussion time on mechanisms, not certification trivia or memorizing SDK parameters.

##### AWS-01 — SageMaker deployment choice

A customer needs interactive low-latency inference, while another can wait for long jobs. Explain deployment choice, queueing, scaling, model startup and monitoring. Where do your container/runtime responsibilities end and managed infrastructure responsibilities begin?

**Checkpoint:** distinguish online latency requirements from asynchronous work; state workload and capacity assumptions before selecting an endpoint. Discuss cold starts and model resources, with no universal claim that every endpoint option supports every accelerator/model. [SageMaker deployment documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)

##### AWS-02 — Bedrock latency and caching

A managed-model API workload repeatedly sends a large shared prefix. Design an experiment to reduce TTFT and cost without reducing answer quality. How do you distinguish prompt caching from caching complete responses?

**Checkpoint:** measure queue/network/prefill contributions and actual cache usage; keep reusable content stable. Cache eligibility/support differs by model/API, and a repeated request is not a guaranteed hit. Response caching also depends on full request semantics and freshness. [Bedrock overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)

##### AWS-03 — HyperPod resilience

A multi-GPU workload loses a worker. Explain detection, replacement, workload recovery, checkpoint integrity and what the application must still do. Why does a healthy cluster not guarantee a correct resumed job?

**Checkpoint:** HyperPod manages resilient ML clusters with Slurm or EKS options; application-level state and recovery semantics still need validation. Distinguish training checkpoints from transient inference KV state. [HyperPod documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)

##### AWS-04 — HyperPod capacity and placement

An eight-GPU job shares a cluster with one-GPU jobs. Propose topology-aware gang admission, a starvation policy, quotas and failure recovery. How would online inference and offline work coexist?

**Checkpoint:** explicit resource ownership/leases, bounded queues, placement constraints and admission; evaluate utilization alongside fairness and latency. This scheduling problem is our synthesis, not a documented HyperPod interview question. Use the HyperPod overview for product context and the existing domain design bank for systems reasoning.

##### AWS-05 — Performance release gate

You have a faster Triton kernel for some shapes. Design correctness and performance gates before serving it through a managed endpoint or cluster.

**Checkpoint:** representative shape/dtype/device matrix, numerical tolerances, pinned versions, compile versus warm time, end-to-end SLO and rollback. Explain precompiled variants/fallback and why a microbenchmark win is not enough. Original exercise grounded in the existing Triton/NVIDIA references in [the domain ledger](#material-06).

#### Additional ML coding — bounded, runnable practice

These supplement the existing attention/kernel bank. They are **original specifications**; only the broad K-means theme has the lower-confidence reported support above. Default practice language: Python. NumPy is for rehearsal when available; be able to express loops and shapes without it. Actual libraries must be confirmed by the interviewer. Do not use sklearn estimators or built-in attention/loss functions to bypass the requested implementation.

##### MC-01 — K-means, 45 minutes

Implement `kmeans(X, initial_centroids, max_iter, tol)` for finite X[N,D] and supplied centers[K,D], 1≤K≤N. Use squared Euclidean distance, assign ties to the smallest center index, update means, retain a previous center for an empty cluster, and stop on maximum center displacement ≤tol or iteration limit. Return centers and assignments recomputed against final centers.

Tests: two separated clusters, K=1, duplicate points, empty cluster, no movement, max_iter=1. Explain O(iterations*N*K*D) work and avoid needlessly materializing N*K*D intermediates. Reference: [scikit-learn's K-means explanation](https://scikit-learn.org/stable/modules/clustering.html#k-means); these interface/edge-case choices are ours.

##### MC-02 — Logistic-regression step, 45 minutes

Given X[N,D], y[N] in {0,1}, w[D], b and learning rate, implement mean binary cross entropy from logits plus one batch-gradient step. Use a stable sigmoid and `max(z,0)-z*y+log1p(exp(-abs(z)))` for loss. No regularization in the base task.

Tests: zero weights, extreme positive/negative logits, N=1, finite-difference gradient on a tiny case, decreasing loss with a suitably small step. Follow-up: add L2 on w only, explicitly defining its coefficient convention.

##### MC-03 — Linear-regression step, 35 minutes

Implement predictions, mean squared error and gradients for Xw+b; loss is mean((prediction-y)^2), without a 1/2 factor. Include shape validation.

Tests: exact fit, nonzero residual, N=1, finite differences; explain feature scaling and the learning-rate tradeoff. Follow-up: compare closed-form least squares without claiming explicit matrix inversion is required.

##### MC-04 — Classification metrics, 30 minutes

Given binary labels and prediction scores, compute TP/FP/TN/FN, precision, recall and F1 at a supplied threshold; predict positive when score≥threshold. Define a zero denominator to return 0 for this exercise.

Tests: all negatives, no predicted positives, perfect predictions, threshold boundary and empty-input policy. Explain why accuracy can mislead with imbalance and why threshold selection must not use the held-out test set.

##### MC-05 — Cosine top-k retrieval, 40 minutes

Given query[D], embeddings[N,D] and 1≤k≤N, return highest cosine scores and indices. Define zero-vector similarity as 0 and ties by ascending index.

Tests: identical/opposite vectors, zero vectors, ties and k=N. Compare sort versus bounded heap/selection and chunked computation when N is large. Do not accidentally rank by raw dot product when norms differ.

##### MC-06 — Streaming latency metrics, 40 minutes

Input: request start time and time-ordered events `(timestamp, token_count)`, where token_count≥0. Return TTFT to the first positive-token event, E2E to the last positive-token event, gaps between positive-token events, and total token count. Tokenless trailers must not extend E2E. For no tokens, return None for TTFT/E2E and an empty gap list. Reject decreasing timestamps and timestamps before request start.

Tests: empty stream, tokenless first/trailing events, one positive event, multi-token chunks, equal timestamps. Explain why event gaps cannot reconstruct individual-token latency within a chunk. This is a synthetic task inspired by the candidate's vLLM measurement work, not a claim about an Amazon interview question.

#### Practice mechanics

Each live solve: clarify contract → tiny example → approach/invariant and complexity → complete code → edge cases → follow-up. Use a plain local editor, speak aloud, and avoid AI during timed coding mocks. Ask which libraries are permitted rather than assuming NumPy/PyTorch. The invite's transcription feature is not permission to use an AI coding assistant.


#### Research refresh — October 31, 2026

Searched recent-window and broader public LeetCode, Reddit, Glassdoor and 1point3acres-indexed results for Amazon MLE II, SageMaker, Bedrock and HyperPod. No new attributable exact-team/level coding report qualified for addition. Search recency filters also returned older posts; crawl dates were not treated as interview dates. Excluded an Aug 7 MLE-loop preparation request (https://www.reddit.com/r/amazonsdeprep/comments/1vhne6a/machine_learning_engineer_loop_prep/) because it asks what to expect rather than reports completed interviews, an older senior-level promotional account already encountered, unrelated employers using HyperPod, and broad commercial guides with no original prompt provenance. Reopened the existing curated Amazon MLE/K-means source; its team/level/date limitations remain.

November 12 live coding, ML implementations, DSA and truthful project/LP defense remain the priorities. Schedule and question IDs unchanged. Phone and question-bank trackers contain no recorded attempts as of this check; no independent mastery or readiness inferred from chat explanations. No private interview links opened.

---

<a id="material-03"></a>

## 03. Inference-engine question bank

**Source:** [inference-engines-question-bank.md](inference-engines-question-bank.md) · **Section:** current

### Inference engines — vLLM and SGLang interview focus

**Research date: October 28, 2026.** Supplement to the [cross-company domain bank](#material-05) for the November 12 Amazon MLE II interview. **32 targeted questions/exercises**: six vLLM, six SGLang, four optimization, six coding, six cases and four project defenses. These extend engine-specific follow-ups; existing general attention, quantization and design questions remain in the main bank.

All 32 prompts below are **original practice**, including prompts inspired by a candidate account or the user's own contributions. They are not claimed verbatim reported interview questions. Priority indicates training value, not frequency. [Research evidence and reading list](#material-04) distinguishes public reports from technical sources. No complete exact-team vLLM/SGLang question set was found.

#### Highest priority for November 12

Be able to trace a request, explain prefill/decode and metrics, calculate KV memory, distinguish paging from prefix reuse, reason through batching/cache pressure, and defend your actual vLLM/SGLang contributions. Kernel/profiling reasoning remains central given the Director's stated focus. Engine flags/defaults and source class names are version-dependent. Start with mechanisms; attach a pinned version when discussing an implementation.

**Answer structure:** requirement → state/data flow → bottleneck → proposed change → correctness risk → measurement. Coding: contract → tiny example → plain Python functions → tests → optional vectorization/optimization. Do not start by memorizing a whole production scheduler.

**Runnable starting point:** [Plain-Python engine lab](#material-12) provides starter functions, public checks and separate reference solutions for streaming metrics, queue waits and a token-budget scheduler.

#### Small coding steps before full engine exercises

Since full from-scratch code was difficult to follow, use these stages; time boxes are practice suggestions, not interview predictions:

1. **15 min:** count token events and compute first/last valid event times (ECODE-01).
2. **20 min:** accumulate two queue intervals with explicit state (ECODE-02).
3. **20 min:** trace then implement one token-budget iteration (ECODE-03).
4. **20 min:** ceil-divide token counts into blocks; only then write pool allocation (ECODE-04).
5. **20 min:** find a common prefix using a loop; only then search several cached prefixes (ECODE-05).
6. **20 min:** score two workers from supplied synthetic measurements (ECODE-06).

For each stage, write one function without consulting the reference, print state after each operation, and explain a boundary case. Extend only when you can predict the output. Treat performance as unmeasured unless actually benchmarked.

#### VLLM-01 — Trace a request through the engine

**P0 · Original practice · Evidence/reference: E01,E03**

Trace a streaming request from HTTP input to the first generated output and cancellation. Identify frontend, scheduler, cache manager, worker/model runner and output processing.

**Answer checkpoints:** Explain responsibilities and state ownership before naming classes. Include tokenization, admission, execution and streaming; distinguish CPU overhead from GPU work.

**Follow-up:** Where would you instrument a TTFT regression?

#### VLLM-02 — Token-budget scheduling

**P0 · Original practice · Evidence/reference: E02**

A toy iteration has budget 12 tokens. Four active requests need one decode token each. Two waiting prompts have 10 and 6 uncached tokens. With decode-first scheduling and FCFS prefill, allocate this iteration.

**Answer checkpoints:** Four decode tokens leave eight for a partial first prompt; second prompt waits. State assumptions: no cache-pressure constraint, no speculation, one token per decode. This is a toy model, not complete runtime behavior.

**Follow-up:** What tradeoff changes when the token budget rises?

#### VLLM-03 — Paged KV mapping

**P0 · Original practice · Evidence/reference: E04**

A request has 35 cached tokens and blocks hold 16 tokens. Show logical-to-physical mapping, internal slack and growth when one more token arrives.

**Answer checkpoints:** Three blocks with capacity 48 and 13 unused token slots; adding one token uses a current free slot. Paging bounds tail waste, not total cache growth. Block sharing changes physical allocation.

**Follow-up:** How do refcounts and copy-on-write change branching generation?

#### VLLM-04 — Prefix reuse correctness

**P0 · Original practice · Evidence/reference: E05**

Two prompts share a long textual prefix but use different adapters. What must match before sharing cached KV?

**Answer checkpoints:** Check effective model/adapter, token identities, positions, relevant multimodal inputs and cache namespace. Textual similarity alone is insufficient. Explicitly state implementation/version assumptions.

**Follow-up:** Why can prefix reuse improve prefill yet leave long decode slow?

#### VLLM-05 — Preemption and recomputation

**P0 · Original practice · Evidence/reference: E02**

Explain why an active request might be preempted despite successful model loading. How would you diagnose repeated recomputation?

**Answer checkpoints:** Check growing KV demand, concurrency, context lengths and pool headroom. Change one setting at a time; extra memory or parallelism carries other costs. Current V1 documentation describes recompute as default.

**Follow-up:** What evidence would justify reducing admission rather than adding GPUs?

#### VLLM-06 — Compilation and CUDA graphs

**P0 · Original practice · Evidence/reference: E01,E07**

What work can compilation and graph replay remove? Why might a fast warm engine still miss its cold-request SLO?

**Answer checkpoints:** Separate loading, compilation, autotuning, graph capture and warmed execution. Graph coverage, memory and dynamism impose constraints; prewarming should reflect the workload.

**Follow-up:** Design a cold/warm benchmark without hiding compilation cost.

#### SGL-01 — Radix prefix reuse

**P0 · Original practice · Evidence/reference: E08**

Draw a token-prefix tree for [1,2,3,4], [1,2,3,5], and [1,2,6]. What can be shared, and what must remain request-specific?

**Answer checkpoints:** Trace exact common prefixes and associated KV state. Explain compressed edges conceptually; token generation and mutable tails retain request ownership. Radix reuse is not semantic answer caching.

**Follow-up:** How would a cache namespace prevent model/tenant mix-ups?

#### SGL-02 — Eviction with live references

**P0 · Original practice · Evidence/reference: E08,E09**

A hot prefix has been unused recently but is referenced by an active request. Can a recency policy immediately free its storage?

**Answer checkpoints:** First determine what is reclaimable; popularity/recency policy operates within ownership constraints. Then compare LRU with workload-dependent alternatives.

**Follow-up:** How would you test that eviction cannot invalidate a running batch?

#### SGL-03 — CPU/GPU overlap

**P0 · Original practice · Evidence/reference: E10**

Explain the SGLang v0.4 design of preparing a later batch while the GPU executes the current one. What dependency makes this harder for autoregressive generation?

**Answer checkpoints:** Track next-token dependency and asynchronous execution; speculative/future metadata and synchronization must preserve correctness. Zero overhead is a scoped design/measurement claim, not literal absence of CPU work.

**Follow-up:** Which timeline would show whether overlap actually hid scheduling cost?

#### SGL-04 — Memory tuning by failure phase

**P0 · Original practice · Evidence/reference: E11**

Explain why raising the static memory fraction can help cache capacity but cause an activation-time OOM. How does prefill differ from decode here?

**Answer checkpoints:** Budget weights/cache separately from graphs/activations. Identify failing phase before changing chunk size or active-request limits. Do not transfer flag names or percentages mechanically from another engine.

**Follow-up:** Which measurements would distinguish cache exhaustion from activation peaks?

#### SGL-05 — Prefill/decode transfer

**P0 · Original practice · Evidence/reference: E12**

Trace a disaggregated request from prefill completion to decode readiness. What state must transfer, and what if the destination fails halfway?

**Answer checkpoints:** Discuss KV layout/identity, readiness acknowledgment, capacity, retry cleanup and cancellation. Transfer and coordination can outweigh compute isolation benefits.

**Follow-up:** How would different tensor-parallel layouts complicate the transfer?

#### SGL-06 — Queue timing state machine

**P0 · Original practice · Evidence/reference: P02**

A request waits, runs, retracts, waits again and resumes. Define cumulative queue time without counting running intervals or counting one wait twice.

**Answer checkpoints:** Use explicit lifecycle intervals or a carefully defined accumulator/sentinel. Handle serialization and reset. This is original practice connected to the candidate PR audit; no fresh fix is asserted.

**Follow-up:** What integration test catches a caller that forgets to stamp re-entry?

#### OPT-01 — Select the optimization target

**P0 · Original practice · Evidence/reference: E03,E07,E13**

A service has high TTFT, normal token intervals and low GPU activity. Rank queueing, CPU preprocessing, compilation and attention arithmetic as hypotheses.

**Answer checkpoints:** Propose measurements before ranking conclusively. A service symptom alone does not identify a kernel bottleneck. Use an end-to-end latency breakdown and controlled workload.

**Follow-up:** What observation would make you abandon the kernel hypothesis?

#### OPT-02 — Quantization operating point

**P1 · Original practice · Evidence/reference: E04,P01**

Compare weight, activation and KV quantization for short prompts versus long-context decode.

**Answer checkpoints:** State which bytes/compute each changes and evaluate quality on relevant slices. Kernel availability, conversion overhead and batch shape affect speed; memory savings alone are insufficient.

**Follow-up:** How do you avoid combining compression and quality results from different experiments?

#### OPT-03 — Speculation and parallelism

**P1 · Original practice · Evidence/reference: E02,E14**

Why can high draft acceptance fail to improve latency, and why can larger tensor parallelism make a small-batch request slower?

**Answer checkpoints:** Account for total draft/verify cost and interconnect/synchronization. Measure comparable token work and request latency; compare against a non-speculative baseline at the same load.

**Follow-up:** When would an extra replica beat increasing tensor parallelism?

#### OPT-04 — Choose an engine experimentally

**P0 · Original practice · Evidence/reference: E13,E15**

How would you select vLLM or SGLang for a mixed workload of short chats, repeated system prefixes and long documents?

**Answer checkpoints:** Build a feature/compatibility shortlist, then matched tests over request mix and SLO-constrained goodput. Pin versions, hardware, model, dtype, sampling and cache warmness. No universal winner assumed.

**Follow-up:** How do you report a workload where each engine wins a different regime?

#### ECODE-01 — Measure streaming events

**P0 · Original practice · Evidence/reference: P01**

Implement first_positive_event(events), last_positive_event(events), then TTFT/E2E from supplied start and event times. Each event has a nonnegative token count.

**Answer checkpoints:** Use MC-06 contract in phone research. Unit-check tokenless trailers, empty streams and multi-token chunks. Do not label event gaps as per-token intervals inside a chunk.

**Follow-up:** Why can an extra call to the clock break a metric identity?

#### ECODE-02 — Accumulate queue waits

**P0 · Original practice · Evidence/reference: P02**

Implement QueueWait.start(t), admit(t), and reset(). start opens an interval; admit closes it. Reject repeated start while open, repeated admit while closed and decreasing timestamps.

**Answer checkpoints:** Use an injected clock/input times. Trace start(1), admit(4), start(8), admit(10) => total 5; reset clears sum/state. Define serialization before adding it.

**Follow-up:** What changes if completion or cancellation occurs while waiting?

#### ECODE-03 — Budget one scheduler iteration

**P0 · Original practice · Evidence/reference: E02**

Implement choose_batch(active_decode_ids, waiting_prefills, budget). Serve one token per active decode first, then FCFS prefill chunks; reject budget below decode count. Return allocations and new remaining prefill counts.

**Answer checkpoints:** Start with lists/dicts, a pure function and the VLLM-02 example. Do not mutate input; test budget zero with no decodes, exact fit, partial prompt and no waiting work.

**Follow-up:** Add a finite cache-capacity admission check as a separate function.

#### ECODE-04 — Allocate KV blocks

**P0 · Original practice · Evidence/reference: E04**

Implement blocks_needed(token_count, block_size), then a fixed pool with allocate(n) and release(ids). Allocation failure leaves the pool unchanged; reject double release.

**Answer checkpoints:** First test ceil division at 0,1,16,17. Then capacity exhaustion, rollback and reuse. Extend to refcounts only after basic invariants hold.

**Follow-up:** How do shared blocks change cancellation cleanup?

#### ECODE-05 — Find reusable token prefixes

**P0 · Original practice · Evidence/reference: E08**

First implement common_prefix_length(a,b) using plain Python. Then search a list of cached token sequences for the longest prefix match; ties use insertion order.

**Answer checkpoints:** Test empty sequences, total mismatch, exact match and divergence after several tokens. This linear baseline is sufficient before a trie/radix optimization. No fuzzy text matching.

**Follow-up:** What is the cost, and when is a radix structure worth its complexity?

#### ECODE-06 — Route with cache and queue cost

**P0 · Original practice · Evidence/reference: E10**

Given workers with queue_ms and reusable_prefix_tokens, choose minimum queue_ms + (prompt_len-hit_tokens)*ms_per_uncached_token. Reject impossible hit counts; tie by worker ID.

**Answer checkpoints:** Use supplied synthetic costs; test that an overloaded cache-hot worker can lose to a cooler worker. This is an educational heuristic, not the SGLang production routing algorithm.

**Follow-up:** What runtime measurements would improve this model?

#### ECASE-01 — Long prompts stall chat

**P0 · Original practice · Evidence/reference: E02,E11**

Synthetic observation: short-chat p95 token interval doubles only when 32k-token prompts arrive. Present a diagnosis and two controlled experiments.

**Answer checkpoints:** Inspect iteration mix and scheduling; compare chunk budgets or isolation while preserving request mix and offered load. Report TTFT and token intervals together.

**Follow-up:** How would you distinguish GPU interference from queue-only delay?

#### ECASE-02 — Cache hits rise but goodput falls

**P0 · Original practice · Evidence/reference: E05,E10**

Synthetic observation: cache hits rise after routing changes, but SLO-compliant throughput falls. Explain three distinct causes.

**Answer checkpoints:** Inspect skew/hot workers, longer waits, memory pressure/eviction and useful tokens saved. Hit percentage and saved compute are different quantities.

**Follow-up:** What would you log per request and per worker?

#### ECASE-03 — Cache memory settings appear contradictory

**P0 · Original practice · Evidence/reference: E02,E11**

vLLM advice suggests increasing memory utilization for preemption; SGLang advice may suggest decreasing its static fraction for an OOM. Reconcile them.

**Answer checkpoints:** The flags govern resource budgets whose pressure can occur in different places. Cache-capacity exhaustion and total allocation/activation OOM require different responses. Identify engine version and failing phase.

**Follow-up:** How would you demonstrate the limiting budget experimentally?

#### ECASE-04 — Disaggregation hurts short requests

**P0 · Original practice · Evidence/reference: E12**

Prefill and decode pools increase hardware use but short-request latency gets worse. What could dominate?

**Answer checkpoints:** Transfer, routing, synchronization, imbalance and extra queue boundaries. Establish whether the workload has enough prefill interference to justify separation.

**Follow-up:** Estimate transfer time as bytes/bandwidth plus fixed overhead.

#### ECASE-05 — Microkernel win disappears

**P0 · Original practice · Evidence/reference: E07,E13**

A new attention kernel is 20% faster in isolation, but the service barely changes. What do you measure next?

**Answer checkpoints:** Determine fraction of critical-path time, workload coverage and new overhead. Apply Amdahl-style reasoning and inspect changed batching/caching.

**Follow-up:** Which two baselines distinguish a kernel regression from a harness artifact?

#### ECASE-06 — Cancellation leaks capacity

**P0 · Original practice · Evidence/reference: Original lifecycle exercise**

Requests disconnect; completed-request count looks healthy but free cache blocks steadily fall. Trace likely ownership errors.

**Answer checkpoints:** Follow request ID, cancellation propagation, in-flight work and last-reference release. Avoid freeing buffers still used by a GPU operation. Test retries and double cleanup.

**Follow-up:** Design a deterministic test without requiring a real GPU.

#### PROJ-01 — vLLM timing contribution

**P0 · Original practice · Evidence/reference: P01**

Explain the timing invariant your benchmark fix protected, the exact event boundaries, and how a regression test makes an extra clock read visible.

**Answer checkpoints:** Use recorded PR evidence. Identify tokenless trailers and endpoint behavior. Describe benchmark correctness; do not assert engine acceleration.

**Follow-up:** Why are scripted clocks useful but insufficient for every integration question?

#### PROJ-02 — SGLang retraction contribution

**P0 · Original practice · Evidence/reference: P02**

Explain how a first-forward timestamp minus a later queue-entry timestamp could become negative, and why clamping the number loses information.

**Answer checkpoints:** Trace multiple admissions and accumulation, serialization/reset and the existing sentinel in the merged patch. Separate known caller-path limitation from tested behavior.

**Follow-up:** What would you change in the test strategy based on the later PD-path report?

#### PROJ-03 — Triton tuning contribution

**P0 · Original practice · Evidence/reference: P01**

Choose one actual winning shape and one losing regime. Explain mapping, precision, baseline, bottleneck hypothesis and next experiment.

**Answer checkpoints:** Use project audit and verified personal knowledge. Keep INT2 compression and INT4 quality experiments separate; state unreproduced measurements as reported artifacts.

**Follow-up:** What evidence would show your split strategy pays for its reduction overhead?

#### PROJ-04 — Observability and resource judgment

**P0 · Original practice · Evidence/reference: P01**

Explain either completion output logging or retry-budget clarification: requirement, code path, compatibility, tests and scope.

**Answer checkpoints:** Use the final merged behavior in the audit. Logging is not a proven speedup; retry-budget work preserved restrictive accounting rather than creating a new budget mechanism.

**Follow-up:** What did review change about your initial approach?

#### Applied engine comparison — avoid slogans

| Dimension | What to establish before comparing |
|---|---|
| Request processing | Pin the version and trace frontend, scheduling and worker boundaries. |
| Cache management | Understand vLLM's block-based KV/prefix mechanisms and SGLang's radix reuse; both cover more than a single headline technique. |
| Scheduling | Identify token budgets, admission, mixed-phase handling and retraction/preemption behavior for the deployed configuration. |
| Optimization | Match model/hardware/kernel backend, dtype, graph/compile mode and sampling semantics. |
| Evaluation | Same offered load, length distribution and quality target; report cold/warm and percentile metrics. |

No engine is designated universally faster. Prefix caching, paging, FlashAttention and continuous batching address related but distinct costs; none substitutes for all the others.

#### Current progress and maintenance

No independent answers or timed engine exercises have been evaluated yet. [Engine attempt log](#material-10) starts unattempted. Preserve IDs and source confidence as research improves. Existing broad CODE-03/07/08/15/16 and DES-01/02/03/07 remain useful later-stage extensions; do not duplicate them as newly reported questions.

---

<a id="material-04"></a>

## 04. Inference-engine research and resources

**Source:** [inference-engines-research.md](inference-engines-research.md) · **Section:** current

### Inference-engine interview research — evidence and study resources

**Researched October 28, 2026.** Focus: inference, optimization and vLLM/SGLang. Companion to [32 targeted questions](#material-03). Exact target remains Amazon MLE II AWS Inference Optimization, live interview November 12. Interview questions from other companies support preparation, not predictions about Amazon.

#### What interview accounts actually support

1. **NVIDIA inference phone screen — specific firsthand account.** [LeetCode original](https://leetcode.com/discuss/post/6809037/), Sukanya Saha, published June 4, 2025. Role Deep Learning Software Engineer—Inference; hiring-manager phone screen, exact seniority/location/interview date unspecified. Reports CUDA kernel/optimization challenges, model-serving/vLLM follow-ups, exact project contributions, and tree serialization coding. This is the same source already in the domain ledger, not a new independent corroboration. It supports project defense plus systems understanding; it provides no precise vLLM scheduler coding prompt.
2. **Fireworks applied ML — adjacent reported themes.** [Glassdoor reviews](https://www.glassdoor.com/Interview/Fireworks-AI-Interview-Questions-E9514416.htm): Jul 31, 2026 Applied MLE account discusses RAG optimizations and TTFT; Aug 17 review describes an Aug 2026 AI Engineer interview in New York with evaluation/model-selection/latency questions. Previous search-visible review extracts are retained; current direct page retrieval did not expose equivalent full review bodies. No exact kernel-engineer attribution.
3. **Anthropic SWE onsite — anonymous specific account.** [Reddit](https://www.reddit.com/r/Technical_Interview/comments/1wswnys/sweanthropic_anthropic_onsite_interview_experience/), recent October 2026, actual interview date/level/location unconfirmed. Describes inference design review, batching/rate limits and fixed-capacity scheduling for one-unit versus eight-unit models. Same source already recorded in the domain ledger. Supports scheduling/capacity follow-ups.
4. **Anthropic Fellowship OA — additional low-confidence lead.** [Reddit InterviewDB](https://www.reddit.com/r/InterviewDB/comments/1vm1ooz/anthropic_fellow_program_assessment_questions/), page says two months ago as of access, exact posting/interview date unclear; November cohort mentioned, no independently verified year. Account describes a supplied vLLM-like codebase involving cache/prefill and undocumented APIs. Author is a question-aggregation account; [Karavine repost](https://www.reddit.com/r/Karavine/comments/1w3lpf0/anthropic_fellowship_oa_interview_experience_vllm/) promotes a paid pack. Treat as a low-confidence possibly overlapping cluster, not two independent confirmations. This is an OA for a different program, not evidence Amazon will use a repository exercise.

**Evidence boundary:** no attributable exact SGLang interview transcript or reliable vLLM/SGLang question-frequency data was found. Searches covered NVIDIA, Together AI, Fireworks, Anthropic and general inference-engineer reports in LeetCode, Reddit, Glassdoor-indexed pages and Chinese interview-note indexes. Commercial guides and LinkedIn “asked at NVIDIA” content often lack candidate/date/round provenance. Do not promote them to verified question reports.

A Deep-ML inference path sometimes labels papers, role postings or tutorial sites as “reportedly asked at.” Those labels alone are not interview evidence. Use its coding exercises as educational practice; verify employer claims against an original candidate account. Source duplication and web freshness do not establish repeated interview frequency.

#### Primary references for engine practice

Read the mechanism, then close the page and answer the associated bank question. No need to install or run a full server before understanding the request lifecycle. Current docs were checked October 28; original papers/blogs are explicitly dated.

| ID | Primary source | What to use it for / limits |
|---|---|---|
| E01 | [vLLM V1 architecture announcement](https://vllm.ai/blog/2025-01-27-v1-alpha-release), Jan 27, 2025 | Execution-loop/frontend changes, token scheduling, compilation/graphs. Historical V1 introduction, not a current code-layout guarantee. |
| E02 | [vLLM optimization and tuning](https://docs.vllm.ai/en/latest/configuration/optimization/), accessed Oct 28 | Current V1 preemption and chunked-prefill discussion; distinguish recompute/cache pressure from old V0 swapping descriptions. Tune against measured workloads, not magic defaults. |
| E03 | [vLLM production metrics](https://docs.vllm.ai/en/latest/usage/metrics/) | Queue/inference/prefill/decode timing and metric families. Verify exact emission semantics and enabled families for the deployed version. |
| E04 | [PagedAttention/vLLM paper](https://arxiv.org/abs/2309.06180), 2023 | Block mapping, fragmentation and cache sharing. Toy allocator exercises are ours; not literal APIs. |
| E05 | [vLLM automatic prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) | Prefix reuse and workload-dependent benefit. Prefix cache reuse and response caching are distinct. |
| E07 | [vLLM profiling example](https://docs.vllm.ai/en/latest/examples/features/profiling/) | How to separate and inspect execution regions. Use a version-appropriate profiler and retain cold/warm distinction. |
| E08 | [SGLang/RadixAttention paper](https://arxiv.org/abs/2312.07104), 2023–2024 | Prefix-tree reuse mechanisms and structured-program execution; current framework is broader than the original system description. |
| E09 | [SGLang radix eviction policies](https://docs.sglang.io/docs/advanced_features/radix_eviction_policy) | Workload-dependent recency/frequency choices. Original exercise adds explicit ownership/pinning constraints; do not infer full allocator implementation from policy names. |
| E10 | [SGLang v0.4 engineering post](https://www.lmsys.org/blog/2024-12-04-sglang-v0-4/), Dec 4, 2024 | CPU/GPU overlap and cache-aware routing rationale. Published speedups are workload-specific historical results; no claim those versions are today's fastest. |
| E11 | [SGLang hyperparameter tuning](https://docs.sglang.io/docs/advanced_features/hyperparameter_tuning) | Weights/cache versus activation/graph memory; diagnose OOM phase before changing limits. Defaults/flags can change. |
| E12 | [SGLang PD disaggregation](https://docs.sglang.io/docs/advanced_features/pd_disaggregation) | KV transfer and heterogeneous-layout constraints. Specific backend support must be checked against deployed versions. |
| E13 | [SGLang benchmark and profiling](https://docs.sglang.io/docs/developer_guide/benchmark_and_profiling) | Serving measurement and trace-based diagnosis. Our benchmark scenarios supply synthetic data, not reported measurements. |
| E14 | [Exact speculative decoding paper](https://arxiv.org/abs/2211.17192), 2022–2023 | Draft/verify correctness and cost reasoning. Modern variants require their own assumptions. |
| E15 | [Current SGLang overview](https://docs.sglang.io/) and [documentation index](https://docs.sglang.io/llms.txt) | Current feature navigation. The old docs.sglang.ai hostname redirected to docs.sglang.io during this research. |
| P01 | [Local project/PR audit](#material-07) | vLLM timing/logging/resource-budget scope and Triton experiment limits. Evidence audit, not fresh experiment reproduction. |
| P02 | [SGLang contribution section of the same audit](#material-07) | Queue re-entry accumulation, serialization/reset and recorded PD caller-path caveat. No fresh upstream-resolution verification performed. |

Some SGLang `.md` links from the official index returned unsupported-content-type errors in the web reader. Their corresponding HTML pages were successfully opened above. No unavailable content was reconstructed.

#### Learning order — make code understandable

**First:** explain prefill/decode with a two-token prompt and one generation step. Draw Q/K/V shapes and what remains in the cache.

**Next:** work through ECODE-01/02/03 using lists, dictionaries and explicit timestamps. These teach engine state changes without NumPy broadcasting. Then do ECODE-04/05 for cache ownership/prefix matching. Finally add a model computation using the existing CODE-02/03 attention references.

**Read and discuss:** E01 and E02 for vLLM; E08 and E10 for SGLang; then E13 for experimental practice. You should be able to draw the mechanism and name a workload that benefits and one that may not.

**Resources to practice implementation:** [Deep-ML K-means](https://www.deep-ml.com/problems/17), [softmax](https://www.deep-ml.com/problems/23), [simple self-attention](https://www.deep-ml.com/problems/955), and [multi-head attention](https://www.deep-ml.com/problems/94). Read each contract: the simplified self-attention task is not a full causal decoder implementation. Employer labels on educational pages are not used as evidence here.

#### Research update rules

Preserve this bank's IDs, attempt history and source uncertainty. Add dated original reports when available; do not repackage the same NVIDIA report as several independent signals. Prefer pinned code/version references for implementation claims. Keep confirmed interview constraints above speculative research. Use actual practice errors to narrow revision; no unobserved skill/readiness claims.

Research outcome: existing evidence reinforces project ownership, latency/evaluation reasoning and scheduling depth. The main additions are a low-confidence repository-exercise lead, current engine-specific references, 32 targeted prompts and a smaller-step coding sequence. No new exact Amazon team question list was found.


#### Research refresh — October 31, 2026

Rechecked inference-engine interview searches and reopened the original NVIDIA screen account (https://leetcode.com/discuss/post/6809037/). This remains one June 2025 report, not fresh independent corroboration. No new original vLLM/SGLang question account met the evidence threshold. Candidate preparation requests, educational question lists, promotional reposts and papers mislabeled as interview evidence were not promoted.

Revalidated the existing mechanisms against the current vLLM tuning page (https://docs.vllm.ai/en/latest/configuration/optimization/) and SGLang tuning page (https://docs.sglang.io/docs/advanced_features/hyperparameter_tuning). vLLM's current V1 guidance still describes decode-prioritized chunked prefill and default recomputation preemption; SGLang still distinguishes static weights/cache allocation from graph/activation headroom. No plan-changing technical correction was identified. Keep implementations version-aware and measure workload tradeoffs. All 32 IDs and the small-function learning sequence retained; no attempt outcomes added.

---

<a id="material-05"></a>

## 05. ML, attention and inference question bank

**Source:** [ml-inference-engineering-question-bank.md](ml-inference-engineering-question-bank.md) · **Section:** current

### ML and LLM inference engineering — cross-company question bank

**Engine-specific depth:** [vLLM/SGLang focus bank](#material-03), with current sources and small coding stages.

> **CURRENT STAGE — November 12, 2026, 2 PM EST (UTC−5):** 60-minute phone interview with Sathishkumar Sivashanmugam; live coding confirmed, recruiter says ML and LeetCode preparation. OA waived after a prior pass. Use the [current study plan](#material-01) and [AWS research supplement](#material-02). Earlier OA-first schedules below are historical.

**Current daily schedule:** [Combined two-week study plan](#material-22). This supersedes earlier daily sequencing; question IDs remain unchanged.

**Researched:** October 28, 2026. **Audience:** mid-level ML/inference engineer, with optional deeper systems follow-ups. **Scope:** transformers, attention, serving, GPU kernels, and practical ML engineering across relevant AI companies. This is separate from the [Amazon OA bank](#material-19); do not treat domain-loop questions as confirmed OA content.

#### Evidence and use

There are **72 original practice exercises** below: 24 conceptual, 16 coding, 12 system design, 12 case studies and 8 ML-engineering exercises. Eight additional reported prompts/themes appear first. The original exercises include concrete requirements and answer checkpoints; they are not claimed verbatim interview questions.

- **Reported:** public candidate account, with company/round/date and limitations. A report is not independent confirmation that the company uses it today.
- **Original practice:** our prompt, informed by primary papers/documentation or an explicitly labeled reported theme. No company attribution is implied.
- **P0/P1:** training priority, not reported frequency. P0 targets the user's inference-optimization focus; P1 adds breadth/depth.

[Source ledger](#material-06) distinguishes firsthand accounts, promotional reposts and primary engineering references. Source IDs on each prompt resolve there. [Attempt tracker](#material-11) starts unattempted; the bank does not assert candidate readiness.

#### What has actually been reported

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

#### Suggested starting sequence

1. CON-01–08: shapes, masks, KV arithmetic, RoPE and online attention.
2. CODE-01–05: write correct CPU/PyTorch references before GPU optimization.
3. CON-17–24, then CODE-09–11/13/15: hardware reasoning, kernels and measurement.
4. CON-09–16 and DES-01–03/05/07: serving tradeoffs and failure handling.
5. CASE-01/02/06/07/09/12 and ML-01/02/04/08: diagnose evidence, quantify claims and protect correctness.

Until the OA is complete, use this as a supplementary domain track rather than replacing timed OA practice. No GPU is required for conceptual work, design, CPU references or numerical exercises. Actual kernel correctness/performance claims require a compatible device; no GPU benchmarks have been run as part of building this bank.

#### Practice rubric

Score 0–2 each for correctness, explicit assumptions, implementation/mechanism, validation/evidence, and tradeoff reasoning (10 total). This is our feedback rubric, not a company pass threshold. Conceptual answers should include a small example or derivation. Coding requires tests and complexity. Design requires numbers, a bottleneck and a failure path. Cases require a falsifiable hypothesis and the next measurement.

For your own project answers, distinguish authored code, integration, tests, measurements and team decisions. Trace claims to your existing resume/evidence audit; do not adopt synthetic case-study numbers as your results.

#### Conceptual deep dives

##### CON-01 — Attention shapes

**P0 · Conceptual · 8–12 min · Original practice · Sources: T01**

Given X with shape [B,T,D], derive Q, K, V, attention-score and output shapes for H heads. Where does the 1/sqrt(d_head) factor come from?

**Answer checkpoints:** Track projections and head reshaping; scaling controls dot-product variance under standard assumptions. Explain which axis softmax normalizes.

##### CON-02 — Causal and padding masks

**P0 · Conceptual · 8–12 min · Original practice · Sources: T01,T06**

Why do we need both causal and padding masks? What changes when decoding a single token against a cached prefix?

**Answer checkpoints:** Use absolute query/key positions; unequal query and key lengths need correct causal alignment. Define fully masked-row behavior explicitly.

##### CON-03 — GQA versus MHA and MQA

**P0 · Conceptual · 8–12 min · Original practice · Sources: T02**

Keep 32 query heads but use 8 KV heads. What changes in model weights, cache memory, and head mapping? Can we just drop heads from a checkpoint?

**Answer checkpoints:** Four query heads share each KV group. Savings concern KV, not every activation or parameter. Architecture/checkpoint conversion can affect quality.

##### CON-04 — KV-cache arithmetic

**P0 · Conceptual · 8–12 min · Original practice · Sources: T02,T04**

For B=4, T=8192, L=32, Hkv=8, d=128 and two-byte cache elements, derive total KV storage without tensor parallelism.

**Answer checkpoints:** 2*B*T*L*Hkv*d*bytes = 4 GiB. Add allocator overhead, weights, workspace and temporary buffers separately; replication/sharding changes per-device memory.

##### CON-05 — RoPE during cached decoding

**P0 · Conceptual · 8–12 min · Original practice · Sources: T03**

How do rotations encode relative position? What breaks if you rotate a cached key twice or restart position IDs for each decode step?

**Answer checkpoints:** Track absolute positions and consistent rotation convention; explain the relative-angle dot product. Position encoding is not equivalent to a causal mask.

##### CON-06 — FlashAttention mechanism

**P0 · Conceptual · 8–12 min · Original practice · Sources: T06**

Explain how exact dense attention avoids materializing the full score/probability matrix. Does this make dense attention linear-time?

**Answer checkpoints:** Tiling and online normalization reduce memory traffic/storage; dense attention arithmetic remains quadratic in sequence length. Exact mathematical formulation does not mean bitwise-identical floating point.

##### CON-07 — Online softmax derivation

**P0 · Conceptual · 8–12 min · Original practice · Sources: T06**

Maintain a running maximum m, exponential sum l, and unnormalized weighted value accumulator o. Derive updates when a new score/value tile arrives.

**Answer checkpoints:** m_new=max(m,max(tile)); rescale old l and o by exp(m-m_new), add new exp(score-m_new) contributions, normalize o/l at the end. Handle initialization and all-masked tiles.

##### CON-08 — Prefill versus decode

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04,T09**

Explain why a large prefill can benefit from GEMM throughput while small-batch decode can be bandwidth-limited. When does that rule stop being useful?

**Answer checkpoints:** Reason from shapes, bytes and reuse; long-context cache reads, large batches, communication and launch overhead can change the bottleneck. Measure instead of labeling every decode memory-bound.

##### CON-09 — Serving metrics

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04,T10**

Define TTFT, inter-token latency, time per output token, request throughput, output-token throughput and goodput. How can a system improve one while hurting another?

**Answer checkpoints:** State timestamp boundaries and warm/cold treatment. Separate queueing, prefill and decode; goodput counts work meeting an explicit SLO. Avoid averaging away tail behavior.

##### CON-10 — Continuous batching

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04**

Contrast static and iteration-level batching. What happens when one request ends, another arrives, and a third runs out of KV capacity?

**Answer checkpoints:** Discuss admission, removal, token budgets, preemption/recomputation and fairness. Scheduling policy and cache management are linked.

##### CON-11 — Paged cache versus prefix cache

**P0 · Conceptual · 8–12 min · Original practice · Sources: T04,T05**

What different problems do paging and shared-prefix caching solve? What is copy-on-write needed for?

**Answer checkpoints:** Paging manages allocation/fragmentation; prefix reuse avoids repeated work/storage for matching prefixes. Sharing mutable tails requires care; neither guarantees a hit on arbitrary similar text.

##### CON-12 — RadixAttention deep dive

**P0 · Conceptual · 8–12 min · Original practice · Sources: T05**

What information does a radix prefix structure retain? Explain reuse and eviction while requests still reference a prefix.

**Answer checkpoints:** Walk token-prefix matching, reference ownership and reclaimable leaves. Do not claim every current SGLang behavior follows the original paper; identify a version before implementation-specific answers.

##### CON-13 — Speculative decoding correctness

**P1 · Conceptual · 8–12 min · Original practice · Sources: T07**

Why is accepting a draft token only when it equals the target argmax not a general sampling algorithm? Derive the acceptance test for distributions p and q.

**Answer checkpoints:** For the classical exact method use min(1,p(x)/q(x)); rejection samples from normalized positive p-q. Explain support, draft cost and target verification.

##### CON-14 — Quantization tradeoffs

**P1 · Conceptual · 8–12 min · Original practice · Sources: T08**

Compare weight-only, weight+activation and KV-cache quantization. Which storage or bandwidth cost does each attack?

**Answer checkpoints:** Discuss scales, group/channel granularity, calibration distribution and actual kernel support. Smaller tensors do not guarantee faster end-to-end serving.

##### CON-15 — Parallelism choice

**P1 · Conceptual · 8–12 min · Original practice · Sources: T09**

Contrast tensor, pipeline, data and expert parallelism for serving. What would make doubling tensor parallelism slower?

**Answer checkpoints:** Identify what is sharded/replicated and where communication enters; topology, small messages, batch size and synchronization matter.

##### CON-16 — MoE inference

**P1 · Conceptual · 8–12 min · Original practice · Sources: T09**

Why can a model with fewer active parameters still have poor latency? How do routing skew and all-to-all traffic affect it?

**Answer checkpoints:** Separate total weights from active compute; account for dispatch/combine, expert imbalance and small expert batches. Explain capacity and dropped/rerouted-token semantics.

##### CON-17 — GPU execution and memory

**P0 · Conceptual · 8–12 min · Original practice · Sources: T11**

Map grid, block, warp and thread onto the memory hierarchy. Explain coalescing versus shared-memory bank conflicts.

**Answer checkpoints:** Distinguish address patterns, access granularity and memory spaces; state hardware assumptions. Coalesced global loads do not prove conflict-free shared accesses.

##### CON-18 — Roofline reasoning

**P0 · Conceptual · 8–12 min · Original practice · Sources: T12**

A kernel does 2 GFLOP and transfers 1 GB on a hypothetical GPU with 100 TFLOP/s and 1 TB/s. Estimate a lower bound.

**Answer checkpoints:** Compute bound 20 microseconds, memory bound 1 millisecond: max is 1 ms assuming decimal units and ideal execution. It is a bound, not a measured prediction.

##### CON-19 — Occupancy and registers

**P0 · Conceptual · 8–12 min · Original practice · Sources: T11,T12**

Why might higher occupancy be slower? What evidence distinguishes latency hiding from register spilling?

**Answer checkpoints:** Trade register/shared-memory use against active work; inspect spills, stalls and throughput. Occupancy alone is not the objective.

##### CON-20 — Fusion decision

**P0 · Conceptual · 8–12 min · Original practice · Sources: T13**

When is fusing residual addition, normalization and activation helpful, and when might splitting win?

**Answer checkpoints:** Estimate removed launches/intermediates versus register pressure, reuse and synchronization costs. Check supported shapes and numerical behavior.

##### CON-21 — Triton tiling

**P0 · Conceptual · 8–12 min · Original practice · Sources: T14**

How would you choose BLOCK_M, BLOCK_N, BLOCK_K, warps and stages for a matrix multiplication family?

**Answer checkpoints:** Start with shapes/dtype/device constraints, then tune a bounded space and inspect resource use. Include tails and strides; one best tile need not generalize.

##### CON-22 — JIT versus precompiled specialization

**P0 · Conceptual · 8–12 min · Original practice · Sources: T13,T14**

Design a precompiled Triton kernel catalog for known shape families. Which keys must dispatch consider, and what happens on a miss?

**Answer checkpoints:** Include target architecture, dtype/layout, shape constraints and compiler/build identity; bound variant growth, validate artifacts, and provide a correct fallback. Precompilation removes compilation cost, not inherently steady-state arithmetic.

##### CON-23 — Numerical correctness

**P0 · Conceptual · 8–12 min · Original practice · Sources: T15**

Why can a fused reduction disagree with a framework reference? Define a validation strategy more useful than exact equality.

**Answer checkpoints:** Explain accumulation precision, ordering, error tolerance and extreme values. Use a high-precision reference where appropriate and evaluate model quality separately.

##### CON-24 — Profiling method

**P0 · Conceptual · 8–12 min · Original practice · Sources: T12**

A kernel looks slow. What do you measure before changing code? Which questions belong to a timeline and which to kernel counters?

**Answer checkpoints:** First isolate launch gaps, synchronization and transfers; then inspect dominant kernels and relevant counters. Control warmup and instrumentation effects; profiler overhead can perturb timings.

#### Coding exercises

##### CODE-01 — Stable masked softmax

**P0 · Coding · 35–60 min · Original practice · Sources: T13**

Implement softmax(x, mask) over the last axis in NumPy/PyTorch primitives; forbidden: calling a built-in softmax. For this exercise a fully masked row returns zeros.

**Answer checkpoints:** Test huge logits, equal logits, one valid entry, all masked entries and noncontiguous input. Subtract the maximum and avoid invalid all-masked arithmetic.

##### CODE-02 — Causal attention reference

**P0 · Coding · 35–60 min · Original practice · Sources: T01**

Implement attention(Q,K,V) for [B,H,T,D] tensors with explicit causal and padding masks; no scaled_dot_product_attention call. Return [B,H,T,Dv].

**Answer checkpoints:** Compare to a trusted reference; vary head/value dimensions, padding and dtype. State scale and dropout policy. Test that changing a future value cannot change an earlier output.

##### CODE-03 — Decode with a KV cache

**P0 · Coding · 35–60 min · Original practice · Sources: T04**

Implement a one-token decode step that appends K/V and attends over the valid prefix. Cache capacity and valid length are explicit inputs; reject overflow.

**Answer checkpoints:** Cached results must match full recomputation with dropout disabled and consistent positions. Test capacity boundary, several steps and independent batch entries.

##### CODE-04 — GQA attention mapping

**P0 · Coding · 35–60 min · Original practice · Sources: T02**

Extend the reference to Hq query heads and Hkv key/value heads where Hq is divisible by Hkv, without permanently duplicating the KV cache.

**Answer checkpoints:** Check Hq=Hkv, Hkv=1 and intermediate grouping against a repeat-based reference; verify output shapes and head mapping.

##### CODE-05 — RoPE implementation

**P0 · Coding · 35–60 min · Original practice · Sources: T03**

Rotate even-dimensional query/key vectors using supplied positions and inverse frequencies; choose and document adjacent-pair layout.

**Answer checkpoints:** Position zero is identity; norms are preserved within tolerance; compare full-sequence and cached positions. Reject odd dimensions.

##### CODE-06 — Top-p sampler

**P1 · Coding · 35–60 min · Original practice · Sources: Original algorithm exercise**

Given finite logits, temperature>0, p in (0,1], and a seeded RNG, implement nucleus sampling; keep the smallest sorted prefix whose mass reaches p.

**Answer checkpoints:** Keep at least one token, renormalize retained mass, test p=1, peaked/uniform distributions and deterministic sorting ties. Specify temperature=0 separately as greedy mode.

##### CODE-07 — Tiny continuous-batch scheduler

**P1 · Coding · 35–60 min · Original practice · Sources: T04**

Implement a deterministic simulator. Each request has arrival tick, remaining prefill tokens and decode tokens; each tick has a token budget and active-sequence limit.

**Answer checkpoints:** Declare prefill/decode accounting, deterministic tie breaking, admission and completion rules. Test idle periods, cancellations, zero-length phases and a starvation bound. This is a simulator, not vLLM internals.

##### CODE-08 — Paged block allocator

**P1 · Coding · 35–60 min · Original practice · Sources: T04**

Implement allocate, retain and release for fixed-size KV blocks; request block tables map logical blocks to physical IDs. Refcounts are explicit.

**Answer checkpoints:** No double allocation, no negative references, freed blocks reusable, shared blocks remain live until last owner releases. Define failure atomicity and zero-token behavior.

##### CODE-09 — Row softmax in Triton

**P0 · Coding · 35–60 min · Original practice · Sources: T13**

Write a row-wise stable softmax kernel for rows fitting on-chip, with a mask for padded lanes. Support widths 1,127,128,129 and 1025.

**Answer checkpoints:** Use a framework reference, warm benchmarks and dtype-specific tolerances; separate compile time. Include a fallback for unsupported row sizes.

##### CODE-10 — RMSNorm kernel

**P0 · Coding · 35–60 min · Original practice · Sources: T15**

Implement y=x*rsqrt(mean(x*x)+eps)*weight along the final dimension, using FP32 reduction for low-precision input.

**Answer checkpoints:** Test non-power-of-two widths, all-zero and large-magnitude input, epsilon semantics and output dtype. Compare separate versus fused residual variants only after correctness.

##### CODE-11 — Tiled matrix multiplication

**P0 · Coding · 35–60 min · Original practice · Sources: T14**

Implement C=A@B in Triton with explicit strides and tail masks. Start FP16 input/FP32 accumulation; no cuBLAS call inside your implementation.

**Answer checkpoints:** Test rectangular and odd dimensions and transposed views; benchmark against a library baseline. Explain tile reuse before tuning.

##### CODE-12 — Transpose and coalescing

**P1 · Coding · 35–60 min · Original practice · Sources: T11**

Write a CUDA or Triton transpose for a large rectangular matrix; compare naive and tiled strategies.

**Answer checkpoints:** Check non-square tails, exact indexing and alias restrictions. Explain read/write transaction patterns; avoid claiming a faster result without device measurements.

##### CODE-13 — Fused residual and activation

**P0 · Coding · 35–60 min · Original practice · Sources: T13**

Implement y=SiLU(x+bias)+residual, with row-broadcast bias. Preserve stated dtype and strides or reject unsupported layouts.

**Answer checkpoints:** Compare numerical output and bytes moved with separate operators. Test saturation regions and tails. Report both small launch-bound and large bandwidth-sensitive shapes.

##### CODE-14 — Online attention accumulator

**P1 · Coding · 35–60 min · Original practice · Sources: T06**

Implement a CPU reference for tiled online softmax attention using running (m,l,o); do not construct the full score matrix.

**Answer checkpoints:** Match dense attention across tile sizes and adversarial logits. Test masked initial tiles and tail tiles. Explain why averaging independently normalized tile outputs is wrong.

##### CODE-15 — Benchmark harness

**P0 · Coding · 35–60 min · Original practice · Sources: T12,T15**

Implement a harness reporting compile/cold latency separately from warmed median and p95, plus correctness checks and a shape matrix.

**Answer checkpoints:** Synchronize GPU measurement appropriately, preserve raw samples, record device/software/dtype, and reject empty sample sets. Compare equivalent work; avoid timing only enqueue cost.

##### CODE-16 — Prefix-cache lookup

**P1 · Coding · 35–60 min · Original practice · Sources: T05**

Implement longest token-prefix matching with reference counts and an eviction policy that never deletes pinned entries. Use integer token arrays, not raw-text substring matching.

**Answer checkpoints:** Test shared prefixes, diverging suffixes, empty input and pinned-cache exhaustion. Return matched length and ownership handle. Document tenant/model isolation in the cache key.

#### System design

##### DES-01 — Interactive LLM serving

**P0 · System design · 40–50 min · Original practice · Sources: T04**

Design a service for 100 requests/s, median 2k input and 300 output tokens, p95 TTFT<1s and inter-token latency<50ms. GPU throughput is unknown; request measurements instead of guessing fleet size.

**Answer checkpoints:** Separate gateway, queues, scheduler, workers and streaming. Budget KV and throughput, define admission/cancellation, load tests and failure handling.

##### DES-02 — Prefill/decode disaggregation

**P0 · System design · 40–50 min · Original practice · Sources: T10**

Long prompts cause interactive decode stalls. Design separate prefill and decode pools and explain when transfer cost makes it a bad choice.

**Answer checkpoints:** Account for KV transfer volume, routing, backpressure, topology and state ownership. Compare against colocated chunked-prefill baseline.

##### DES-03 — Multi-tenant prefix reuse

**P0 · System design · 40–50 min · Original practice · Sources: T05**

Customers share common system prompts but require isolation. Design cache identity, routing, eviction and accounting.

**Answer checkpoints:** Include model/tokenizer/adapter versions, tenant boundary and token identity. Quantify benefit against memory pressure; cancellation must release ownership.

##### DES-04 — Multi-cluster scheduler

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

Design placement for jobs requesting 1,2,4 or 8 GPUs across two clusters with different interconnects. Include priority, deadlines and gang allocation.

**Answer checkpoints:** Avoid partial gang deadlock and starvation. Define leases, stale-worker detection, retries and topology-aware placement. Inspired by weak report R04; details are ours.

##### DES-05 — Precompiled kernel service

**P0 · System design · 40–50 min · Original practice · Sources: T14**

Build a pipeline that compiles, validates, benchmarks and distributes Triton variants for known production workloads.

**Answer checkpoints:** Artifact keys, reproducibility, correctness gates, shape coverage, versioned rollout and fallback; limit autotuning cost and prevent silently selecting incompatible binaries.

##### DES-06 — Quantized model launch

**P1 · System design · 40–50 min · Original practice · Sources: T08,T16**

Roll out an INT8/INT4 serving variant under a quality floor and cost target. What artifacts, evaluations and rollback conditions are required?

**Answer checkpoints:** Pin calibration and evaluation sets; test workload slices, kernels, latency tails and memory; shadow/canary deployment and versioned rollback.

##### DES-07 — Benchmark platform

**P0 · System design · 40–50 min · Original practice · Sources: T04,T05**

Design fair comparisons among vLLM, SGLang and another engine for a specific workload.

**Answer checkpoints:** Pin model/tokenizer/dtype/device and request distributions; report SLO-constrained goodput, cold/warm costs and quality. Vary concurrency and prompt lengths; preserve reproducible configs.

##### DES-08 — RAG inference path

**P0 · System design · 40–50 min · Original practice · Sources: R02,T16**

Design a document assistant with citations and a strict TTFT budget. Explain retrieval, reranking, context construction and generation tradeoffs.

**Answer checkpoints:** Instrument stage latencies and quality separately; use bounded context, provenance and evaluation by document/query slice. Do not assume a larger model repairs retrieval failure.

##### DES-09 — LoRA serving

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

Serve many tenant adapters over one base model. Design admission, adapter residency and batch formation.

**Answer checkpoints:** Key caches by adapter identity, bound adapter-loading latency, prevent tenant mixups, and compare shared batching versus dedicated pools.

##### DES-10 — Long-running batch inference

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

Process a large offline corpus with restartability and a completion deadline while sharing capacity with online traffic.

**Answer checkpoints:** Durable tasks/checkpoints, idempotent output writes, priority/preemption, token-aware estimates and cost accounting; protect online SLOs.

##### DES-11 — Streaming API failure

**P1 · System design · 40–50 min · Original practice · Sources: Original systems exercise**

A client disconnects after receiving some tokens and retries. Design request identity, cancellation and replay semantics.

**Answer checkpoints:** Separate transport disconnect from computation lifecycle. Define at-most-one active generation if required, bounded replay storage and billing; do not promise identical stochastic continuation without retained state.

##### DES-12 — GPU fleet rollout

**P0 · System design · 40–50 min · Original practice · Sources: T12,T15**

Deploy a new attention kernel to mixed GPU architectures without silently changing outputs or taking down serving.

**Answer checkpoints:** Compatibility matrix, offline differential tests, shadow/canary, per-shape regression gates and fast rollback; watch compilation misses and tail latency.

#### Performance and debugging cases

##### CASE-01 — TTFT regresses after batching

**P0 · Case study · 15–20 min · Original practice · Sources: R02,T04**

Synthetic measurements: p95 TTFT rises from 0.8s to 2.1s; output-token throughput rises 25%; decode interval is unchanged. What do you measure and change?

**Answer checkpoints:** Separate queue delay and prefill duration; inspect admission/window and prompt mix. Throughput improvement alone does not meet the latency SLO. Propose one controlled experiment.

##### CASE-02 — Fusion loses in production

**P0 · Case study · 15–20 min · Original practice · Sources: T12,T13**

A fused kernel wins 30% at width 4096 but loses 20% at 8192. The numbers are hypothetical. Explain plausible mechanisms and a dispatch decision.

**Answer checkpoints:** Inspect registers/spills, occupancy and memory traffic; validate benchmarks and numerical behavior. Gate by measured shape/device regimes rather than declare fusion universally better.

##### CASE-03 — Higher cache hit rate, worse latency

**P0 · Case study · 15–20 min · Original practice · Sources: T05**

Prefix-cache hit rate increases from 40% to 80%, but p99 latency doubles. What could explain it?

**Answer checkpoints:** Check definition of hit rate, saved tokens/work, KV pressure, routing imbalance, eviction and queueing. Cache-hit percentage is not saved compute or end-to-end latency.

##### CASE-04 — Quantization fails one slice

**P1 · Case study · 15–20 min · Original practice · Sources: T08,T15**

Aggregate accuracy is stable after quantization, but long-context extraction loses 8 percentage points. What is your investigation plan?

**Answer checkpoints:** Verify statistical support and preprocessing; isolate weights/activations/cache quantization, calibrate on representative inputs, compare logits/layers and consider selective precision.

##### CASE-05 — Four GPUs do not beat two

**P1 · Case study · 15–20 min · Original practice · Sources: T09**

Tensor-parallel degree doubles from 2 to 4 but median decode latency worsens. Give three falsifiable hypotheses.

**Answer checkpoints:** Communication/topology, smaller GEMMs, or synchronization/placement; profile collectives versus compute and hold batch/context constant. Quantify memory benefit separately.

##### CASE-06 — Impossible benchmark speedup

**P0 · Case study · 15–20 min · Original practice · Sources: T12**

A GPU operation allegedly completes in 0.5 microseconds while the reference takes 100 microseconds. What invalidates the comparison?

**Answer checkpoints:** Check asynchronous timing, warmup, output use, shapes, dtype, graph capture and synchronization; preserve raw samples. Do not reject a result solely because it is surprising.

##### CASE-07 — OOM with apparently free memory

**P0 · Case study · 15–20 min · Original practice · Sources: T04**

The dashboard shows several GB free, yet a long request fails allocation. Walk through diagnosis.

**Answer checkpoints:** Distinguish device memory, engine cache pool, allocator fragmentation, reservation, graph/workspace peaks and concurrent growth. Estimate request KV before changing limits.

##### CASE-08 — Speculation is slower

**P1 · Case study · 15–20 min · Original practice · Sources: T07**

Draft acceptance is high but wall-clock latency worsens. How can that happen?

**Answer checkpoints:** Draft generation, verification cost, batch/context regime, communication and scheduling overhead can exceed saved steps. Measure accepted tokens per total cost, not acceptance alone.

##### CASE-09 — Cold start misses SLO

**P0 · Case study · 15–20 min · Original practice · Sources: T14**

Warm requests are fast; the first request for a shape takes several seconds. Design a remedy and proof.

**Answer checkpoints:** Separate model loading, compilation, autotuning and graph capture. Prewarm or precompile bounded hot variants, retain fallback and measure cold paths explicitly.

##### CASE-10 — Tail shapes are wrong

**P0 · Case study · 15–20 min · Original practice · Sources: T06,T15**

Attention outputs pass tests at lengths 128 and 256 but fail at 129. What do you inspect first?

**Answer checkpoints:** Tail masks, strides, block bounds, causal alignment and uninitialized lanes. Use smallest failing case and differential tests before changing arithmetic.

##### CASE-11 — GPU utilization is low

**P1 · Case study · 15–20 min · Original practice · Sources: T12**

A service has low reported GPU utilization and high end-to-end latency. Would you buy more GPUs?

**Answer checkpoints:** Inspect CPU tokenization, request arrival, batching, copies, launch gaps and synchronization before scaling. Utilization aggregates cannot identify the bottleneck.

##### CASE-12 — Kernel claim versus service gain

**P0 · Case study · 15–20 min · Original practice · Sources: Original quantitative exercise**

Your kernel is 2x faster and originally consumed 20% of request time. Estimate ideal total speedup; explain what makes reality worse.

**Answer checkpoints:** Amdahl bound is 1/(0.8+0.2/2)=1.111x, about 10% latency reduction. Changed overhead, contention or workload mix can reduce it. State sequential-fraction assumptions.

#### ML engineering fundamentals

##### ML-01 — Data leakage

**P0 · ML engineering · 15–30 min · Original practice · Sources: T16**

Validation quality is excellent but live performance is poor. How do you detect duplicates, temporal leakage and label contamination?

**Answer checkpoints:** Audit data lineage and split by deployment unit/time, then test on a genuinely held-out distribution. Distinguish leakage from serving skew.

##### ML-02 — Evaluation design

**P0 · ML engineering · 15–30 min · Original practice · Sources: R02**

Compare two models for text-to-SQL across unseen database schemas. What do you score besides exact-string match?

**Answer checkpoints:** Execution correctness and semantic equivalence, schema-generalization splits, latency/cost and error categories. Handle invalid/unsafe queries in a sandbox; report uncertainty.

##### ML-03 — Distribution shift

**P1 · ML engineering · 15–30 min · Original practice · Sources: T16**

A new customer has different prompt lengths, terminology and language. How do you decide between retrieval changes, prompting, fine-tuning and a different model?

**Answer checkpoints:** Build a representative labeled sample and baseline; localize failure before choosing intervention. Measure quality/latency per slice.

##### ML-04 — Training-serving skew

**P0 · ML engineering · 15–30 min · Original practice · Sources: T16**

Offline embeddings improve retrieval but online quality degrades. Where could the mismatch be?

**Answer checkpoints:** Check preprocessing, model/tokenizer versions, index refresh, normalization and similarity metric. Make artifacts reproducible and compare actual served inputs.

##### ML-05 — Numerical ML debugging

**P1 · ML engineering · 15–30 min · Original practice · Sources: T15**

Loss becomes NaN after moving to lower precision. How do you localize the first invalid tensor and evaluate a fix?

**Answer checkpoints:** Trace a minimal batch, inspect activations/gradients and optimizer state, review overflow/underflow and scaling; compare an appropriate higher-precision run.

##### ML-06 — Cost-quality model selection

**P1 · ML engineering · 15–30 min · Original practice · Sources: Original ML exercise**

A smaller model costs half as much per token but emits longer answers and retries more often. How do you compare it with a larger model?

**Answer checkpoints:** Use cost per successful task under quality and latency constraints, including retries, input/output lengths and failure cost; compare representative workloads.

##### ML-07 — Canary evaluation

**P1 · ML engineering · 15–30 min · Original practice · Sources: T16**

A new model improves a benchmark but customer complaints rise. Design a rollout and investigation strategy.

**Answer checkpoints:** Use baseline comparison, task slices, operational metrics and delayed feedback; preserve rollback and examine whether the benchmark represents customer needs.

##### ML-08 — Loss and perplexity coding

**P0 · ML engineering · 15–30 min · Original practice · Sources: T15**

Implement stable token-level cross entropy and perplexity from logits and target IDs with an ignore mask. No built-in cross-entropy function.

**Answer checkpoints:** Use logsumexp; average over valid tokens only; define no-valid-token behavior. Test extreme logits and padding; compare to a trusted implementation.

#### Mock rounds

- **Transformer coding, 60 minutes:** CODE-02 (35), CON-03/04 (15), test review (10).
- **Kernel engineering, 60 minutes:** CODE-09 (35), CON-18/19 (15), benchmark critique (10). Implement a CPU reference if a compatible GPU is unavailable; do not mark the GPU portion tested.
- **Inference systems, 60 minutes:** DES-01 (40), CASE-01 (15), explicit unknowns (5).
- **Project defense, 45 minutes:** one real Triton/vLLM/SGLang contribution (15), implementation/correctness follow-ups (15), performance attribution and limits (15).

##### Change log

- 2026-10-28: Initial cross-company bank with 72 original exercises and 8 reported prompts/themes. All attempt statuses unattempted. Kept separate from the Amazon OA bank. Company evidence strongest for a specific NVIDIA screen and Fireworks applied-ML themes; exact kernel interview transcripts remain sparse.

---

<a id="material-06"></a>

## 06. Cross-company research sources

**Source:** [ml-inference-engineering-sources.md](ml-inference-engineering-sources.md) · **Section:** current

### Cross-company inference interview research — source ledger

**Accessed:** October 28, 2026. Companion to [the bank](#material-05). Reported questions are evidence of an individual account, not an employer promise or a frequency estimate. Technical references support our original exercises, not claims about what an interviewer asked.

#### Candidate accounts

##### R01 — NVIDIA inference phone screen

[Original LeetCode account](https://leetcode.com/discuss/post/6809037/), author Sukanya Saha, posted **June 4, 2025**. Role: Deep Learning Software Engineer—Inference. Round: first technical phone screen with hiring manager. Actual interview date, location and seniority not specified. Candidate reports CUDA/project ownership and vLLM-serving discussion plus tree serialization coding. Specific and relevant firsthand account; independently unverified and not a full loop. REP-01–03 come from this single account. Do not infer that NVIDIA always asks these questions or that their kernel round was a live CUDA exercise.

##### R02 — Fireworks AI applied-ML interviews

[Glassdoor candidate reviews](https://www.glassdoor.com/Interview/Fireworks-AI-Interview-Questions-E9514416.htm). Search-visible review text was available; directly opening the current page returned its surrounding structure without the same full review bodies. This access limitation is retained.

- **Applied Machine Learning Engineer**, posted **July 31, 2026**: RAG take-home, project/take-home discussion, TTFT optimization. Exact interview date/location unstated; onsite still pending in the account.
- **AI Engineer, New York**, interview **August 2026**, posted **August 17, 2026**: text-to-SQL assignment, model/dataset evaluation and latency discussion.

These support applied-ML and serving-performance themes, not a claim about Fireworks kernel-engineer interviews. Anonymous candidate reports, not company-confirmed questions. REP-04–05 summarize these reviews. The current page's aggregate update date is not an interview date.

##### R03 — Anthropic SWE onsite

[Reddit original account](https://www.reddit.com/r/Technical_Interview/comments/1wswnys/sweanthropic_anthropic_onsite_interview_experience/), u/CollegeBotHelper. Recent **October 2026** post based on relative page date; exact publication/interview day unconfirmed. Level/location unspecified. Describes multiprocessing and intermediate-prefix reuse, plus inference design review and scheduling with one-unit versus eight-unit model requirements. Anonymous self-report with useful specifics; authenticity not independently verified. REP-06–07 paraphrase a single account. Do not equate it with an ML/kernel specialist process.

##### R04 — Together AI SWE onsite (low confidence)

[Reddit report](https://www.reddit.com/r/OfferEngineering/comments/1wj52vj/together_ai_swe_onsite_interview_experience_sep/), posted **September 17, 2026**, titled September onsite experience. Explicitly sourced from the commercial “Chill Interview” service: **secondhand promotional repost**, not a verified original candidate submission. Describes multi-cluster scheduling and timestamped key/value retrieval. Retained as optional inspiration for REP-08 only. The canonical coding analogue is [LeetCode 981](https://leetcode.com/problems/time-based-key-value-store/). No inference-specialist level or team established.

#### Coverage and exclusions

- NVIDIA, Fireworks, Together AI and Anthropic had relevant public accounts or clearly limited adjacent material. These companies do not share one standardized interview process.
- [Together AI Glassdoor](https://www.glassdoor.com/Interview/together-ai-CA-Interview-Questions-E10746640.htm) exposed general project/background questions, not an attributable attention/kernel task. No domain prompt was manufactured from it.
- Cerebras searches surfaced [upcoming Kernel Reliability interview questions from a candidate](https://www.reddit.com/r/leetcode/comments/1sgvspt/interview_with_cerebras/) and [an AI Inference Core candidate seeking advice](https://www.reddit.com/r/leetcode/comments/1vftt7h/cerebras_infrastructure_swe_interview_insights/). Asking what to expect is not a report of questions asked; excluded as question evidence.
- Modular/GPU compiler searches did not yield a usable attributable domain-question account in this pass. No company-specific questions assigned.
- Generic interview guides, anonymous commercial question dumps and “starter” community posts were discovery leads, not independent evidence. No frequency/pass-rate claims copied.
- No paywalled or hidden interview text reconstructed. Broader general coding remains represented by the reported NVIDIA/Together examples; this bank focuses on domain preparation rather than duplicating the OA DSA curriculum.

#### Primary technical references

Use these to check mechanisms and extend answers. The IDs in the bank refer here. Papers describe the named version/algorithm; current runtime behavior requires a pinned implementation. URLs with `main` or `latest` can change.

| ID | Primary source | Supports |
|---|---|---|
| T01 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017 | Attention shapes, scaled dot products, transformer foundations. |
| T02 | [GQA paper](https://arxiv.org/abs/2305.13245), 2023 | Grouped query/KV heads and quality/efficiency tradeoffs. |
| T03 | [RoFormer / RoPE](https://arxiv.org/abs/2104.09864), 2021 | Rotary positional formulation; our implementation tests are original. |
| T04 | [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180), 2023 | KV allocation, sharing and serving. Scheduling drills and numerical examples are ours, not literal vLLM APIs. |
| T05 | [SGLang paper](https://arxiv.org/abs/2312.07104), 2023–2024 | RadixAttention and prefix reuse. Does not establish every current SGLang implementation detail. |
| T06 | [FlashAttention](https://arxiv.org/abs/2205.14135), 2022; [Triton fused attention tutorial](https://triton-lang.org/main/getting-started/tutorials/06-fused-attention.html) | IO-aware exact attention and tiled implementation. |
| T07 | [Speculative decoding](https://arxiv.org/abs/2211.17192), 2022–2023 | Classical distribution-preserving draft/verify algorithm. |
| T08 | [SmoothQuant](https://arxiv.org/abs/2211.10438), 2022–2024 | Quantization and activation-outlier tradeoffs; broader launch scenarios are our exercises. |
| T09 | [Megatron-LM](https://arxiv.org/abs/1909.08053); [Switch Transformers](https://arxiv.org/abs/2101.03961) | Tensor partitioning and sparse expert routing fundamentals. These are foundational training papers; inference placement questions are our extrapolation. |
| T10 | [vLLM disaggregated prefilling](https://docs.vllm.ai/en/latest/features/disagg_prefill/) | Prefill/decode separation and transfer considerations; documentation labels the feature experimental. |
| T11 | [NVIDIA CUDA best practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/) | GPU memory/execution and resource tradeoffs. Hardware-specific details must be qualified. |
| T12 | [NVIDIA Nsight Compute profiling guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) | Counter interpretation and profiling limitations; case-study measurements are synthetic. |
| T13 | [Triton fused softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html) | Reduction/fusion practice; other fused operators and dispatch designs are our exercises. |
| T14 | [Triton matrix multiplication](https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html) | Tiling, pointer arithmetic and autotuning; artifact service design is original. |
| T15 | [PyTorch numerical accuracy](https://docs.pytorch.org/docs/2.14/notes/numerical_accuracy.html) | Floating-point differences and numerical validation. RMSNorm/cross-entropy tasks specify their own mathematical contract. |
| T16 | [Google Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml) | Data quality, evaluation and training-serving skew; task-specific scoring scenarios are original. |

#### Refresh contract

When updating this bank, preserve IDs and attempts. Search original candidate accounts first, then use company-authored engineering sources to address coverage gaps. Date interview and publication separately. Record company, role, round, geography and confidence where available. Tag expanded prompts as original practice; never turn a broad theme into a supposedly verbatim question. Add stronger evidence to existing items before inflating the bank. Keep this domain bank distinct from confirmed Amazon OA requirements.

##### Research log

- **2026-10-28:** Initial public-source research. Eight reported prompts/themes across four companies (three of the eight from one NVIDIA account; Together evidence low-confidence). Seventy-two original exercises backed by primary references or explicitly original engineering scenarios. No GPU testing performed.


- **2026-10-31 refresh:** No new sufficiently attributable exact-team or engine-specific candidate question qualified for addition. Existing NVIDIA account and engine tuning references rechecked; full search/exclusion record is in `inference-engines-research.md` and `amazon-10587705-phone-research.md`. Banks, IDs, schedule and attempt history preserved. No readiness conclusion drawn.

---

<a id="material-07"></a>

## 07. Project and PR evidence audit

**Source:** [amazon-10587705-project-pr-review.md](amazon-10587705-project-pr-review.md) · **Section:** current

### Project and PR review for the AWS inference conversation

**Reviewed:** October 27, 2026. Scope: the four project groups on the AWS resume, with vLLM separated into three merged contributions. Other master-CV projects are summarized as secondary material below.

**Method:** reread all four PR descriptions, complete returned patches and non-bot review discussions; inspect the recorded head versions of SGLang request-time stats and vLLM completion serving; read the kernel README/H100 report and LLMCP README/feasibility ADR. This is a source audit, not a rerun of experiments or independent verification of reported results. No master CV edits were made.

**Evidence boundary:** current CV facts remain the basis of prepared personal claims. Additional details below are explicitly repository/PR findings for analysis and rehearsal. Source comments do not establish how you personally first discovered a problem; reconstruct that history from memory rather than inventing it.

#### 1. TritonAttn / flash-family: attention and KV-cache engineering

**Highlight:** a correctness-focused implementation of multiple attention-serving techniques, with competitive prefill in useful regimes and an explicit diagnosis of the remaining decode gap.

**Current CV evidence:** fused Triton attention/KV kernels; 210 H100 tests; 433 TFLOP/s BF16; 1.1–1.3× SDPA at long sequences; split-KV up to 13.6× versus the custom naive baseline; peak 1.29× SDPA in target GQA regimes; quantization and Nsight profiling; tested greedy model integration.

**What the repository adds to the analysis:**

- The peak prefill case is reported at B=4, H=16, D=128, N=16,384, BF16, non-causal, H100 80GB HBM3. The report lists PyTorch 2.8.0+cu128 and Triton 3.4.0. These are reported configuration details, not independently reproduced here.
- The custom prefill wins are shape-dependent; short sequences and some intermediate D=128 cases lose. Decode wins only 2/72 configurations against SDPA.
- The report attributes useful decode changes to occupancy-aware split selection and grouping shared query heads into tensor-core matrix work. It documents fixing a profiler filter that had selected a reduction kernel instead of the intended compute kernel.
- Separate the quantization experiments: about 5.24× compression is INT2 at 32k context, including metadata/residual overhead. The INT4 +0.33% perplexity result uses a shorter quality experiment; the report lists a different compression ratio there. Never combine the two into one operating point.
- Streaming quality numbers are explicitly provisional because the Hugging Face evaluation's position/RoPE behavior needs parity validation. Avoid using its apparent quality gain as the leading interview result.
- Register/occupancy diagnosis suggests next experiments; it does not prove an already-achieved speedup from a register-cap change. Some profiling captured an initial launch; use benchmark artifacts for steady-state timing.

**Deep-dive sequence:** original single-program mapping → shape sweep → under-parallelized low-batch decode → split/reduction tradeoff → occupancy-aware selection → GQA tensor-core mapping → fair SDPA comparison → correct-kernel profiling → remaining bottleneck and next controlled experiment.

**Personal-history question:** What was your first actual observation that led you to split the decode work: a timing curve, a profiler capture, a paper, or another observation? Recover that sequence before drafting a first-person story.

Sources: [README](https://github.com/surajm20061998/Inference-and-decoding/blob/main/README.md), [H100 report](https://github.com/surajm20061998/Inference-and-decoding/blob/main/docs/report.md). The report was read through its final assessment. `docs/benchmark-methodology.md` is currently only a pointer, so it is not a complete benchmark specification.

#### 2. vLLM #55508: streaming benchmark correctness

**Highlight:** consistent measurement boundaries across endpoints, supported by deterministic tests.

**Documented bug:** completions read the clock again for TTFT instead of reusing the arrival timestamp that seeded inter-token accounting. Chat/audio allowed tokenless usage trailers to move the measured endpoint. Consequently, E2E minus TTFT did not match the summed measured intervals.

**Final patch:** reuse the first arrival timestamp; advance the measured endpoint inside the appropriate choice-bearing branch; reject usage-only streams; use explicit first-chunk state; cover modern and legacy benchmark paths. The code's branch predicates matter: do not describe every SSE message as exactly one generated token.

**Validation highlights:** scripted clocks make extra reads visible without noisy sub-microsecond timing. The patch includes real-clock checks, trailer exclusion and usage-only cases. Maintainer review explicitly asks whether tests fail without the fix; the author response reports checking this. The body’s 12-new/8-sibling counts describe a reported run; the final diff also contains legacy parametrizations, so verify the exact final test inventory before quoting a current aggregate count.

**Deep-dive sequence:** timing invariant → endpoint comparison → timestamp mismatch → trailing frame mismatch → consistent boundary decision → deterministic test → regression sensitivity → compatibility.

**Boundary:** benchmark-client correctness, not measured engine acceleration. A controlled delayed trailer illustrates the mechanism; it is not typical production latency improvement.

Source: [PR #55508 and review](https://github.com/vllm-project/vllm/pull/55508). The initial real-world trigger is not established by the patch alone.

#### 3. SGLang #39312: cumulative waiting across request lifecycles

**Highlight:** a negative-duration bug required understanding state transitions, serialization and compatibility rather than clamping a number.

**Documented bug:** queue re-entry updated `wait_queue_entry_time`, while first-forward time remained from an earlier admission. Their subtraction could become negative.

**Final implementation, distinguishing it from the original description:** `queue_duration_s` accumulates completed waits. First admission and first forward after retraction add an interval; the existing `last_forward_entry_time` sentinel prevents repeated chunks adding the same wait. The merged version does not require a new wait-open boolean. The duration is serialized and excluded from timestamp-name rebasing; retry reset clears it. Histogram sampling retains first-wait semantics and scheduling policy is unchanged.

**Review lesson:** a reviewer suggested reusing existing lifecycle state and questioned serialization. The discussion explains why accumulated waiting cannot be recovered from only two timestamps after multiple admissions.

**Limit:** a later comment reports a PD decode path that failed to restamp queue entry, potentially counting decode time as waiting; the author invited a follow-up from that contributor. This audit has not verified the follow-up's current-main resolution. Unit/randomized PD lifecycle coverage is distinct from full caller-path integration coverage. Broad tests also had documented pre-existing platform failures.

**Deep-dive sequence:** impossible duration → retraction state machine → accumulator → existing sentinel/idempotency → serialization/rebasing → metric contract → missing real caller-path test.

Sources: [PR](https://github.com/sgl-project/sglang/pull/39312), [later PD-path report](https://github.com/sgl-project/sglang/pull/39312#issuecomment-5849702666), [recorded head code](https://github.com/sgl-project/sglang/blob/08a13315266420425435e82458e8be240e43b9ce/python/sglang/srt/observability/req_time_stats.py).

#### 4. vLLM #62205: completion output observability

**Highlight:** the completions frontend silently ignored an existing logging capability; the contribution made enabled output logging work across streaming and non-streaming responses.

**Documented mismatch:** chat and other endpoints supported output logging; the independent completions handler did not accept or implement the flags.

**Final patch:** forward/store output and delta flags; log completed outputs; accumulate generated streaming text per choice; optionally log deltas and then complete text; preserve default-disabled behavior. Tests inspect content, token IDs, finish reasons, delta/full semantics and request correlation.

**Review lesson:** request-ID selection and alignment with chat's implementation were reviewed. The description and intermediate comment discuss per-prompt/engine IDs, while the recorded final head uses the serving method's `request_id` argument. Use the safe statement “request-correlated output logging”; trace the complete call path before promising exact per-prompt or beam-search ID semantics. Code and final tests take precedence over intermediate narrative.

**Deep-dive sequence:** endpoint behavior comparison → missing flag wiring → separate frontend class → streaming state and full-output accumulation → disabled-path overhead → regression tests → ID semantics.

**Boundary:** improved observability, not a proven latency reduction. Reported broad tests had environment-only failures; do not describe them as an entirely green universal suite.

Sources: [PR #62205](https://github.com/vllm-project/vllm/pull/62205), [recorded head code](https://github.com/vllm-project/vllm/blob/38ae9fd214e8c565490bcc50d4fcc3a08407d16f/vllm/entrypoints/openai/completion/serving.py).

#### 5. vLLM #62204: retry-budget clarity and security judgment

**Highlight:** a suspected accounting problem became a lesson in the intended security invariant; the final contribution improved operator explanations and pinned existing restrictive behavior.

**Documented sequence:** the original proposal refunded failed-attempt bytes. Maintainers explained that a repeatedly disconnecting remote URL could then transfer more than the request budget while the accounting forgot earlier bytes. The author accepted this and narrowed scope.

**Final patch:** error wording explicitly includes retried attempts; security documentation says concurrent and retried downloads count; sync/async tests simulate an interrupted body followed by retry. A 1 MiB test budget with 0.5 MiB already received plus a 0.75 MiB retry must reject the cumulative transfer even though the final object's size alone is below the cap.

**Deep-dive sequence:** confusing error → initial refund hypothesis → security review → aggregate resource-consumption invariant → revised scope → adversarial retry regression.

**Boundary:** the merged code preserves the existing accounting. Do not say you implemented a new security budget or fixed an exploitable bypass.

Source: [PR #62204 and discussion](https://github.com/vllm-project/vllm/pull/62204).

#### 6. LLMCP: operational decisions from measured serving quality

**Highlight:** a Kubernetes rollout can be ready and return successful responses while user-visible latency regresses. LLMCP combines request measurement with guarded rollout and scaling decisions.

**Current CV evidence:** operator, streaming measurement sidecar, TTFT/error/concurrency/queue signals, last-good revision, promote/rollback/hold, separate scaling and rollout logic, SLO dashboards, CPU feasibility work and deterministic tests.

**Repository findings:** approximate replica-based canary exposure is distinct from exact request-level routing. Operational gates are distinct from semantic model evaluation. The README names explicit unsupported features, including first-class GPU placement and scale-to-zero; do not infer those from generic Kubernetes support.

**Strong methodology story from the feasibility ADR:** the first comparison confounded replica count/concurrency with the candidate's CPU limit, making the healthy side appear slower. A matched comparison isolated the intended variable. Another issue was benchmarking through port-forward, which bypassed the intended Service distribution and introduced errors; the document describes using an in-cluster load generator instead. These are documented experimental narratives; confirm your personal sequence before speaking them as recollection.

**Deep-dive sequence:** readiness is insufficient → define a useful signal → test noise/effect separation → remove load-generator confounds → compare variants → sufficient-traffic and failure policies → controller state → safe rollout/scaling separation.

Sources: [README](https://github.com/surajm20061998/LLM_Inference_Control_Plane/blob/main/README.md), [feasibility ADR](https://github.com/surajm20061998/LLM_Inference_Control_Plane/blob/main/docs/adr/0001-spike-closed-loop.md). No fresh cluster test was run.

#### Secondary projects from the master CV

These are highlights from `cv.md`, not additional repository audits in this pass:

| Project | Highlight | Best use for this role |
|---|---|---|
| Small-model GRPO | Checkpoint/held-out rollout instrumentation, seeded comparisons and PEFT memory/accuracy tradeoffs | Training lifecycle, experiment design and reproducibility. |
| Transformer scaling | Training/tokenization/checkpoint pipeline and model/token-budget sweeps | Model fundamentals and resource accounting. |
| Long-context interpretability | Refusal behavior, causal interventions and reproducible GPU workflow | Empirical diagnosis, controls and evaluation limits; secondary to inference work here. |
| VICReg | Self-supervised distributed training and downstream evaluation | Broader ML background. |
| Multilingual analysis | Token-level evaluation and systematic failure analysis | Measurement and error analysis. |
| RedCollar | Java event-driven microservices, gateway, persistence and workflows | Backend design and service boundaries. |
| Identity/alerting | SQL/streaming integration, caching and access-controlled APIs | Backend/data-path performance. |

#### Order for our deep dives

1. vLLM #55508: smallest clear example of observation → invariant → fix → proof.
2. SGLang #39312: richer lifecycle/serialization reasoning and integration limitation.
3. TritonAttn: benchmark shape → bottleneck → controlled change → measured tradeoff.
4. LLMCP: experimental confounds and closed-loop decision design.
5. vLLM #62205: frontend wiring and streaming observability.
6. vLLM #62204: changing a proposal after understanding a security constraint.

For each, reconstruct: **first signal → reproduction → competing explanations → decisive evidence → exact code change → tests → result → remaining limitation**. Ask one personal-history question at a time. The PR proves what changed; it cannot by itself prove your original thought process.

---

<a id="material-08"></a>

## 08. Technical revision notes

**Source:** [amazon-10587705-inference-revision-notes.md](amazon-10587705-inference-revision-notes.md) · **Section:** reference

### AWS inference optimization: revision notes and spoken answers

**Prepared:** October 27, 2026. **Role:** Machine Learning Engineer II, AWS Inference Optimization, requisition 10587705.

**Purpose:** revise the selected Stanford CS336 Spring 2025 lectures and Baseten book sections, then connect them to your actual work. Sadaf offered a 30-minute informational phone chat. All questions below are **inferred from the JD and your CV**, not reported questions from her team. Technical follow-ups are preparation options; the call's exact technical depth is unconfirmed.

**Subsequent source audit, October 27:** read the [project/PR review](#material-07) before quoting results. The kernel report separates INT2's 5.24× long-context compression from INT4's +0.33% short-evaluation perplexity result; these are not one operating point. SGLang's final patch reuses existing `last_forward_entry_time` state, and a later PR comment identifies an uncovered PD decode caller path. The audit also distinguishes final code from intermediate PR descriptions and recorded test counts. These clarifications supersede broader interpretations of the summaries below.

**Evidence labels:** **Your work** means established in the current [master CV](../../cv.md). **Concept** means technical knowledge to understand. **Proposed approach** means how you would investigate a new problem, not an experiment you already performed. Numerical examples labeled **illustrative** are not your measurements. This document adds no new experience to the CV.

**Use:** read cards 1, 8, 9, 10, 12 and 13 first for the call. Work through the remaining cards before a technical interview. Rehearse each short answer, then explain the mechanism in your own words.

#### 1. Your introduction and why this team

**Likely question:** “Tell me about yourself, and why inference optimization?”

> I have nearly four years of professional software-engineering experience at Oracle and Incture, and I completed my master's at NYU this May. My recent work focuses on GPU performance and LLM inference. I built Triton attention and KV-cache kernels, profiled them on H100, and contributed merged fixes to vLLM and SGLang around reliable serving measurements. This role connects those interests: kernel performance, inference engines, and the engineering needed to turn improvements into dependable customer-facing serving.

**Why your background matters:** kernels supply hands-on optimization evidence; upstream work supplies evidence of correctness and compatibility in existing systems; professional roles supply Java/backend/test-infrastructure experience. Keep those categories clear when discussing duration and ownership.

**If asked about professional GPU tenure:** your nearly four professional years are not four years of professional MLE/kernel work. State that the specialization is recent project/open-source work. Two years of qualifying professional architecture scope is not independently established by total employment duration.

#### 2. Prefill, decode and the KV cache

**Revise:** CS336 Lecture 10; Baseten 2.2 and 2.4.

**Likely question:** “Why do you optimize prefill and decode differently?”

> Prefill processes the input positions together, which exposes larger matrix operations and opportunities for data reuse. Autoregressive decode adds one token per active sequence per step, often doing less arithmetic relative to weight and KV-cache movement. Those different resource profiles motivate different kernels and serving policies. The actual bottleneck still depends on batch size, context length, architecture and implementation.

**Concept:** caching avoids recomputing prior keys and values; each new token still needs to attend to the relevant cached context. A long KV history can make attention's data movement important. Feed-forward, projection, communication or launch overhead can dominate other regimes; “attention is always the bottleneck” is too broad.

**Your work:** connect prefill to FlashAttention-style tiling, and decode to split-KV/GQA/MQA. Connect queueing and TTFT to serving measurements, rather than describing TTFT as kernel time alone.

**Follow-up:** increasing batch size can amortize weight traffic, but consumes KV capacity and can worsen latency. There is no single batch size that is optimal for every service.

Sources: [Stanford Lecture 10 code](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_10.py), [Baseten bottlenecks](https://www.baseten.co/inference-engineering/book/02-models/calculating-inference-bottlenecks/).

#### 3. Resource accounting and a roofline explanation

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

#### 4. GPU execution, memory and occupancy

**Revise:** CS336 Lecture 5; Baseten 3.1 and 3.3.

**Likely question:** “What does register-pressure-limited occupancy mean?”

> Registers are a finite resource on each streaming multiprocessor. A kernel's per-thread or per-block register requirements can limit how much work is resident at once. That may reduce opportunities to hide latency. But forcing register use down can cause spills or reduce useful work, so the decision has to be judged by measured performance.

**Concept map:** threads execute in warps; blocks are assigned to SMs. Registers are thread-private, shared memory is shared within a block, caches service memory accesses, and HBM holds large tensors. Tensor cores accelerate supported matrix operations; kernel efficiency still depends on moving and scheduling the data.

**Your work:** the CV establishes Nsight Compute diagnosis of register-pressure-capped occupancy. Prepare an actual report and code/configuration change. Exact occupancy percentages, register counts, stall counters and a resulting speedup are not recorded in the CV, so do not manufacture them.

**Follow-up:** “Is maximum occupancy your target?” Your target is the best relevant latency/throughput under correctness constraints. Occupancy is diagnostic evidence, not the objective function.

Sources: [Baseten GPU architecture](https://www.baseten.co/inference-engineering/book/03-hardware/gpu-architecture/), [NVIDIA occupancy guidance](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy).

#### 5. FlashAttention, tiling and stable online softmax

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

#### 6. Split-KV decoding and GQA/MQA

**Revise:** CS336 Lecture 10; Baseten 2.5 and 5.3.

**Likely question:** “What is split-KV, and when can it lose?”

> Instead of assigning an entire KV history to one unit of work, split-KV processes portions in parallel and combines the partial attention results. That can help when the original mapping exposes too little parallelism. It also introduces partial-result storage, reduction and coordination work, which can outweigh the benefit for other shapes.

**Concept:** partial softmax outputs require normalization-aware merging; simply averaging the normalized outputs is generally wrong. GQA shares KV heads across groups of query heads; MQA uses one KV head. This reduces KV storage relative to otherwise comparable multi-head attention.

**Your work:** occupancy-aware split policy and tensor-core GQA/MQA path. Keep both baselines explicit: up to **13.6× versus naive decode**; **peak 1.29× versus SDPA in target GQA regimes**.

**Prepare:** one winning shape and one losing shape, plus the chosen split count and reduction cost. Those settings are not supplied in the master CV.

Sources: [Lecture 10](https://raw.githubusercontent.com/stanford-cs336/spring2025-lectures/main/lecture_10.py), [Baseten attention](https://www.baseten.co/inference-engineering/book/02-models/optimizing-attention/).

#### 7. KV capacity, quantization and cache behavior

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

#### 8. Benchmarking and profiling: your highest-priority defense

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

#### 9. Latency metrics and your vLLM contribution

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

#### 10. Request lifecycles and your SGLang contribution

**Revise:** Baseten 4.3/4.5; connect request lifecycle reasoning to continuous batching.

**Likely question:** “Why could queue time become negative?”

> A request could run, be retracted or preempted, and re-enter the queue. The accounting mixed its original execution timestamp with its newer queue-entry timestamp. I accumulated each waiting interval, made closing a wait idempotent and handled process-clock rebasing while preserving scheduling decisions and the histogram contract.

**Illustrative timestamps:** queue at 1, run at 3, requeue at 8, resume at 10. `3 - 8 = -5` is invalid; total waiting is `(3 - 1) + (10 - 8) = 4`.

**Important distinctions:** an interval should close once even if chunked-prefill callbacks repeat. Elapsed durations must not be treated as absolute timestamps during clock rebasing. Preserve timestamps other scheduler code relies on; clamping a negative result to zero hides the faulty accounting. The existing histogram retained first-wait semantics, while total-wait accounting served other outputs.

**Your evidence:** six regression/contract tests, 303 related tests validated, 20,000 randomized lifecycles, 9,504 non-retracted compatibility cases. Broader testing included documented pre-existing platform failures; avoid saying every test passed. PD coverage was unit/randomized lifecycle validation, not an end-to-end deployment.

Sources: [SGLang PR #39312](https://github.com/sgl-project/sglang/pull/39312), current CV. This card summarizes the PR mechanism; the timestamps are invented solely for teaching.

#### 11. Engines, batching, parallelism and multi-GPU tradeoffs

**Revise:** CS336 Lectures 7–8 and 10; Baseten 4.3 and 5.4.

**Likely question:** “How would you choose an inference engine?”

**Proposed approach:** start with supported model/hardware, correctness and required features; compare under the intended prompt/output distribution, concurrency and latency objectives; consider operation and debugging. No engine is automatically best for all workloads.

**Concept:** continuous batching admits new requests as capacity becomes available rather than waiting for every sequence in a static batch to finish. KV memory and scheduling influence achievable concurrency. Efficient GPU work can still sit behind a long queue.

**Your connection:** vLLM measurement correctness and SGLang lifecycle accounting sit around the engine's execution path; they do not establish changes to engine scheduling policy or upstream attention kernels.

**Parallelism refresher:** tensor parallelism divides operations/model tensors and introduces communication; pipeline parallelism divides layers/stages and faces scheduling/bubble tradeoffs; expert parallelism distributes MoE experts and routing traffic; data parallelism provides replicas for separate work. FSDP/ZeRO primarily address distributed training state/memory; mentioning them alone does not demonstrate a production serving design.

**Your boundary:** NCCL, RDMA, FSDP and DeepSpeed are in your established skills. Exact production topology, device count or collective optimization ownership is not established here.

Sources: [Baseten engines](https://www.baseten.co/inference-engineering/book/04-software/inference-engines/), [Baseten model parallelism](https://www.baseten.co/inference-engineering/book/05-techniques/model-parallelism/), [CS336 schedule](https://cs336.stanford.edu/spring2025/).

#### 12. Speculative decoding: a knowledge gap to explain honestly

**Revise:** CS336 Lecture 10; Baseten 5.2.

**Likely question:** “What is speculative decoding, and when would it help?”

> A cheaper draft mechanism proposes several tokens, then the target verifies them. The goal is to emit more useful tokens per expensive target step. Benefit depends on acceptance, drafting/verification costs and workload utilization. Low acceptance or high overhead can make it slower.

**Concept:** standard exact speculative sampling needs correct acceptance/rejection and correction to preserve the target distribution in theory. Approximate variants may relax that goal; do not promise identical sampled text under every implementation and numerical setting.

**Proposed experiment:** compare with the same target model, quality checks and traffic; sweep draft depth/concurrency; measure emitted tokens per verification cycle, draft/verify overhead, TTFT/TPOT and useful throughput. This is a proposed benchmark, not existing project evidence.

**Your connection:** attention, quantization and measurement experience provides relevant foundations. The CV does not establish that you implemented speculative decoding.

Sources: [Baseten speculation](https://www.baseten.co/inference-engineering/book/05-techniques/speculative-decoding/), [vLLM lossless-guarantee discussion](https://docs.vllm.ai/en/latest/features/speculative_decoding/).

#### 13. Disaggregated inference: another honest boundary

**Revise:** Baseten 5.5, 3.3 and 4.4.

**Likely question:** “Why separate prefill and decode?”

> Their different resource and latency requirements can justify independent workers and capacity allocation. Separation may reduce interference, but requires KV transfer, routing and coordination. It helps only when those costs are outweighed by improved utilization or latency for the workload.

**Concept:** estimate the KV payload, effective transfer bandwidth and added coordination delay. Then inspect prefill/decode queues, cache locality, capacity imbalance and failure recovery. Treat claims about benefit as workload-dependent.

**Your connection:** you understand both phases through kernel work; SGLang tests exercised relevant lifecycle modes. You did not establish an end-to-end PD deployment or author the disaggregation architecture. NCCL collective knowledge does not automatically prove a point-to-point KV-transfer implementation.

**Proposed question for the team:** “How do you decide which workloads benefit from disaggregation, and what is the biggest constraint in practice: transfer, routing or capacity balance?”

Source: [Baseten disaggregation](https://www.baseten.co/inference-engineering/book/05-techniques/disaggregation/).

#### 14. Production: bridge kernel work to the LLM control plane

**Revise:** Baseten 7.2, 7.4 and 7.5.

**Likely question:** “How would you keep an inference optimization safe in production?”

**Proposed approach:** establish correctness and a representative performance baseline; test mixed traffic and failure behavior; deploy a canary with explicit acceptance criteria; watch errors, tail latency and useful throughput; roll back or hold if the evidence is negative or inconclusive. This is a design answer, not a claim of doing it on AWS products.

**Your work:** LLMCP deploys an OpenAI-compatible service, instruments streaming TTFT/errors/concurrency/queue depth, and separates scaling decisions from revision promotion. Its CPU p95-TTFT feasibility study supports that project's release gate; it does not establish production GPU-fleet scale.

**Autoscaling concept:** traffic growth, queueing, occupied request slots, KV capacity and cold-start time can matter more than CPU percentage. An aggressive scaling loop can still lose to slow model loading or poor capacity availability.

**Client concept:** timeouts, cancellation, retries and streaming completion semantics affect reliability and observed latency. Logging must remain useful and appropriately controlled; default/no-op behavior is relevant to your output-logging contribution.

Sources: [Autoscaling](https://www.baseten.co/inference-engineering/book/07-production/autoscaling/), [Testing/deployment](https://www.baseten.co/inference-engineering/book/07-production/testing-and-deployment/), [Client code](https://www.baseten.co/inference-engineering/book/07-production/client-code/), current CV.

#### 15. Price-performance and what your results establish

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

#### 16. Questions to ask and final rehearsal

Pick three for the informational conversation:

1. “Which is the immediate priority: kernels, inference-engine development, or AWS integration?”
2. “What evidence would the manager want beyond the projects and upstream work on my CV?”
3. “What do the next stages assess, and should I prepare Python, C++, CUDA/Triton, inference design or a combination?”
4. “How is the role leveled, and what architecture ownership does a successful mid-level engineer take on?”

**Sixty-minute revision:** 10 minutes on introduction/fit; 15 on one real kernel benchmark/profile; 15 on both PR mechanisms; 10 on speculation/disaggregation; 10 explaining the answers aloud without reading.

**Stop and verify rather than guessing:** exact H100 variant, tensor shapes, software/backend versions, test tolerances, benchmark repetitions, model/data behind perplexity, personal code change after profiling, current work authorization, start date, and whether the application was submitted.

**Avoid these overclaims:** four years of professional GPU work; production SageMaker/Bedrock/HyperPod ownership; authored speculative/disaggregated systems; upstream kernel acceleration from the metrics PRs; all 303 SGLang tests passed; universal SDPA superiority; retracted Oracle production-throughput claims.

#### Source map

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

---

<a id="material-09"></a>

## 09. Interview practice log

**Source:** [amazon-10587705-phone-attempts.csv](amazon-10587705-phone-attempts.csv) · **Section:** progress

````csv
date,track,question_or_story_id,minutes,independent_or_hints,correctness,tests_or_evidence,followup_gap,next_review
````

---

<a id="material-10"></a>

## 10. Inference-engine practice tracker

**Source:** [inference-engines-attempts.csv](inference-engines-attempts.csv) · **Section:** progress

````csv
id,priority,status,date,minutes,independent,result,misconception_or_error,next_review
VLLM-01,P0,unattempted,,,,,,
VLLM-02,P0,unattempted,,,,,,
VLLM-03,P0,unattempted,,,,,,
VLLM-04,P0,unattempted,,,,,,
VLLM-05,P0,unattempted,,,,,,
VLLM-06,P0,unattempted,,,,,,
SGL-01,P0,unattempted,,,,,,
SGL-02,P0,unattempted,,,,,,
SGL-03,P0,unattempted,,,,,,
SGL-04,P0,unattempted,,,,,,
SGL-05,P0,unattempted,,,,,,
SGL-06,P0,unattempted,,,,,,
OPT-01,P0,unattempted,,,,,,
OPT-02,P1,unattempted,,,,,,
OPT-03,P1,unattempted,,,,,,
OPT-04,P0,unattempted,,,,,,
ECODE-01,P0,unattempted,,,,,,
ECODE-02,P0,unattempted,,,,,,
ECODE-03,P0,unattempted,,,,,,
ECODE-04,P0,unattempted,,,,,,
ECODE-05,P0,unattempted,,,,,,
ECODE-06,P0,unattempted,,,,,,
ECASE-01,P0,unattempted,,,,,,
ECASE-02,P0,unattempted,,,,,,
ECASE-03,P0,unattempted,,,,,,
ECASE-04,P0,unattempted,,,,,,
ECASE-05,P0,unattempted,,,,,,
ECASE-06,P0,unattempted,,,,,,
PROJ-01,P0,unattempted,,,,,,
PROJ-02,P0,unattempted,,,,,,
PROJ-03,P0,unattempted,,,,,,
PROJ-04,P0,unattempted,,,,,,
````

---

<a id="material-11"></a>

## 11. ML and inference practice tracker

**Source:** [ml-inference-engineering-attempts.csv](ml-inference-engineering-attempts.csv) · **Section:** progress

````csv
id,priority,status,attempt_date,minutes,score_out_of_10,blocker,evidence_or_tests,revisit_date
REP-01,optional,unattempted,,,,,,
REP-02,optional,unattempted,,,,,,
REP-03,optional,unattempted,,,,,,
REP-04,optional,unattempted,,,,,,
REP-05,optional,unattempted,,,,,,
REP-06,optional,unattempted,,,,,,
REP-07,optional,unattempted,,,,,,
REP-08,optional,unattempted,,,,,,
CON-01,P0,unattempted,,,,,,
CON-02,P0,unattempted,,,,,,
CON-03,P0,unattempted,,,,,,
CON-04,P0,unattempted,,,,,,
CON-05,P0,unattempted,,,,,,
CON-06,P0,unattempted,,,,,,
CON-07,P0,unattempted,,,,,,
CON-08,P0,unattempted,,,,,,
CON-09,P0,unattempted,,,,,,
CON-10,P0,unattempted,,,,,,
CON-11,P0,unattempted,,,,,,
CON-12,P0,unattempted,,,,,,
CON-13,P1,unattempted,,,,,,
CON-14,P1,unattempted,,,,,,
CON-15,P1,unattempted,,,,,,
CON-16,P1,unattempted,,,,,,
CON-17,P0,unattempted,,,,,,
CON-18,P0,unattempted,,,,,,
CON-19,P0,unattempted,,,,,,
CON-20,P0,unattempted,,,,,,
CON-21,P0,unattempted,,,,,,
CON-22,P0,unattempted,,,,,,
CON-23,P0,unattempted,,,,,,
CON-24,P0,unattempted,,,,,,
CODE-01,P0,unattempted,,,,,,
CODE-02,P0,unattempted,,,,,,
CODE-03,P0,unattempted,,,,,,
CODE-04,P0,unattempted,,,,,,
CODE-05,P0,unattempted,,,,,,
CODE-06,P1,unattempted,,,,,,
CODE-07,P1,unattempted,,,,,,
CODE-08,P1,unattempted,,,,,,
CODE-09,P0,unattempted,,,,,,
CODE-10,P0,unattempted,,,,,,
CODE-11,P0,unattempted,,,,,,
CODE-12,P1,unattempted,,,,,,
CODE-13,P0,unattempted,,,,,,
CODE-14,P1,unattempted,,,,,,
CODE-15,P0,unattempted,,,,,,
CODE-16,P1,unattempted,,,,,,
DES-01,P0,unattempted,,,,,,
DES-02,P0,unattempted,,,,,,
DES-03,P0,unattempted,,,,,,
DES-04,P1,unattempted,,,,,,
DES-05,P0,unattempted,,,,,,
DES-06,P1,unattempted,,,,,,
DES-07,P0,unattempted,,,,,,
DES-08,P0,unattempted,,,,,,
DES-09,P1,unattempted,,,,,,
DES-10,P1,unattempted,,,,,,
DES-11,P1,unattempted,,,,,,
DES-12,P0,unattempted,,,,,,
CASE-01,P0,unattempted,,,,,,
CASE-02,P0,unattempted,,,,,,
CASE-03,P0,unattempted,,,,,,
CASE-04,P1,unattempted,,,,,,
CASE-05,P1,unattempted,,,,,,
CASE-06,P0,unattempted,,,,,,
CASE-07,P0,unattempted,,,,,,
CASE-08,P1,unattempted,,,,,,
CASE-09,P0,unattempted,,,,,,
CASE-10,P0,unattempted,,,,,,
CASE-11,P1,unattempted,,,,,,
CASE-12,P0,unattempted,,,,,,
ML-01,P0,unattempted,,,,,,
ML-02,P0,unattempted,,,,,,
ML-03,P1,unattempted,,,,,,
ML-04,P0,unattempted,,,,,,
ML-05,P1,unattempted,,,,,,
ML-06,P1,unattempted,,,,,,
ML-07,P1,unattempted,,,,,,
ML-08,P0,unattempted,,,,,,
````

---

<a id="material-12"></a>

## 12. Plain-Python engine lab guide

**Source:** [README.md](practice/engine_basics/README.md) · **Section:** practice

### Inference engines, one small function at a time

This is a learning lab for ECODE-01–03 in the inference-engine bank. It requires Python 3 only. It models a few state transitions; it is not an implementation of vLLM or SGLang and does not benchmark performance.

Open `exercises.py`. Work on one function, predict the output manually, then run its checks. `reference.py` contains complete answers for review after an attempt. Reference tests passed when the lab was prepared; this does not record a candidate solve.

Run commands from this directory:

```bash
cd /Users/surajmishra/workspace/careerops/career-ops/interview-prep/amazon-mle-2/practice/engine_basics
python3 check.py first
```

The starter intentionally raises `NotImplementedError`. That means the exercise needs implementation. It is not a dependency or environment failure. Keep other stages untouched until the current stage is understood.

#### Stage 1 — Find the first generated output

Each event is `(timestamp, token_count)`. For this exercise, timestamps are supplied, times are ordered, and counts are nonnegative. An event with count zero contains no generated tokens. It can represent metadata rather than useful model output.

Example:

```python
events = [(10, 0), (12, 1), (15, 3), (19, 0)]
```

Trace:

| Event | Contains tokens? | What to do |
|---|---|---|
| `(10, 0)` | No | Continue looking |
| `(12, 1)` | Yes | This is the first token-bearing event |
| `(15, 3)` | Yes | Later output; irrelevant to finding the first |
| `(19, 0)` | No | A later metadata event |

Implement `first_token_time(events)`, returning `12` here and `None` if no event contains tokens. Return the timestamp, not the tuple, index or elapsed duration. Try with an empty list and with a first timestamp of zero.

Build it with a loop and an `if` statement. No NumPy or list comprehension is required. First explain which values a loop iteration unpacks.

```bash
python3 check.py first
```

Interview follow-up after your attempt: why would taking the first network event produce the wrong TTFT for some streams?

#### Stage 2 — Derive streaming measurements

Implement `streaming_summary(start_time, events)` with the same valid-input assumptions.

For start time `10` and the example above, return:

```python
{
    "ttft": 2,
    "e2e": 5,
    "event_gaps": [3],
    "total_tokens": 4,
}
```

The final event at 19 adds no tokens and must not extend the measured output endpoint. If no tokens arrive, both durations are `None`, gaps are empty and the token total is zero. A single output event has no gap. Two output events at the same instant produce a zero gap.

Decide which running state you need before coding. Write down the state after each event. A three-token chunk does not tell you when its three individual tokens were produced; call the measured differences **event gaps**.

```bash
python3 check.py streaming
```

#### Stage 3 — Account for repeated waiting

Complete `QueueWait`. A request can wait, run, then wait again. `total` sums completed waits only; running time is excluded.

```text
start(1) → admit(4): completed wait = 3
running from 4 to 8: no waiting added
start(8) → admit(10): completed wait = 2
total = 5
```

`start` opens a wait and `admit` closes it. Repeated start while open, admit while closed and time moving backward raise `ValueError` without altering state. Equal timestamps are allowed. `reset()` clears the total, open interval and timestamp history.

```bash
python3 check.py queue
```

Before writing methods, draw the two states: **not waiting** and **waiting**. Mark legal transitions. This connects to retraction/queue-time reasoning in SGLang; it does not reproduce that project's exact class or metrics contract.

#### Stage 4 — Allocate a token budget

Implement `choose_batch`. Each active decode gets one token; remaining budget goes to waiting prefill requests in order. A prompt may be partially processed. Inputs must remain unchanged. A budget below the active-decode count raises `ValueError`.

Example:

```text
budget = 12
active decodes = a,b,c,d → spend 4
waiting prompts = p needs 10, q needs 6
budget remaining = 8 → p receives 8
unfinished prompts = p needs 2, q needs 6
```

Return:

```python
(
    [("a", 1), ("b", 1), ("c", 1), ("d", 1), ("p", 8)],
    [("p", 2), ("q", 6)],
)
```

The prompt counts are positive; IDs are unique across active and waiting requests. Completed prompts disappear from the remaining list. Unused budget is permitted if there is no work. This toy scheduler has no KV-capacity constraint, preemption or speculation.

```bash
python3 check.py scheduler
python3 check.py all
```

#### Reviewing your attempt

After each stage: state what was confusing, explain one edge case, and describe the state your function maintains. Then compare against the reference if needed:

```bash
python3 check.py all --reference
```

Passing the reference checks validates the teaching implementation, not your starter file. Passing public checks on your own implementation is a learning milestone, not proof of production correctness or an interview outcome. Record actual attempts only; do not mark a walkthrough as an independent solve.

---

<a id="material-13"></a>

## 13. Engine lab starter exercises

**Source:** [exercises.py](practice/engine_basics/exercises.py) · **Section:** practice

````python
"""Small inference-engine practice tasks. Implement one function at a time.

Use ordinary Python only. Read README.md for the contracts and worked traces.
Do not open reference.py until after your own attempt.
"""


def first_token_time(events):
    """Return the timestamp of the first event with count > 0, or None.

    events is a list of (timestamp, token_count) pairs in time order.
    """
    raise NotImplementedError("Start here: inspect one event at a time")


def streaming_summary(start_time, events):
    """Return ttft, e2e, event_gaps, and total_tokens as a dictionary.

    Event times are nondecreasing and >= start_time; counts are nonnegative.
    TTFT/E2E end at the first/last positive-token event. No tokens means
    ttft=None, e2e=None, event_gaps=[], total_tokens=0.
    """
    raise NotImplementedError("Build this after first_token_time")


class QueueWait:
    """Track completed waiting intervals with explicit start/admit operations.

    Expose total (initially 0). Reject start while waiting, admit while not
    waiting, or a timestamp earlier than the last accepted operation.
    Rejected operations must not change state. reset() clears everything.
    """

    def __init__(self):
        self.total = 0.0
        # Add the state you need here.

    def start(self, timestamp):
        raise NotImplementedError("Open a wait interval")

    def admit(self, timestamp):
        raise NotImplementedError("Close and accumulate a wait interval")

    def reset(self):
        raise NotImplementedError("Reset accumulated time and lifecycle state")


def choose_batch(decode_ids, prefills, budget):
    """Return (allocations, remaining_prefills) without changing inputs.

    decode_ids: unique request IDs, each needing one token this iteration.
    prefills: [(id, positive_remaining_token_count), ...], in FCFS order.
    IDs are unique across both collections. budget is a nonnegative integer.
    Reject budget < len(decode_ids) with ValueError.
    allocations is [(id, token_count), ...], decode first, then FCFS prefill.
    remaining_prefills includes unfinished prompts only, in original order.
    """
    raise NotImplementedError("Manually allocate the 12-token example first")
````

---

<a id="material-14"></a>

## 14. Engine lab public checks

**Source:** [check.py](practice/engine_basics/check.py) · **Section:** practice

````python
"""Run public exercise checks. Reference success does not imply user mastery."""
import argparse
import importlib
import unittest

parser = argparse.ArgumentParser()
parser.add_argument("stage", choices=["first", "streaming", "queue", "scheduler", "all"])
parser.add_argument("--reference", action="store_true", help="verify teaching reference instead")
args = parser.parse_args()
subject = importlib.import_module("reference" if args.reference else "exercises")


class FirstChecks(unittest.TestCase):
    def test_leading_metadata(self):
        self.assertEqual(subject.first_token_time([(10, 0), (12, 1), (15, 2)]), 12)

    def test_zero_timestamp(self):
        self.assertEqual(subject.first_token_time([(0, 2), (3, 1)]), 0)

    def test_no_output(self):
        self.assertIsNone(subject.first_token_time([]))
        self.assertIsNone(subject.first_token_time([(1, 0), (2, 0)]))


class StreamingChecks(unittest.TestCase):
    def test_trailer_and_chunk_semantics(self):
        result = subject.streaming_summary(10, [(10, 0), (12, 1), (15, 3), (19, 0)])
        self.assertEqual(result, {"ttft": 2, "e2e": 5, "event_gaps": [3], "total_tokens": 4})

    def test_single_event(self):
        self.assertEqual(subject.streaming_summary(0, [(2, 5)]),
                         {"ttft": 2, "e2e": 2, "event_gaps": [], "total_tokens": 5})

    def test_no_tokens(self):
        expected = {"ttft": None, "e2e": None, "event_gaps": [], "total_tokens": 0}
        self.assertEqual(subject.streaming_summary(0, []), expected)
        self.assertEqual(subject.streaming_summary(0, [(1, 0)]), expected)

    def test_equal_times(self):
        self.assertEqual(subject.streaming_summary(0, [(0, 1), (0, 1)])["event_gaps"], [0])


class QueueChecks(unittest.TestCase):
    def test_two_waits_running_time_excluded(self):
        q = subject.QueueWait()
        q.start(1)
        q.admit(4)
        q.start(8)
        q.admit(10)
        self.assertEqual(q.total, 5)

    def test_rejected_operations_preserve_state(self):
        q = subject.QueueWait()
        with self.assertRaises(ValueError):
            q.admit(0)
        q.start(1)
        with self.assertRaises(ValueError):
            q.start(3)
        with self.assertRaises(ValueError):
            q.admit(0)
        q.admit(4)
        self.assertEqual(q.total, 3)
        with self.assertRaises(ValueError):
            q.admit(4)
        with self.assertRaises(ValueError):
            q.start(2)
        q.start(5)
        q.admit(6)
        self.assertEqual(q.total, 4)

    def test_reset_and_zero_wait(self):
        q = subject.QueueWait()
        q.start(10)
        q.reset()
        self.assertEqual(q.total, 0)
        q.start(0)
        q.admit(0)
        self.assertEqual(q.total, 0)


class SchedulerChecks(unittest.TestCase):
    def test_twelve_token_trace(self):
        result = subject.choose_batch(["a", "b", "c", "d"], [("p", 10), ("q", 6)], 12)
        self.assertEqual(result, ([("a", 1), ("b", 1), ("c", 1), ("d", 1), ("p", 8)],
                                  [("p", 2), ("q", 6)]))

    def test_finish_then_partial(self):
        self.assertEqual(subject.choose_batch(["a"], [("p", 2), ("q", 5)], 5),
                         ([("a", 1), ("p", 2), ("q", 2)], [("q", 3)]))

    def test_capacity_and_no_mutation(self):
        ids, prompts = ["a"], [("p", 2)]
        self.assertEqual(subject.choose_batch(ids, prompts, 3), ([("a", 1), ("p", 2)], []))
        self.assertEqual(ids, ["a"])
        self.assertEqual(prompts, [("p", 2)])

    def test_zero_and_unused_budget(self):
        self.assertEqual(subject.choose_batch([], [("p", 2)], 0), ([], [("p", 2)]))
        self.assertEqual(subject.choose_batch([], [], 10), ([], []))

    def test_insufficient_decode_budget(self):
        with self.assertRaises(ValueError):
            subject.choose_batch(["a", "b"], [], 1)


stages = {"first": FirstChecks, "streaming": StreamingChecks,
          "queue": QueueChecks, "scheduler": SchedulerChecks}
selected = stages.values() if args.stage == "all" else [stages[args.stage]]
suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(cls) for cls in selected)
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
````

---

<a id="material-15"></a>

## 15. K-means teaching implementation

**Source:** [kmeans_day1.py](practice/kmeans_day1.py) · **Section:** practice

````python
"""Day 1 teaching reference: Lloyd's K-means with supplied initial centers."""
import numpy as np


def assign_labels(X, centroids):
    # Each column contains squared distances to one centroid.
    distances = np.empty((len(X), len(centroids)), dtype=float)
    for j, center in enumerate(centroids):
        distances[:, j] = np.sum((X - center) ** 2, axis=1)
    # argmin picks the first index when distances tie.
    return np.argmin(distances, axis=1)


def kmeans(X, initial_centroids, max_iter=100, tol=1e-4):
    X = np.asarray(X, dtype=float)
    centroids = np.array(initial_centroids, dtype=float, copy=True)

    if X.ndim != 2 or X.shape[0] == 0 or X.shape[1] == 0:
        raise ValueError("X must have shape [N, D], with N and D positive")
    if centroids.ndim != 2 or centroids.shape[1] != X.shape[1]:
        raise ValueError("centroids must have shape [K, D]")
    if not 1 <= len(centroids) <= len(X):
        raise ValueError("require 1 <= K <= N")
    if not np.isfinite(X).all() or not np.isfinite(centroids).all():
        raise ValueError("inputs must be finite")
    if not isinstance(max_iter, (int, np.integer)) or max_iter < 1:
        raise ValueError("max_iter must be a positive integer")
    if not np.isfinite(tol) or tol < 0:
        raise ValueError("tol must be finite and nonnegative")

    for _ in range(max_iter):
        labels = assign_labels(X, centroids)
        new_centroids = centroids.copy()

        for j in range(len(centroids)):
            members = X[labels == j]
            if len(members) > 0:
                new_centroids[j] = members.mean(axis=0)
            # Empty cluster: keep its previous centroid.

        shifts = np.linalg.norm(new_centroids - centroids, axis=1)
        centroids = new_centroids
        if shifts.max() <= tol:
            break

    # Centers moved after labels were computed; synchronize returned labels.
    labels = assign_labels(X, centroids)
    return centroids, labels


def _self_check():
    X = np.array([[0., 0.], [0., 2.], [8., 8.], [8., 10.]])
    initial = np.array([[0., 0.], [8., 8.]])
    centers, labels = kmeans(X, initial)
    np.testing.assert_allclose(centers, [[0, 1], [8, 9]])
    np.testing.assert_array_equal(labels, [0, 0, 1, 1])
    np.testing.assert_array_equal(initial, [[0, 0], [8, 8]])

    centers, labels = kmeans(X, [[0., 0.]])
    np.testing.assert_allclose(centers, [[4, 5]])
    np.testing.assert_array_equal(labels, [0, 0, 0, 0])

    centers, labels = kmeans([[1.], [1.], [1.]], [[1.], [100.]])
    np.testing.assert_allclose(centers, [[1], [100]])
    np.testing.assert_array_equal(labels, [0, 0, 0])

    # max_iter=1: old assignments differ from final nearest-center labels.
    centers, labels = kmeans([[0.], [2.], [3.], [10.]], [[0.], [3.]], max_iter=1)
    np.testing.assert_allclose(centers, [[0], [5]])
    np.testing.assert_array_equal(labels, [0, 0, 1, 1])

    centers, labels = kmeans([[0.], [2.]], [[0.], [2.]])
    np.testing.assert_allclose(centers, [[0], [2]])
    np.testing.assert_array_equal(labels, [0, 1])

    # Tie at x=1 is assigned to the smaller centroid index.
    np.testing.assert_array_equal(assign_labels(np.array([[1.]]), np.array([[0.], [2.]])), [0])
    print("Passed: separated clusters, K=1, duplicates/empty cluster, iteration limit, fixed point, ties, input preservation.")


if __name__ == "__main__":
    _self_check()
````

---

<a id="material-16"></a>

## 16. Engine lab reference solutions — spoilers

**Source:** [reference.py](practice/engine_basics/reference.py) · **Section:** solutions

````python
"""Reference solutions: inspect only after trying exercises.py."""


def first_token_time(events):
    for timestamp, count in events:
        if count > 0:
            return timestamp
    return None


def streaming_summary(start_time, events):
    first = None
    last = None
    gaps = []
    total = 0
    for timestamp, count in events:
        if count == 0:
            continue
        if first is None:
            first = timestamp
        if last is not None:
            gaps.append(timestamp - last)
        last = timestamp
        total += count
    return {
        "ttft": None if first is None else first - start_time,
        "e2e": None if last is None else last - start_time,
        "event_gaps": gaps,
        "total_tokens": total,
    }


class QueueWait:
    def __init__(self):
        self.reset()

    def start(self, timestamp):
        if self._opened_at is not None:
            raise ValueError("already waiting")
        if self._last_event is not None and timestamp < self._last_event:
            raise ValueError("time moved backward")
        self._opened_at = timestamp
        self._last_event = timestamp

    def admit(self, timestamp):
        if self._opened_at is None:
            raise ValueError("not waiting")
        if timestamp < self._last_event:
            raise ValueError("time moved backward")
        self.total += timestamp - self._opened_at
        self._opened_at = None
        self._last_event = timestamp

    def reset(self):
        self.total = 0.0
        self._opened_at = None
        self._last_event = None


def choose_batch(decode_ids, prefills, budget):
    if budget < len(decode_ids):
        raise ValueError("budget cannot cover active decodes")
    allocations = [(request_id, 1) for request_id in decode_ids]
    available = budget - len(decode_ids)
    remaining = []
    for request_id, tokens in prefills:
        scheduled = min(tokens, available)
        if scheduled > 0:
            allocations.append((request_id, scheduled))
        available -= scheduled
        if tokens > scheduled:
            remaining.append((request_id, tokens - scheduled))
    return allocations, remaining
````

---

<a id="material-17"></a>

## 17. Historical full interview dossier

**Source:** [amazon-aws-inference-optimization-10587705.md](amazon-aws-inference-optimization-10587705.md) · **Section:** historical

> Historical material. Its OA assumptions, past dates and daily schedules are superseded by the current November 12 phone-interview plan. Questions remain available as practice.

### Amazon AWS MLE II — interview preparation guide

**Inference-engine research update:** [32 vLLM/SGLang questions](#material-03) and [evidence/readings](#material-04). The current phone plan now assigns these within its existing domain blocks.

> **CURRENT STAGE — November 12, 2026, 2 PM EST (UTC−5):** 60-minute phone interview with Sathishkumar Sivashanmugam; live coding confirmed, recruiter says ML and LeetCode preparation. OA waived after a prior pass. Use the [current study plan](#material-01) and [AWS research supplement](#material-02). Earlier OA-first schedules below are historical.

**Current preparation schedule:** [OA-first two-week plan with daily inference fundamentals](#material-22).

> **October 28, 2026 — current stage supersedes the October 27 plan below.** Suraj reports the recruiter conversation went well. Immediate priority is the online assessment, available within two weeks: **70 minutes LeetCode-style coding, 20 minutes AI coding, 20 minutes system design, 10 minutes behavioral**. Official documentation is pending; question count, platform, assistance rules and exact expiry remain unknown. Start with the [OA question bank](#material-19), [scenario drills](#material-20) and [research ledger](#material-21). The earlier kernel-focused preparation remains relevant for later technical rounds but is not the current two-week OA plan.
>
> **Later stages, user-reported October 28:** telephone interview with 30 minutes behavioral and 30 minutes coding; then a four-hour loop with three coding rounds and one system-design round, with behavioral questions in every round. These are provisional until the official packet. No exact interview dates reported.

#### Historical preparation — October 27

**Requisition:** [10587705 — AWS Inference Optimization](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization)  
**Updated:** October 27, 2026, after the Senior Director conversation.  
**Next conversation:** Sree Natarajan, Sr. Technical Recruiter, AWS Talent Acquisition; Wednesday **October 28 at 10:30 a.m. ET** (New York EDT; 7:30 a.m. Pacific). The pasted email proposes this time; acceptance and meeting details have not been independently checked.  
**Priority:** Suraj's sole current interview-preparation target, per his October 27 instruction.  
**Start with:** [Recruiter call brief](#material-18).  
**Resume located:** [October 26 tailored PDF](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.pdf), with matching editable `.tex`. This is the role-specific artifact already linked in CareerOps; the portal upload itself was not inspected.  
**Supporting material:** [Project/PR evidence audit](#material-07), [technical revision notes](#material-08), [captured JD](#material-24).

#### 1. What we know and how it changes preparation

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

#### 2. Research findings: exact-team evidence versus adjacent accounts

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

#### 3. Tomorrow's recruiter conversation

Your objective is to turn the positive technical connection into a clearly specified next step. Be concise about fit, accurate about experience, and prepared on logistics.

##### Opening: approximately 60–75 seconds

> I'm a software engineer with nearly four years of professional experience at Oracle and Incture, and I completed my master's at NYU in May. My recent work focuses on GPU performance and LLM inference. I've built Triton attention and KV-cache kernels on H100, and contributed merged fixes to vLLM and SGLang around inference measurement and request-lifecycle correctness. My earlier work gave me a foundation in backend performance, test infrastructure and automation. I spoke with the Senior Director yesterday, and the team's focus on profiling, kernel tuning and fusion aligned closely with the work I want to do. I'm excited to understand the next steps for this role.

Use “yesterday” on October 28. Avoid claiming four years of professional GPU optimization. Your kernel work and open-source contributions are recent project experience.

##### Likely recruiter prompts [inferred from invitation/JD]

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

##### Ask these in priority order

1. “Following my conversation with the Senior Director, what is the next assessed round, and what will it cover? Is there an online assessment before the phone screen?”
2. “Could you share the round-by-round interview plan, durations and preparation material? For the coding round, is it conventional coding, AI-assisted repository work, or ML-specific implementation?”
3. “For domain coding, should I expect Python/PyTorch, Triton, CUDA/C++, or a choice? Will there be GPU execution, profiling output, or just an editor? What tools and documentation are permitted?”
4. “Does domain design emphasize an inference service, engine internals, or kernel compilation and deployment? Is there also a general ML breadth component?”
5. “How is this MLE II requisition leveled internally, and what timeline is the team targeting?”
6. Confirm location, authorization/sponsorship routing and compensation structure as time permits.

If time is short, prioritize 1–3 and necessary eligibility logistics. Ask the recruiter to obtain technical specifics from the team if she does not have them. Close: “I'm interested in moving forward. Is there anything about my background I should clarify before the technical screen, and what is the next action on each side?”

#### 4. Evidence to defend from the submitted-role resume

Candidate claims below trace to current `cv.md` and the role-specific resume; caveats come from the existing October 27 source audit. The audit is not a rerun of benchmarks. The story-provenance script was run, but its success does not override explicit uncertainty in the Oracle evidence reset.

| Story | What you should be able to explain | Boundary |
|---|---|---|
| TritonAttn | Problem shape, mapping, numerical method, bottleneck, chosen change, correctness reference, comparison and losing regimes | 13.6× is versus naive decode; peak SDPA result is a different comparison. Never present either as universal. |
| vLLM #55508 | Why TTFT and inter-arrival timestamps disagreed; tokenless trailer handling; deterministic regression tests | Metric correctness, not engine acceleration. A streaming chunk is not necessarily one token. |
| SGLang #39312 | Retraction, repeated waits, accumulation, idempotent closure, serialization/clock rebasing, retained histogram contract | Did not change scheduling policy. Existing audit records a later caller-path caveat; randomized lifecycle tests do not prove all integration paths. |
| LLMCP | Reconciliation, revision state, canary gates, insufficient evidence, queue-based scaling, rollback | Project and CPU feasibility evidence; do not imply a production GPU fleet. |
| Oracle parallel tests | Shared interface-object setup, verification versus mutation, parallel/sequential grouping, TeamCity distribution | Approximate full then-existing test pipeline: 10–11 hours to within 3. No unchanged-compute or production-throughput claim. |
| Incture | SQL plans/indexing/pools and backend design | Resume metrics need a defensible recollection of baseline, workload, measurement window and personal action before detailed retelling. |

**Kernel numbers:** retain 210 H100 tests and shape-qualified prefill results when useful. The existing report audit records peak BF16 prefill at B=4, H=16, D=128, N=16,384, non-causal, H100 80GB; verify against the report before a technical discussion. Its decode comparison wins only 2/72 SDPA configurations. The approximately 5.24× compression is an INT2 experiment; +0.33% perplexity is a separate INT4 experiment. Do not combine them into one operating point. [Prior audit and original source links](#material-07)

For each main story, prepare a six-line evidence card: **problem; my change; why this choice; proof; limitation; next experiment**. Speak the one-minute version first. Keep a five-minute technical expansion available. We still need to elicit your actual discovery sequence and rejected alternatives rather than invent them from a patch.

#### 5. Technical curriculum, ordered by the Director's signal

All exercises in sections 5–7 are **[inferred from Director/JD]**, not reported interview questions. Read for the specific task, then close the material and explain or implement it.

##### A. Profiling: diagnose before optimizing

Practice a repeatable sequence: define the workload and latency objective; reproduce; separate cold compilation from warmed execution; find time on the critical path; isolate the relevant kernel; test one explanation; remeasure correctness and end-to-end performance.

Use Nsight Systems for CPU/GPU timelines, launch gaps, transfers and synchronization. Use Nsight Compute to investigate a selected kernel's execution and memory behavior. Verify the actual launch/name/shape—you have a concrete prior audit example where the wrong reduction kernel was selected. Treat profiler replay and collection overhead separately from benchmark timing. [Nsight Systems](https://docs.nvidia.com/nsight-systems/UserGuide/index.html), [Nsight Compute profiling guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)

**Exercise P1:** a kernel is faster but serving p99 is worse. Offer competing explanations: larger batching/queue delay, another critical-path stage, launch/transfer overhead, changed output lengths, cache behavior or measurement boundaries. State which trace or controlled experiment distinguishes them.

**Exercise P2:** low occupancy and high register usage. Explain a smaller tile or changed launch configuration as a hypothesis; predict possible spills, reduced reuse or extra work. High occupancy is not the objective—lower latency for equivalent correct work is. [CUDA best practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)

**Ready when:** you can interpret a real profile for ten minutes, separate observation from hypothesis, and propose a falsifiable next experiment.

##### B. Kernel tuning and GPU fundamentals

Review coalescing, strides, tiling, register/shared-memory limits, warps, synchronization, tensor-core-friendly work and masked tails. In Triton, connect program IDs and pointer expressions to tensor coordinates; distinguish compile-time constants from runtime parameters. Tune tile sizes, warps and stages on a workload matrix rather than a single favorable shape. [Triton matmul tutorial](https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html)

**Exercise K1:** explain why a bigger tile can improve reuse yet reduce performance. **K2:** derive offsets for a strided batched tensor and handle partial tiles. **K3:** compare an under-parallelized low-batch decode kernel with a split-KV implementation, including the reduction cost.

**Ready when:** you can write and explain a small correct reduction kernel, identify its assumptions, and describe a tuning experiment without claiming a result you have not measured.

##### C. Fusion

Start with stable row softmax or residual-add plus RMSNorm. Fusion can avoid intermediate global-memory traffic and launch overhead; it can also increase live values, resource use and implementation complexity. A good answer identifies the work removed and the constraints added. [Triton fused softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)

**Exercise F1:** implement row softmax, masking padded columns with negative infinity and defining behavior for entirely masked rows. Test odd widths, extreme values and dtype tolerances. **F2:** for a proposed fused normalization path, account for reads/writes and identify whether the residual output must also be retained. **F3:** give a workload where fusion is slower and a way to detect it.

**Ready when:** you can defend a fusion boundary using correctness and measured memory/launch savings, including a losing regime.

##### D. Precompiled and workload-specialized Triton kernels

This is the most important newly identified study area. The Director's phrase could mean ahead-of-time compilation, prewarming a JIT cache, offline autotuning, or a library of specialized variants; those are related but distinct. Ask the team which they mean.

Triton's public AOT tool accepts typed signatures, specialization hints and compile-time values and produces launchable artifacts. Compilation before serving can remove request-path compilation work; it does not by itself improve the steady-state instructions of an identical kernel. [Triton AOT compiler source](https://github.com/triton-lang/triton/blob/main/python/triton/tools/compile.py)

**Proposed design exercise A1:** design a specialized-kernel registry. Define keys for operation, GPU target, dtype, shape/layout constraints, causal mode and code/compiler version. Use representative shape buckets, offline tuning, correctness checks and measured promotion. At runtime validate guards, choose a compatible variant and fall back safely on unsupported input. Track fallback frequency, cold-start time and service latency. Avoid compiling every possible combination: coverage, build cost and artifact size are competing objectives.

These registry choices are our design exercise, not a claim about Amazon's implementation. Discuss cache invalidation, version compatibility, rollout/rollback, and why an alignment assumption must be checked before dispatch. **Ready when:** you can explain cold versus warm behavior, specialization benefits, variant explosion and correctness-preserving fallback in five minutes.

##### E. Attention, decode and numerical reasoning

Be able to derive stable softmax: subtract the maximum, exponentiate and normalize. For online attention, maintain running max `m`, normalization `l`, and unnormalized output `a`. Combining a new score tile uses `m_new=max(m,max(tile))`, rescales old `l` and `a` by `exp(m-m_new)`, adds the tile's contributions, then normalizes at the end. State how masking and empty tiles are handled. [Triton fused attention](https://triton-lang.org/main/getting-started/tutorials/06-fused-attention.html)

For split-KV, partial maxima and sums must be combined under a common normalization. Simply averaging normalized partial outputs is wrong. Explain GQA's shared KV heads and why query-head mapping changes reuse. For quantization, include scales/zero points, grouping, residual storage, unpacking and quality tests. Tie each concept back to actual project evidence.

**Practice arithmetic [hypothetical inputs]:** dense KV bytes ≈ `2 × layers × batch × cached_tokens × kv_heads × head_dim × bytes_per_element`, before allocator/metadata/replication overhead. For 32 layers, batch 1, 8192 tokens, 8 KV heads, dimension 128 and BF16, this is 1 GiB. Explain how batching and quantization change it; do not use query-head count in place of KV-head count.

##### F. Serving design and broader ML coverage

Review continuous/chunked batching, KV allocation, prefix caching, prefill/decode interference, admission control, backpressure, cancellation and tail latency. Know TTFT, TPOT, throughput and request success boundaries. Compare equal work under explicit latency/quality limits.

For speculative decoding, reason about useful accepted tokens versus drafting, verification and bookkeeping cost. Distribution-preserving verification requires the appropriate sampling algorithm; “the output always matches” is too broad. [vLLM speculative decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/)

AWS's public [P-EAGLE article](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/) is a concrete parallel-drafting example. Its [llm-d article](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/) illustrates separate prefill/decode pools and the associated transfer/routing considerations. These are relevant AWS examples; exact ownership by your prospective team is unverified.

Keep a smaller fundamentals block: transformer blocks, causal masking, training versus inference, sampling, perplexity/task evaluation, quantization quality, bias/variance and overfitting. Increase this allocation only if Sree confirms ML breadth.

#### 6. Coding practice pack

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

#### 7. Domain design and behavioral preparation

##### Design mock D1: inference service under latency and cost constraints

**Prompt [inferred]:** design a service for an open-weight LLM with interactive and batch traffic, variable prompt lengths and a latency objective.

Use a 45-minute practice structure: 5 minutes requirements; 5 estimates; 10 architecture; 15 bottleneck/deep dive; 5 failure/rollout; 5 summary and tradeoffs. Clarify model, workload distribution, output limits, quality, tenant isolation, throughput and percentile SLOs before choosing optimizations.

Start with routing/admission → queue/scheduler → engine/model workers → KV management → streaming response. Separate control-plane deployment from request execution. Explain when to batch, scale, shard, quantize or disaggregate. Include memory headroom, cancellation, overload, fairness, worker failure, model-version consistency, warmup, canary evaluation and rollback. Measure completed useful work at acceptable latency, rather than maximizing raw tokens/s alone.

**Follow-ups:** What changes for long prompts? What if transfers dominate disaggregation? How do you avoid a noisy tenant consuming KV memory? Why could average throughput improve while p99 worsens? How do you compare versions with changing prompt/output distributions?

##### Design mock D2: kernel specialization and release pipeline

**Prompt [inferred]:** build a system that selects, validates, packages and deploys precompiled kernels for recurring model workloads.

Cover representative workload capture, candidate generation/tuning, numeric reference tests, hardware/version matrix, reproducible results, artifact manifests, dispatch guards, fallback, service-level validation and rollback. Explain how you prevent an optimized artifact from silently running on an incompatible layout or target. This mock directly addresses the Director's new specialization signal.

##### Behavioral evidence

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

#### 8. Preparation schedule and readiness gates

##### October 27: 100 minutes for tomorrow

- 15 min: introduction and why-team answer, twice aloud.
- 25 min: three 60-second stories—TritonAttn, vLLM, SGLang—with one limitation each.
- 15 min: professional timeline and transition; Oracle result with accurate scope.
- 15 min: actual authorization dates, location preference, start date and compensation questions.
- 20 min: mock recruiter conversation, including concise answers to gaps.
- 10 min: select recruiter questions; check invitation details and resume.

If only 30 minutes remain: 10 pitch, 10 project stories, 10 logistics/questions. Tomorrow does not require cramming a GPU textbook.

##### October 28 morning

Finish substantive study by about 9:00–9:30 ET. At 10:15, skim the brief, check call details and settle in. Be ready at 10:25. Record answers and next steps immediately afterward.

##### Provisional 14-day technical plan

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

#### 9. Next actions and open questions

- [ ] Confirm tomorrow's invitation/connection details.
- [ ] Rehearse the recruiter brief aloud.
- [ ] Capture Sree's exact round format, languages, allowed tools, dates and internal level.
- [ ] Build factual incident cards; recover genuine discovery/decision history for kernel and PR work.
- [ ] Retrieve original benchmark artifacts before quoting detailed performance figures.
- [ ] Start baseline timed practice after recruiter clarification.

The interview outcome remains an ongoing goal. This guide completes the initial research/preparation deliverable; it does not imply interview readiness has already been demonstrated or interviews scheduled.

---

#### Historical preparation retained below

The following October 26–27 material is preserved for its evidence and source links. Its scheduling instructions and earlier stage assumptions are historical; the update above governs the October 28 recruiter call and subsequent preparation.

### Interview Intel: Amazon AWS — Machine learning engineer II, Inference Optimization

**URL:** https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization
**Requisition:** 10587705
**Legitimacy:** unknown formal evaluation tier; live title, full JD and Apply now verified at Amazon.jobs on October 26, 2026. Recruiter conversation supplied directly by Suraj; email headers were not independently inspected.
**Report:** N/A — standalone CV and interview preparation, no application submission or tracker status change.
**Researched:** 2026-10-26
**Sources:** 0 Glassdoor reviews, 0 Blind posts, public primary sources listed below and in the October 27 revision plan, current primary CV/profile, and the user-pasted recruiter thread. No team-specific interview reports established.
**Audiences covered:** recruiter-screen; hiring-manager and peer-tech follow-up preparation clearly labeled as inferred. No panel or later-round format confirmed.
**Candidate email:** sm12377@nyu.edu
**Revision notes:** [Lecture/book concepts, likely questions and project connections](#material-08) — added October 27, 2026.
**Project/PR audit:** [Highlights, final patches, review decisions and deep-dive order](#material-07) — October 27; includes later SGLang coverage caveat and separation of INT2 compression from INT4 quality results.
**Resume:** [Tailored PDF](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.pdf)
**JD archive:** [Captured posting](#material-24)

#### Historical October 26 preparation for the October 27 informational call

Sadaf Fardeen offered a **30-minute informational phone chat**, then sent this requisition and asked you to apply. That is the confirmed format from your thread. Coding, a formal technical screen, internal level, remaining rounds, and hiring timeline are not confirmed. Prepare for fit and logistics, with a short technical explanation ready if she probes. Amazon's general guide describes initial screens as potentially covering qualifications, technical validation, behavior and compensation; it does not establish this team's agenda. [Amazon interview guide](https://www.aboutamazon.com/news/workplace/amazon-interview-guide)

**Time: Tuesday, October 27, 2026.** She wrote “2 PM PST.” On that date Los Angeles observes PDT, so **2 PM local Pacific = 5 PM New York EDT**. Literal PST would instead mean 6 PM EDT. This conversion was checked with Python's `zoneinfo` for America/Los_Angeles and America/New_York; her intended timezone needs confirmation.

Suggested manual confirmation:

> Hi Sadaf, thank you for sharing the opening. Just confirming our call tomorrow, Tuesday October 27, is at 2 PM Pacific / 5 PM Eastern. I look forward to speaking with you.

Phone provided in the thread: **+1 551-371-2172**. Keep it available, allow unknown callers, and have the job page, new PDF and your notes open. No meeting invite or calendar event was inspected or created.

#### Your objective and best positioning

**Get Sadaf comfortable presenting you to the hiring manager as a software engineer with relevant GPU-inference evidence.** The differentiator is the combination of attention/KV-cache kernels, upstream measurement correctness, and professional software engineering. Avoid presenting yourself as someone with four years of professional GPU/MLE experience: the professional work was backend engineering, test infrastructure and automation; GPU/LLM work is recent project and open-source experience. [Primary source: current cv.md and profile]

The team explicitly needs vLLM/SGLang development, CUDA tuning, model servers, benchmarking and price-performance improvements for Qwen/Gemma/gpt-oss across SageMaker, Bedrock and HyperPod. Your kernel project and upstream contributions make this a credible conversation. They do not establish prior employment on those AWS products. [Exact JD](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization)

##### 60–90-second introduction

> I'm a software engineer with nearly four years of professional experience at Oracle and Incture, and I completed my master's at NYU this May. My recent work has focused on GPU performance and LLM inference.
>
> I built Triton attention and KV-cache kernels covering prefill, split-KV decoding and quantization, with 210 tests passing on H100. The prefill kernel reached 433 TFLOP/s BF16 and 1.1–1.3 times PyTorch SDPA at long sequence lengths. I used Nsight Compute to investigate register-pressure and occupancy bottlenecks and checked integration through token-identical greedy generation.
>
> I've also contributed merged fixes to vLLM and SGLang, particularly around reliable inference latency and scheduler queue-time measurement. My earlier work gives me a foundation in backend performance, automation and testing. This role interests me because it connects the kernel and serving-stack work I've been doing to customer-facing inference performance at AWS.

All personal claims above trace to the current master CV. Practice the introduction aloud; leave a pause after each paragraph. Do not read every test count in the first answer.

##### Why this role / why AWS? [inferred from JD]

> The work spans the layers I most want to work on: kernels, inference engines, and the measurement that tells us whether a change actually improves serving. I've worked on those layers through TritonAttn, vLLM, SGLang and my LLM control-plane project. I'm especially interested in taking that work into production, where an optimization has to improve price-performance while preserving correctness and latency expectations.

Optional research detail, after reading the articles: AWS has published work on parallel speculative drafting integrated into vLLM, and Kubernetes-based disaggregated inference with llm-d. Those are concrete examples of the JD's direction, **not proof that Sadaf's exact team authored or owns them**. [AWS P-EAGLE](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/), [AWS llm-d](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/)

#### Requirements: what you can defend and what needs care

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

#### Prepare three evidence stories

##### October 26 rehearsal cards: short answer first, depth on request

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

##### 1. H100 kernel work: the lead technical story

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

##### 2. vLLM and SGLang: make trustworthy measurement the story

**Headline:** “An inference optimization is only useful if the latency accounting is correct.”

For [vLLM #55508](https://github.com/vllm-project/vllm/pull/55508), explain the first-token timestamp, tokenless usage trailers, and the invariant **E2E − TTFT = sum of inter-token intervals** for the measured decode window. You added 12 new tests and validated 8 siblings. This was measurement correctness; do not claim it made the model intrinsically generate faster.

For [SGLang #39312](https://github.com/sgl-project/sglang/pull/39312), explain how retraction/preemption creates multiple waiting intervals. You accumulated those waits, handled idempotent closure/chunked prefill and process-clock rebasing, and preserved scheduling behavior and the histogram contract. Evidence: six new tests, 303 related tests, 20,000 randomized lifecycles and 9,504 non-retracted compatibility cases. **No scheduling-policy change.**

Keep [vLLM #62205](https://github.com/vllm-project/vllm/pull/62205) as the serving-debuggability example: correlated delta/full/final output logging, 53 focused and 281 broader tests. [#62204](https://github.com/vllm-project/vllm/pull/62204) documents/tests existing retry byte-budget behavior; it is not a claim of inventing a security mechanism. [Current cv.md, open-source projects]

Prepare one genuine maintainer-review decision from memory or the PR, including the change you made and why. No specific disagreement or review incident has been established in this brief.

##### 3. Oracle: professional ownership and a real tradeoff

**Headline:** “I redesigned test execution and object lifecycles, reducing execution of the then-existing full pipeline from approximately 10–11 hours to within three hours.”

Explain shared setup for dependent interface objects, verification versus state-mutating tests, parallel/sequential grouping in JUnit 5, and suite distribution with TeamCity. Saved time enabled more testing. This is **test execution improvement**, not production database throughput; unchanged compute cost/hardware is not established. [Current cv.md; story bank O1]

Useful challenge/reflection: interleaved logs became harder to investigate, so you researched attribution-capable Java logging and wrote a class-based log organization script. The work took roughly five to six months while tests grew. You would establish authoring guidelines earlier and account for growing compute needs. [Current profile and story bank O1/O2]

Backup automation example: you adapted existing Terraform scripts and personally wrote readiness, artifact-collection and cleanup scripts. Cleanup ran despite earlier failures. Discuss the tradeoff honestly: deleting an instance after artifact-copy failure can lose local diagnostics; guaranteed artifact preservation, successful deletion under every failure, and a retry/fallback mechanism are not established. [Current profile; story bank O3]

#### Likely recruiter prompts and concise answers

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

#### Five useful questions for Sadaf

Suggested questions **[inferred from JD / recruiter context]**; pick three or four if time is short.

1. “How is this MLE II opening leveled internally, and what distinguishes a strong mid-level candidate from the senior profile in your post?”
2. “What is the balance between hands-on kernels, vLLM/SGLang engine development, and AWS service integration? Which is the biggest immediate need?”
3. “Would my kernel projects plus merged inference-stack work be relevant to the manager's current priorities? Where would they want stronger evidence?”
4. “What would the next stages assess: general coding, CUDA/Triton, C++/Python, inference/system design, and Leadership Principles? Is there an assessment before a technical conversation?”
5. “Could we confirm the Santa Clara work arrangement, work-authorization/sponsorship eligibility and expected hiring timeline? If the fit looks promising, what should I send for the manager review?”

Optional technically specific question if she knows the team: “AWS has published work on P-EAGLE and llm-d. Does this team focus on related problems, or a different part of the serving stack?” Do not ask her to disclose confidential details. [AWS P-EAGLE](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/), [AWS llm-d](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/)

Closing line:

> Based on what we've discussed, do you see a fit worth taking to the hiring manager? Is there anything in my background you'd want me to clarify before that review?

#### Technical refresher: enough for tomorrow, deeper for a later round

All exercise prompts are **[inferred from JD]**. These are preparation topics, not a claim that tomorrow includes coding.

##### Speculative decoding

A drafter proposes several tokens; the target verifies them. Standard exact speculative sampling uses acceptance/rejection and correction to preserve the target distribution in theory; greedy equality and numerical behavior need validation. Gains depend on accepted tokens per target pass versus drafting, verification and bookkeeping overhead. It can lose when acceptance is low or the baseline is already well utilized. vLLM distinguishes standard rejection-sampling guarantees from relaxed-verification variants. [vLLM documentation](https://docs.vllm.ai/en/latest/features/speculative_decoding/)

AWS's P-EAGLE article describes generating multiple draft tokens in one pass, rather than a serial drafter forward pass per token, plus fused Triton work for draft-batch preparation. Read for the principle and tradeoffs; do not memorize its headline speedup as if workload-independent. [AWS P-EAGLE](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/)

**Practice:** “When could speculative decoding make serving slower, and how would you isolate why?”

##### Disaggregated prefill/decode

Separate prompt processing and token generation so they can be provisioned and scaled independently. Review the different resource profiles, KV-cache transfer overhead, queue imbalance and routing/cache locality. AWS's llm-d example connects vLLM, Kubernetes, NIXL and EFA/libfabric; do not treat NCCL collectives and point-to-point KV transfers as interchangeable abstractions. Whether this team's implementation uses that stack is unknown. [AWS llm-d](https://aws.amazon.com/blogs/machine-learning/introducing-disaggregated-inference-on-aws-powered-by-llm-d/)

**Practice:** “When does separating prefill and decode help, and when could transfer or coordination costs outweigh the benefit?”

##### Kernels, measurement and product impact

- Explain online softmax, tiling and shared/register/global memory tradeoffs using your actual attention implementation. [CV; inferred follow-up]
- Explain split-KV's extra parallel work and reduction overhead. Show a winning and a losing regime from your real measurements. [CV; inferred follow-up]
- Explain why lowering register pressure or raising occupancy is not automatically a performance win: measure the effect on spills, memory traffic, work per block and kernel duration. [Inferred technical exercise from profiling requirement]
- Walk from request arrival through queueing, prefill, first token, decode, finish and tokenless trailers; define the timing boundaries you corrected. [vLLM CV evidence]
- Propose a benchmark matrix across model, prompt/output length, concurrency, dtype, backend and latency targets. Keep warmup/compilation separate and compare equivalent work. This is a proposed method, not a claim about undocumented past runs. [Inferred from JD]
- Translate kernel speed into useful completed requests/tokens per dollar under TTFT/TPOT/tail-latency and quality constraints. A faster microkernel can fail to improve the whole service. [Inferred from JD's price-performance ownership]
- Refresh transformer inference versus training, KV-cache scaling, GQA/MQA and the memory/accuracy tradeoff of cache quantization. Have GRPO/LoRA available as secondary evidence of training fundamentals, not the lead story. [CV; inferred from JD]

#### Behavioral story routing

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

#### Tonight: a focused two-hour plan

This is a suggested study sequence, not a scheduled task.

1. **15 min:** Practice the introduction and “why this role” aloud twice. Aim for clarity before adding numbers.
2. **35 min:** Recover the H100 benchmark configuration, one profile and one honest limitation. Be able to explain what the measured speedup does and does not establish.
3. **20 min:** Review vLLM #55508 and SGLang #39312: failure, personal change, invariant, tests and scope boundary. Have the other two vLLM PRs ready as backups.
4. **20 min:** Review speculative decoding and disaggregated inference from the linked primary sources. Practice the two “when does it lose?” questions.
5. **20 min:** Rehearse Oracle O1 and one genuine challenge using personal actions and the corrected test-runtime metric.
6. **10 min:** Confirm timezone, phone, relocation, exact work-authorization dates, start date and your three best questions. Apply with the new resume if you choose to proceed, and retain the application confirmation.

**If you have only 45 minutes:** 10 minutes pitch, 15 minutes benchmark evidence, 10 minutes one PR, 10 minutes logistics/questions. The informational call does not justify substituting hours of unrelated algorithm practice for these basics.

#### After you apply / after the call

Only use the following once the application is actually submitted:

> Hi Sadaf, I've applied for Machine Learning Engineer II, AWS Inference Optimization, requisition 10587705, using sm12377@nyu.edu. I've attached an updated resume with more detail on my H100 attention/KV-cache kernels and merged vLLM/SGLang contributions. Thank you for sharing the opportunity; I look forward to our conversation.

After the call, record the confirmed level, team scope, format of next round, timeline, location and authorization guidance here. If the next round is technical, build a separate practice session from what Sadaf confirms rather than assuming a generic Amazon loop.

#### Public sources and limits

##### Revision resources — October 27, 2026

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

---

<a id="material-18"></a>

## 18. Historical recruiter-call brief

**Source:** [amazon-10587705-recruiter-brief.md](amazon-10587705-recruiter-brief.md) · **Section:** historical

> Historical material. Its OA assumptions, past dates and daily schedules are superseded by the current November 12 phone-interview plan. Questions remain available as practice.

### Amazon MLE II — recruiter call brief

**Wednesday, October 28, 2026 · 10:30 a.m. ET · Sree Natarajan, AWS Talent Acquisition**  
Time proposed in pasted email; check acceptance and call details.  
[Full preparation guide](#material-17) · [Role-specific resume](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.pdf)

**Objective:** explain fit clearly, resolve logistics, and leave with a concrete next interview step.

#### Your opening

> I'm a software engineer with nearly four years of professional experience at Oracle and Incture, and I completed my master's at NYU in May. My recent focus is GPU performance and LLM inference: Triton attention and KV-cache kernels on H100, plus merged vLLM and SGLang contributions to measurement and request-lifecycle correctness. I spoke with the Senior Director yesterday, and the team's focus on profiling, kernel tuning and fusion aligned closely with my work. I'm excited to learn about the next steps.

#### Three proof points

- **Kernels:** Triton prefill/decode/KV-cache work; 210 H100 tests; shape-dependent prefill gains against SDPA. Explain one engineering choice if asked.
- **vLLM:** aligned streaming latency measurements so timestamps and tokenless trailers did not create inconsistent timing windows. This was measurement correctness, not engine acceleration.
- **SGLang:** fixed wait accounting across queue re-entry and repeated lifecycle transitions while preserving existing metric semantics. Explain tests and coverage boundaries if probed.

Candidate sources: current `cv.md`; technical caveats in the [project audit](#material-07). Keep your professional systems experience distinct from recent GPU/open-source project work.

#### Questions to prioritize

1. What is the next assessed round? Is an OA required before the technical phone screen?
2. What are the loop rounds, durations and preparation materials? Does “AI coding” mean AI-assisted debugging, ML implementation, or general coding?
3. For domain coding: Python/PyTorch, Triton, CUDA/C++, or a choice? GPU execution or editor only? Which tools/docs are permitted?
4. For domain design: inference service, engine internals, kernel deployment, or broader ML design?
5. Internal level, scheduling timeline, Santa Clara work arrangement and authorization/sponsorship routing?

#### Logistics and compensation

Have your real current authorization type/expiration, future sponsorship needs, relocation preference, earliest start date and genuine competing deadlines ready. Saved profile only establishes F-1; do not guess additional dates.

The [posting](https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization) lists **$165,200–$223,600 Santa Clara base**, plus sign-on and RSUs. Say: “Could you share the expected total compensation structure and internal level for this requisition? I'd like to calibrate to the role's scope and full package.” No personal target is established in CareerOps.

**Close:** “I'm interested in moving forward. Is there anything I should clarify before the technical screen, and what is the next action on each side?”

#### Notes to fill immediately afterward

- Next stage / date / duration:
- OA required:
- Coding language / environment / AI policy:
- Domain coding and design scope:
- ML breadth / LP expectations:
- Internal level / location / authorization discussion:
- Compensation discussed, if any:
- Next action, owner and timing:

---

<a id="material-19"></a>

## 19. DSA/OA question bank — OA stage waived

**Source:** [amazon-10587705-oa-question-bank.md](amazon-10587705-oa-question-bank.md) · **Section:** historical

> Historical material. Its OA assumptions, past dates and daily schedules are superseded by the current November 12 phone-interview plan. Questions remain available as practice.

### Amazon MLE II — online assessment question bank

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](#material-01).

**Current daily schedule:** [Combined two-week study plan](#material-22). This supersedes earlier daily sequencing; question IDs remain unchanged.

**Updated:** October 28, 2026 · **Role:** AWS Inference Optimization, 10587705  
**Scope:** OA only. Research-informed practice, not a prediction of an exact test. No verified account for this exact requisition was found.

#### Start here

The recruiter call went well, per Suraj. His report sets the working format: **70 minutes coding + 20 minutes AI coding + 20 minutes system design + 10 minutes behavioral**. The number of coding questions, platform, permitted languages/frameworks, AI boundaries, scoring, and whether sections are separately timed remain unconfirmed. The official invitation will supersede this plan.

Suraj has two weeks to take the assessment. **November 11 is a planning estimate**, not a verified expiry. Target a practice-ready date of November 8; use the actual invitation for the deadline. Later telephone and loop rounds are recorded in the main dossier but are outside this bank.

Amazon's public **SDE II** OA page describes a different structure (90-minute coding, design and workstyle). That is adjacent guidance, not authority for this MLE invitation. [Official SDE II OA guidance](https://www.amazon.jobs/content/en/how-we-hire/sde-ii-oa-prep)

**Priority:** P0 = first pass; P1 = coverage after P0; P2 = stretch after diagnosing weaknesses. Priority measures training value, not claimed Amazon frequency. All LC rows below are **practice recommendations**; report mappings are separately identified. Use [NeetCode's curriculum](https://neetcode.io/practice/practice/neetcode150) for explanations after an attempt, not as evidence of Amazon frequency.

**Today:** attempt LC 560 and 994 in one 70-minute session, then AI-01 (20 min), SD-01–04 (20 min total), and a 10-minute workstyle practice. Log errors before reading solutions. These form a diagnostic; they are not a pass prediction.

#### Supplementary domain preparation

The [cross-company ML/inference bank](#material-05) covers transformers, attention, vLLM/SGLang, kernel optimization and ML engineering in coding, design, conceptual and case-study formats. These are broader technical-round exercises, not newly confirmed OA requirements.

#### A. LeetCode practice bank — 38 questions

The time column is an individual practice cap in minutes. First attempt without AI or editorials; at the cap, record the blocker, study the missing idea, and re-solve from scratch 48 hours later. Solve with the actual platform's function signature once known.

| ID | Priority | Problem | Pattern | Difficulty | Cap |
|---|---|---|---|---|---|
| LC-01 | P0 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | sliding window | M | 20 |
| LC-02 | P0 | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | frequency signatures | M | 15 |
| LC-03 | P0 | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | prefix/suffix | M | 20 |
| LC-04 | P0 | [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | prefix sum + hash | M | 25 |
| LC-05 | P0 | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | heap / buckets | M | 20 |
| LC-06 | P0 | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | three-way partition | M | 20 |
| LC-07 | P0 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | sorting intervals | M | 20 |
| LC-08 | P0 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | greedy proof | M | 25 |
| LC-09 | P0 | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | monotonic stack | M | 25 |
| LC-10 | P0 | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | binary search feasibility | M | 25 |
| LC-11 | P0 | [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | binary search feasibility | M | 25 |
| LC-12 | P0 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | grid traversal | M | 20 |
| LC-13 | P0 | [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | multi-source BFS | M | 25 |
| LC-14 | P0 | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) | topological ordering | M | 25 |
| LC-15 | P0 | [198. House Robber](https://leetcode.com/problems/house-robber/) | DP state | M | 20 |
| LC-16 | P0 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | unbounded DP | M | 25 |
| LC-17 | P0 | [139. Word Break](https://leetcode.com/problems/word-break/) | prefix DP | M | 25 |
| LC-18 | P0 | [55. Jump Game](https://leetcode.com/problems/jump-game/) | greedy invariant | M | 20 |
| LC-19 | P0 | [134. Gas Station](https://leetcode.com/problems/gas-station/) | greedy restart proof | M | 25 |
| LC-20 | P0 | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | DP / binary search | M | 30 |
| LC-21 | P1 | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | heap / selection | M | 25 |
| LC-22 | P1 | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | heap / sorting | M | 20 |
| LC-23 | P1 | [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) | greedy counting | M | 30 |
| LC-24 | P1 | [763. Partition Labels](https://leetcode.com/problems/partition-labels/) | greedy boundaries | M | 20 |
| LC-25 | P1 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | binary search | M | 25 |
| LC-26 | P1 | [15. 3Sum](https://leetcode.com/problems/3sum/) | sort + two pointers | M | 25 |
| LC-27 | P1 | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | hash set | M | 20 |
| LC-28 | P1 | [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra | M | 30 |
| LC-29 | P1 | [46. Permutations](https://leetcode.com/problems/permutations/) | backtracking | M | 20 |
| LC-30 | P1 | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS | M | 20 |
| LC-31 | P1 | [146. LRU Cache](https://leetcode.com/problems/lru-cache/) | hash + linked list | M | 30 |
| LC-32 | P1 | [1561. Maximum Number of Coins You Can Get](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) | sorted grouping greedy | M | 25 |
| LC-33 | P2 | [1526. Minimum Number of Increments on Subarrays to Form a Target Array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/) | difference-based greedy; NOT prefix-zero variant | H | 30 |
| LC-34 | P2 | [3413. Maximum Coins From K Consecutive Bags](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/) | weighted interval window | M | 35 |
| LC-35 | P2 | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | monotonic deque | H | 30 |
| LC-36 | P2 | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | monotonic stack | H | 35 |
| LC-37 | P2 | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | frequency window | H | 35 |
| LC-38 | P2 | [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | two pointers | H | 30 |

For every solution: state the invariant, derive complexity, test a smallest legal input, duplicates, boundaries, and worst-case input size. Know why an attractive wrong solution fails. Re-solving remembered code does not count as an unseen diagnostic.

#### B. Candidate-reported OA families — separate from canonical practice

Sources and limitations are in [the research ledger](#material-21). All accounts are self-reported and adjacent to this role. Prompts below are brief paraphrases; follow the linked original for supplied constraints. Do not silently fill missing constraints.

| ID | Family / exercise | Evidence | How to use |
|---|---|---|---|
| R-01 | Choose a fixed-length base string whose repeated copies cover required character frequencies; minimize repetitions, then lexicographic order. | S02: Jul 16, 2026; level/location unspecified | P1, 35 min. Derive a feasibility predicate from counts; distinguish coverage from exact equality. |
| R-02 | Add at most one grid center to minimize the worst distance to a center; eight-direction distance. | S03: Jul 9, 2026; unspecified | P2, 40 min. Multi-source distance computation and feasibility geometry. Do not substitute four-neighbor Manhattan distance. |
| R-03 | Transfer excess server load into spare capacity while minimizing the largest transfer distance. | S04: Jun 5, 2026; incomplete constraints | P2 discussion only until movement/splitting semantics are established; never memorize an unverified feasibility algorithm. |
| R-04 | Remove entries to maximize values equal to their new one-based positions. | S05: SDE I, Bengaluru, invitation Mar 23, 2026 | P1, 35 min. Derive a subsequence DP; do not assume ordinary LIS directly solves it. |
| R-05 | Make an integer array zero by adding/subtracting one from a prefix per operation. | S05; same report as R-04 | P0, 25 min. Work right-to-left on differences. LC 1526 is a related exercise with DIFFERENT allowed operations. |
| R-06 | LC 3413 named by a commenter in a recent OA thread. | S06: weak single comment, no verified level/date | P2; use LC-34. One comment does not establish prevalence. |
| R-07 | Three-way partition, sliding-window and DP themes described in recent OA discussion. | S07: one discussion cluster | Supports coverage of LC-06, LC-01 and DP; not exact repeated questions or independent frequency counts. |

**R-05 self-check (our derivation):** for a nonempty array a, optimum is `abs(a[-1]) + sum(abs(a[i]-a[i+1]))`. A prefix operation changes one adjacent difference, or the final value for a full prefix; each needs that many unit changes. Check `[1,2] → 3`, `[0,0] → 0`, `[-1,1] → 3`. This formula does not apply to arbitrary-subarray increment problems.

#### C. Distributed systems — 24 short scenarios

These are **original practice scenarios**, not claimed leaked/reported Amazon questions. An older candidate described a live-view-counter simulation with storage/prioritization choices (S08); recent discussion also mentions effectiveness ratings (S07). That supports practicing concise decisions, but does not establish your exact UI.

Use [scenario prompts and answer checkpoints](#material-20). Each SD question takes 4–5 minutes: identify the requirement, pick a design, name its failure mode, and explain one tradeoff. Four scenarios make a 20-minute block. Do not spend this block drawing an entire large-system architecture unless the official instructions request it.

#### D. AI-assisted coding — 12 drills

Use [the detailed drill specifications](#material-20). These are original bounded practice tasks inspired by repo debugging reports, not a claim that this MLE test uses a particular backend framework. Reported 40/60 or 100-minute assessments differ from your 20-minute AI section; train to your recruiter's timing.

Practice in an existing small local application and its tests. For a fresh mock, have a helper seed the described defect without showing the patch. The bank supplies requirements and acceptance cases, not a runnable hidden-test repository. Choose the strongest offered language after the packet arrives; do not spend the next fortnight learning an unconfirmed framework.

20-minute routine: 0–3 read task/run baseline; 3–6 reproduce and inspect the failing path; 6–13 request and review a small patch; 13–18 run targeted plus regression tests; 18–20 inspect diff and explain remaining limitations. During practice use AI for this section only; the invitation decides what assistance is allowed in the actual assessment.

Useful prompt: “Read these requirements and failing tests. Identify the smallest likely cause, cite the relevant code, and propose a minimal patch. Preserve public APIs. Add a regression case for the failure; explain behavior at boundaries.” Reject patches that weaken tests, hard-code examples, or rewrite unrelated modules.

#### E. Two-week sequence

Budget assumption: roughly 2.5–3 hours on study days. If less time is available, keep P0 and timed mocks; remove P2 first. Readiness is measured by fresh attempts and error recurrence, not completion count.

| Day/date | Coding focus | 20-min AI | 20-min design |
|---|---|---|---|
| 1 · Oct 28 | Diagnostic LC-04 + LC-13, 70 min | AI-01 | SD-01–04 |
| 2 · Oct 29 | LC-01,02,03 | AI-02 | SD-05–08 |
| 3 · Oct 30 | LC-05,06,07; re-solve misses | AI-03 | SD-09–12 |
| 4 · Oct 31 | LC-08,09,10 | AI-04 | SD-13–16 |
| 5 · Nov 1 | LC-11,12,14 | AI-05 | SD-17–20 |
| 6 · Nov 2 | LC-15,16,17 | AI-06 | SD-21–24 |
| 7 · Nov 3 | Full 120-minute mock: LC-18 + LC-20 | AI-07 | Random 4, hide checkpoints |
| 8 · Nov 4 | LC-19, R-05; repair mock weaknesses | AI-08 | Four weakest scenarios |
| 9 · Nov 5 | LC-21,22,24,25 as time allows | AI-09 | Consistency + failures |
| 10 · Nov 6 | LC-26,27,28; redo failed P0 | AI-10 | Storage + scale |
| 11 · Nov 7 | Full mock: unseen LC-23 + LC-32 | AI-11 | Random 4 |
| 12 · Nov 8 | R-01 + R-04; optional P2 | AI-12 | Explain tradeoffs aloud |
| 13 · Nov 9 | Fresh variant mock, selected from weaknesses | Repeat weakest with changed inputs | Random 4 |
| 14 · Nov 10 | Light error-log review; environment/invitation check | Review workflow | Review principles |

Reserve Nov 11 only if the actual expiry permits it. Move the assessment earlier if ready; don't rely on an inferred deadline. Mock pairings are our training structure, not confirmation that the coding section contains two questions.

**70-minute coding strategy:** spend the first 5 minutes reading all available questions. If there are two, budget about 25 minutes for the more tractable, 30 for the other, and 10 for testing/submission. Adapt to actual weights and constraints. After 10 minutes without a viable approach, simplify, write a small brute-force oracle during practice, or switch questions.

**10-minute behavioral practice:** read workstyle statements literally and answer consistently with real behavior. For scenario items, identify customer impact, facts needed, ownership and a concrete next step. Use the existing truthful story bank if written responses are requested. Do not assume a STAR essay or reverse-engineer a supposed “correct personality.”

**Practice readiness heuristic (not Amazon's bar):** two fresh timed coding sessions with correct implementations and boundary tests; a bounded AI fix without regressions in 20 minutes; four design decisions in 20 minutes with explicit tradeoffs. Log actual outcomes in [attempts.csv](#material-23). All items start unattempted; no readiness inferred from existing job experience.

#### Maintenance

Research baseline: Oct 28. Desired refresh every three days: Oct 31, Nov 3, Nov 6, Nov 9, continuing until OA completion or a user change. Consult the automation's displayed schedule for actual run timing. Preserve IDs and attempts; add dated evidence and retire weak claims rather than silently replacing them. See the source ledger for selection rules.

##### Change log
- 2026-10-28: Initial OA-only bank: 38 canonical coding exercises, 7 reported families, 24 distributed-system scenarios, 12 AI coding drills; recruiter format recorded pending official packet.

---

<a id="material-20"></a>

## 20. OA system-design and AI exercises — historical format

**Source:** [amazon-10587705-oa-scenarios.md](amazon-10587705-oa-scenarios.md) · **Section:** historical

> Historical material. Its OA assumptions, past dates and daily schedules are superseded by the current November 12 phone-interview plan. Questions remain available as practice.

### OA scenario and AI coding drills

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](#material-01).

Updated October 28, 2026. Companion to [the question bank](#material-19). Every prompt here is an **original practice exercise**. Checkpoints are suggested answers under the stated assumptions, not Amazon scoring keys. Hide them during a mock.

#### Distributed systems scenarios

Score each practice response 0–2 on requirement fit, correctness under failure, and explicit tradeoff (6 total). This is a learning rubric, not an assessment cutoff. P0: SD-01–16. P1: SD-17–24.

##### SD-01 — Live audience counter
A broadcast attracts 2 million viewers. The displayed audience count may lag five seconds, but a single popular broadcast must not overload one database key. Pick between one synchronous counter, sharded counters with periodic aggregation, and calculating the count by scanning all sessions on every request.

**Checkpoint:** Shard increments and aggregate for display; define viewer/session expiry and duplicate handling. A single counter can become hot; scanning is expensive. An approximate display requirement differs from billing accuracy. Synthetic scenario inspired by S08's broad counter theme.

##### SD-02 — Last item in inventory
Two customers buy the last unit concurrently. Both previously read stock=1. Is adding a strongly consistent read sufficient? Propose the write path.

**Checkpoint:** No: a read followed by a separate write still races. Use an atomic conditional decrement or transaction, with request idempotency. Decide reservation expiry and cancellation semantics. Strong reads help freshness, not atomicity of a later action.

##### SD-03 — Payment timeout
A payment request times out after the server might have committed it. Compare blind retry, abandoning the order, and retrying with a stable request key.

**Checkpoint:** Persist an idempotency key and operation outcome atomically where possible; reuse it for the same intent and reject conflicting payloads. Reconcile uncertain outcomes. “Timeout” does not prove failure. [AWS idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

##### SD-04 — Duplicate queue delivery
A worker sends a notification and crashes before acknowledging the queue message. How should a redelivery be handled?

**Checkpoint:** Record a durable operation identity and make the effect deduplicatable. A database flag written after an external send leaves a crash window; use a downstream idempotency capability or an explicit reconciliation design. Do not claim queue selection alone makes external effects exactly once. [SQS delivery semantics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html)

##### SD-05 — Product page cache
Catalog reads tolerate 30 seconds of staleness. A promotion creates a surge on one item. Select a caching policy and explain what happens when that entry expires.

**Checkpoint:** Cache-aside with bounded TTL; coalesce concurrent refreshes and jitter expiration to avoid a stampede. Define invalidation on writes and fallback behavior. A cache must not become the authority for stock correctness.

##### SD-06 — Read after profile update
A customer saves a new display name and immediately sees the old value from a replica. What are two remedies, and what do they cost?

**Checkpoint:** Read from an authoritative/strongly consistent path, or preserve session read-your-writes with a version/token strategy. Avoid promising strong reads on unsupported indexes. A DynamoDB GSI is eventually consistent. [DynamoDB consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)

##### SD-07 — Retry storm
A dependency's error rate rises, and clients retry immediately three times at every service layer. What do you change first?

**Checkpoint:** Bound attempts and total elapsed time, apply backoff/jitter, retry only appropriate failures and safe operations, and prevent retry multiplication across layers. Admission control may be needed. More retries can worsen overload. [AWS retries and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)

##### SD-08 — Worker backlog
Arrival rate is 1,200 jobs/s; 40 workers each complete 20 jobs/s. Estimate backlog growth and choose a signal for scaling.

**Checkpoint:** Capacity 800/s; backlog grows 400/s, or 24,000/min under these assumptions. Track oldest-job age and queue depth alongside throughput. At least 60 workers merely match average arrival, with no safety margin or backlog drainage. Scaling is constrained by downstream capacity.

##### SD-09 — Tenant rate limits
Ten application instances serve a customer with a global 100 requests/s limit. Would a local 100/s limiter on each instance enforce it?

**Checkpoint:** No, the aggregate could approach 1,000/s. Use shared atomic state or partitioned quotas with a defined error bound. Token bucket allows bounded bursts; strict fixed windows have boundary effects. Define fail-open versus fail-closed based on product requirements.

##### SD-10 — Partition key choice
Order records are mostly fetched by order ID; one enterprise customer creates half the traffic. Compare customer ID and high-cardinality order ID as primary partition keys.

**Checkpoint:** Start from access patterns and load distribution. Customer ID may create a hot partition; order ID spreads traffic but customer listing needs another index or bounded fan-out. Salting also imposes read complexity.

##### SD-11 — Durable upload
Users upload 500 MB videos and edit small metadata. Choose storage and describe the failure between uploading bytes and saving metadata.

**Checkpoint:** Object storage for bytes, a database for metadata, explicit upload states and checksums, and cleanup for orphaned objects. Prefer direct signed upload when appropriate. Do not promise an atomic transaction across unrelated services; reconcile partial completion.

##### SD-12 — AZ failure
The service must survive losing one availability zone. Why are three app replicas in the same zone insufficient?

**Checkpoint:** Spread app and data replicas across failure domains, provision failover capacity, and use health-aware routing. Test database quorum/failover behavior, not just the web tier. Replicas are also not a substitute for recoverable backups.

##### SD-13 — Ordering shipments
Shipment events arrive out of order; ordering matters per shipment, not across all shipments. Pick partitioning and state-update rules.

**Checkpoint:** Partition by shipment identity; retain event sequence/version, reject stale state transitions, and deduplicate. Event time alone may tie or reflect skew. Global ordering reduces parallelism unnecessarily for this requirement.

##### SD-14 — Commit plus publish
An order is committed in the database, but publishing its event fails. What avoids silently losing the event?

**Checkpoint:** Transactionally write order and outbox record together; relay asynchronously with retries and idempotent consumers. Account for relay duplicates and lag. A simple “save then publish” sequence has a failure gap.

##### SD-15 — Search index lag
A product write succeeds, but search does not show it for ten seconds. Is this necessarily data loss? How should the product behave?

**Checkpoint:** Distinguish indexing lag from loss, measure freshness and failed indexing, and provide authoritative detail reads when required. Eventual search is acceptable only if the requirement permits it. Rebuild/replay capability helps recovery.

##### SD-16 — Inference overload
Requests must finish within two seconds. The GPU worker queue is already five seconds deep. Choose between queueing indefinitely, rejecting excess traffic, and increasing batch size without a bound.

**Checkpoint:** Deadline-aware bounded admission, backpressure, and explicit overload responses; autoscaling helps future capacity but cannot erase current latency. Batch size trades throughput against latency. This is role-relevant practice inferred from the JD, not a reported OA question.

##### SD-17 — Slowest dependency
An API makes three sequential calls that can each take 800 ms; its end-to-end budget is 1.5 seconds. What is wrong with giving each call a 1.5-second timeout?

**Checkpoint:** Propagate remaining deadline and allocate budgets including overhead; parallelize independent calls where semantics allow. Cancel unnecessary work. A per-hop timeout is not an end-to-end guarantee.

##### SD-18 — Regional recovery
The business requires RPO ≤5 minutes and RTO ≤30 minutes. Explain each and propose a recovery validation.

**Checkpoint:** RPO bounds tolerable lost data; RTO bounds restoration time. Verify replication/backup lag and timed restoration/failover under realistic failure. A backup schedule alone proves neither recovery time nor restore success.

##### SD-19 — Configuration rollout
A malformed config can break every host. Compare immediate global replacement with versioned staged rollout.

**Checkpoint:** Validate schema and semantics; use a canary, observable health gates, versioning, and rollback to last-known-good. Plan compatibility when mixed versions coexist. Fast distribution alone is not a safe rollout.

##### SD-20 — Expiring leaderboard
A top-100 ranking refreshes each second. Is a relational scan on every page view a good default? What if exact rankings during ties matter?

**Checkpoint:** Maintain a suitable ordered/aggregated read model; define deterministic tie breaks and update semantics. Separate authoritative events from the serving projection. Account for hot leaders, replay and freshness.

##### SD-21 — Database pagination
A feed inserts new records constantly. Users see repeated rows with offset pagination. Propose an alternative.

**Checkpoint:** Stable cursor/keyset pagination with a total order such as timestamp plus unique ID; index accordingly. Define snapshot expectations and updates/deletions. Cursor pagination does not automatically guarantee a fixed historical snapshot.

##### SD-22 — Observability priorities
p50 latency is steady, but complaints and timeouts increase. Which metrics would you inspect before buying more compute?

**Checkpoint:** p95/p99, error/timeout rates, queue age, per-endpoint and per-tenant load, saturation and dependency traces. Compare deployment changes. Averages can hide a subset of severe failures; scaling does not fix every cause.

##### SD-23 — Poison messages
One invalid job is retried forever and blocks useful work. Design retry and quarantine behavior.

**Checkpoint:** Distinguish transient/permanent failure, cap retries, move exhausted jobs to a dead-letter path, alert with actionable context, and support safe replay after repair. Do not silently drop data or retry all jobs forever.

##### SD-24 — Network partition
Two regions cannot communicate. A global inventory invariant must never oversell. Can both sides freely accept all sales and guarantee that invariant?

**Checkpoint:** Not without preallocated disjoint inventory/rights or another constraint that preserves the invariant. Otherwise restrict writes on a side that cannot coordinate. Explain availability versus coordination; don't say all distributed systems always choose just two properties regardless of partitions.

#### AI-assisted coding drills

All 12 are **synthetic practice specifications**. P0: AI-01–08; P1: AI-09–12. Use a small existing app, a clean branch, and seed defects before starting the clock. Each task should involve one bounded fix, not building the whole app in 20 minutes. S03/S07/S09 support repo debugging as a practice theme; they do not establish these exact prompts or framework availability.

##### AI-01 — Created record disappears
**Task:** `POST /movies` returns 201 but a subsequent `GET /movies/{id}` returns 404. Inspect controller/service/repository boundaries and fix the persistence path while preserving response shape.
**Acceptance:** create then retrieve yields the same ID/title; two creates receive distinct IDs; invalid input is not stored; missing ID returns 404. Distinguish persistence defects from cache or route defects rather than assuming a cause.

##### AI-02 — Wrong route and null result
**Task:** A detail endpoint returns 500 for absent records; the list route is accidentally captured as a dynamic ID. Repair routing and missing-resource handling.
**Acceptance:** list succeeds; valid ID returns record; absent ID returns 404; malformed ID follows the specified 400 contract; no null dereference. Preserve unrelated routes.

##### AI-03 — Validation boundaries
**Task:** A signup endpoint accepts passwords outside its specified inclusive 8–64 character range and crashes on null input. Repair validation. For this exercise, length means Unicode code points, not UTF-8 bytes.
**Acceptance:** 7 and 65 rejected; 8 and 64 accepted; null/non-string rejected with 400; valid existing flow stays green. This is a validation exercise, not a recommended production password policy.

##### AI-04 — Latest shipment status
**Task:** Implement a missing pure function combining shipment deadlines and timestamped events. Choose the greatest `(timestamp,event_id)` per shipment. Delivered by deadline is ON_TIME, delivered later is LATE; undelivered is PENDING until deadline and LATE afterward. `now` is supplied. Unknown shipment events are ignored.
**Acceptance:** out-of-order events, duplicate events, equal timestamps, no events, delivery exactly at deadline, empty input; output sorted by shipment ID. This is our fully specified simplified variant of S03's theme, not its original prompt.

##### AI-05 — Idempotent create
**Task:** A retry with the same request key creates a duplicate order. Add sequential-request idempotency to an existing repository API: same key/payload returns original result; same key/different payload returns 409.
**Acceptance:** repeat identical request; conflicting reuse; independent keys; persistence across service-object reconstruction. Discuss what atomic database support would additionally be needed for concurrent calls; do not claim a local dictionary makes it distributed-safe.

##### AI-06 — Rate limiter boundary
**Task:** Fix an existing single-process fixed-window limiter allowing 5 requests per client per 10 seconds. Time is injected and monotonically increasing; a new window starts at integer multiples of 10.
**Acceptance:** first 5 allowed, sixth denied; separate clients independent; t=9.999 vs t=10; denial does not consume next-window quota. Explain boundary bursts and the single-process limitation.

##### AI-07 — Stable pagination
**Task:** Repair a list endpoint whose page slicing skips records. Contract: page is one-based; size is 1–100; records ordered by `(created_at,id)`; invalid inputs return 400.
**Acceptance:** pages 1/2 don't overlap for static data; partial final page; empty results; zero/negative page and oversized size rejected. Do not promise stable pagination under concurrent writes for this offset-based API.

##### AI-08 — UTC deadline parsing
**Task:** A deadline comparison mixes naive and aware timestamps. Contract: accept RFC3339 timestamps with `Z` or an explicit offset; reject missing offsets; compare instants, not display strings.
**Acceptance:** equivalent instants with different offsets; exactly-at-deadline; malformed input; missing timezone; daylight-saving ambiguity avoided by supplied offsets. Keep comparison independent of machine timezone.

##### AI-09 — Bounded retries
**Task:** Repair a client that retries all failures forever. Contract: at most 3 attempts total; retry timeouts and 503 only; stop on other statuses; an injected delay function avoids real sleeps in tests.
**Acceptance:** immediate success; transient success on attempt 3; persistent failure makes exactly 3 calls; 400 is not retried; verify the number of delays. State that real side-effecting calls also require safe retry semantics.

##### AI-10 — Duplicate event processing
**Task:** Fix a single-process event consumer that applies an increment twice for the same event ID. Existing transactional repository method can atomically record the ID and update the balance; use it.
**Acceptance:** repeated ID applied once; distinct IDs applied independently; repository failure leaves both marker and balance unchanged; replay after reloading repository state is deduplicated. Test failure before commit.

##### AI-11 — TTL cache expiry
**Task:** Correct a cache that serves entries at their expiry instant and treats cached zero as a miss. Clock is injected; an entry expires when `now >= expires_at`.
**Acceptance:** before/at/after expiry; values 0, false and empty string; TTL=0; overwrite resets expiry. Do not introduce unrequested cross-process caching behavior.

##### AI-12 — N+1 database calls
**Task:** A summary endpoint calls `get_user` once per order. Existing `get_users(ids)` returns a map; refactor to one batch request without changing order or response fields. Missing users display “Unknown.”
**Acceptance:** one batch call for nonempty orders; no call for empty input; repeated user IDs fetched once; missing user handled; output order preserved. Verify correctness before claiming a performance improvement.

For each drill record: baseline failure, files inspected, AI suggestion accepted/rejected and why, tests run, remaining uncertainty. Passing self-written cases is useful evidence, not proof of passing unknown assessment tests.

---

<a id="material-21"></a>

## 21. OA research ledger

**Source:** [amazon-10587705-oa-sources.md](amazon-10587705-oa-sources.md) · **Section:** historical

> Historical material. Its OA assumptions, past dates and daily schedules are superseded by the current November 12 phone-interview plan. Questions remain available as practice.

### OA research ledger

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](#material-01).

Last researched: **October 28, 2026**. Requisition 10587705, AWS Inference Optimization MLE II. No verified exact-team OA question report located. Public SDE accounts inform practice only. Publication dates are not interview dates. No question-frequency percentages can be supported by this sample.

#### Sources used

| ID | Source and date/context | What it supports | Limits / confidence |
|---|---|---|---|
| S01 | [Amazon SDE II OA guidance](https://www.amazon.jobs/content/en/how-we-hire/sde-ii-oa-prep), current public page | Coding/design/workstyle baseline | Authoritative for the page's SDE II process, not this MLE invitation. Conflicts with recruiter's timing; don't overwrite user report. |
| S02 | [LeetCode: Smallest Base Segment](https://leetcode.com/discuss/post/8401914/amazon-oa-2026-smallest-base-segment-ful-psx8/), posted Jul 16, 2026 | R-01 frequency/feasibility family | Candidate-shared, level/location unknown; moderate specificity, unverified authenticity. |
| S03 | [LeetCode: OA grid and AI task](https://leetcode.com/discuss/post/8387183/), posted Jul 9, 2026 | R-02 center-placement family; AI shipment aggregation theme | Self-report; role/location unknown. Author reports partial AI test success; neither their solution nor its completeness is authoritative. |
| S04 | [LeetCode: load redistribution](https://leetcode.com/discuss/post/8315233/amazon-online-assessment-question-i-coul-967p/), posted Jun 5, 2026 | R-03 minimax family | Incomplete constraints; discussion-only until clarified. |
| S05 | [Reddit: Amazon OA SDE-I](https://www.reddit.com/r/leetcode/comments/1s6a4kq/amazon_oa_sdei/), invitation Mar 23, 2026 per author; Bengaluru, final-year candidate | R-04 positional subsequence, R-05 prefix adjustment | Adjacent junior/India process. Author's LC analogies are not exact equivalences; no ordinary-LIS solution asserted here. |
| S06 | [Reddit: Amazon OA 2026](https://www.reddit.com/r/leetcode/comments/1xh130w/amazon_oa_2026/), recent Oct 2026 thread | One commenter names LC3413 and movie debugging | Low confidence: OP asks a question, only a reply reports experience; exact assessment date, level and location unclear. Vendor frequency claims discarded. |
| S07 | [Reddit: recent OA experiences](https://www.reddit.com/r/leetcode/comments/1wwsmeu/amazon_sde_oa_2026_looking_for_recent_experiences/), recent 2026 discussion; exact publication day unresolved | DP/window/partition themes; backend repo fixes and effectiveness-style scenarios | Treat as one discussion cluster. Mixed formats and unidentified roles/geographies; don't count replies or cross-posts as verified independent frequency data. |
| S08 | [Reddit: SDE OA tips](https://www.reddit.com/r/leetcode/comments/1c1wpc4/amazon_sde_oa_tips_needed/), 2024 search metadata; exact interview date unclear | Older comment describes live-view counter and storage/prioritization choices | Old adjacent evidence, useful for practice format only. Ignore unsupported claims about weighting and permitted aids. |
| S09 | [Reddit: backend OA report](https://www.reddit.com/r/amazonemployees/comments/1vhkpas/amazon_backend_oa_questions_2026_greedy_coding/), Aug 6, 2026 search metadata | Movie persistence/API/validation debugging themes | Promotional PracHub-linked account; low confidence. Root-cause guesses are not established facts. Greedy log prompt too ambiguous for a canonical exercise. |
| S10 | [Glassdoor SWE II reports](https://www.glassdoor.com/Interview/Amazon-Interview-Questions-E6036.htm?filter.jobTitleExact=Software+Engineer+%28Swe+II%29), entry posted May 28, 2026, actual process Jan/Feb 2025, Santa Clara | Broad easy/medium then harder stack coding account | Search-visible evidence; no exact problem. Old interview despite fresh post; not proof of 2026 MLE format. |
| S11 | [NeetCode 150](https://neetcode.io/practice/practice/neetcode150), accessed Oct 28 | Pattern-coverage curriculum | Primary practice source, NOT employer-frequency evidence. Our prioritization and selection are original. |
| S12 | [LeetCode 3413](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/), accessed Oct 28 | Canonical title, constraints and medium difficulty for LC-34 | Authoritative problem page; Amazon association comes only from weak S06 comment. |

#### Requested sites and access limitations

- **LeetCode, NeetCode, Reddit:** used public original pages above. Reports are distinct from editorials and curriculum.
- **Glassdoor:** search-visible candidate extracts used cautiously, with interview date separated from post date. No invented full interview transcript or premium question list.
- **1point3acres:** searched Amazon/OA terms in English and Chinese. [Amazon tag listing](https://www.1point3acres.com/bbs/tag/amazon-56-119.html) exposes a brief OA-format entry but no usable complete current prompt. A URL ending `amazon-56-2026.html` is a pagination path, not evidence of year 2026; it surfaced old posts. A [2017 gated thread](https://www.1point3acres.com/bbs/thread-279101-1-1.html) is stale and excluded. No hidden text reconstructed. This source has not supplied a reliable current question to the bank.
- **Niche sources:** [amazon-oa.com](https://amazon-oa.com/) helped discover original reports; it is a third-party directory, not Amazon. Prefer original dates/text over its summaries. PracHub-related account S09 retained at low confidence. Promotional question dumps, cheating-tool posts, and unsupported frequency claims do not determine priorities.

#### Exclusions that prevent misleading preparation

- [LeetCode SDE2 Bengaluru Aug 2026 report](https://leetcode.com/discuss/post/8499681/amazon-sde-2-selected-blr-aug-2026-by-dh-61y7/), posted Sep 3: grid/locker/config-sync questions belong to later interviews, not established OA questions.
- [LeetCode SDE2 July 2026 report](https://leetcode.com/discuss/post/8409230/interview-experience-amazon-sde-2-3-yoe-xkxue/): tree-distance, stack-middle and calculator questions came later. Its OA repo-task description is adjacent support only.
- [LeetCode upsolving thread](https://leetcode.com/discuss/post/7550047/upsolving-amazon-oa-by-anonymous_user-099n/): screenshot-only prompt not transcribed from unavailable content.
- [Reddit older OA thread](https://www.reddit.com/r/leetcode/comments/1htdjbf/): retrieval failed; no question adopted from this source. LC1561 is a curriculum recommendation, not a verified report from it.

#### Technical references for synthetic exercises

These support principles, not claims about what Amazon asks:
- [AWS: idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
- [AWS: retries, timeouts and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/).
- [SQS: at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).
- [DynamoDB: read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

#### Refresh procedure — every three days

1. Read the official packet if Suraj has provided it in this chat or the dossier. Record its date and replace conflicting assumptions, including task counts, timing, framework, assistance rules and expiry. Never open a live assessment to investigate its contents.
2. Search exact role/team first, then AWS/MLE II, then clearly labeled SDE II adjacent OA accounts. Use a recent window plus older sources only for gaps. Search LeetCode, Reddit, Glassdoor, 1point3acres, NeetCode updates and niche indexes; follow originals where accessible.
3. Capture publication date, actual interview date if known, level, geography, round, URL, access status and uncertainty. Distinguish firsthand reports, commenters, vendor summaries and inferred practice. Deduplicate authors/cross-posts. Exclude phone/loop-only prompts from OA evidence.
4. Prefer independently corroborated, relevant evidence over recency alone. A single new anecdote can justify one optional drill, not overhaul the plan. Do not attach invented frequency percentages.
5. Preserve question IDs, attempt history and corrected claims. Add questions only for a real coverage gap; retire superseded items with explanation. Update dated change log and source ledger. Refresh date is the actual research date, even if no changes qualify.
6. Prioritize the candidate's demonstrated error patterns when actual attempts exist; until then do not invent strengths, scores or readiness.
7. Notify only meaningful bank/format changes, an actionable access failure or a required clarification. If no meaningful change, update the research record quietly. Stop recurring OA work when the user confirms OA completion or asks to stop; do not infer completion from the planning date.

---

<a id="material-22"></a>

## 22. Historical OA-first combined schedule

**Source:** [amazon-10587705-two-week-study-plan.md](amazon-10587705-two-week-study-plan.md) · **Section:** historical

> Historical material. Its OA assumptions, past dates and daily schedules are superseded by the current November 12 phone-interview plan. Questions remain available as practice.

### Two-week plan — Amazon OA first, inference fundamentals daily

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](#material-01).

**Created October 28, 2026.** Day 1 is October 28; Day 14 is November 10. If starting later, shift dates only within the actual assessment window. November 11 is an estimate from “two weeks,” not a confirmed expiry. The invitation controls the deadline and test rules.

This is the current combined schedule, superseding the earlier OA-only daily sequence. All tracker entries remain unattempted; the plan assumes no demonstrated mastery. Keep this scope stable during source refreshes unless official instructions or actual practice results justify a change.

#### Time budget and method

**Normal day: 3 focused hours**, plus breaks. Allocate 70 minutes coding, 20 AI coding, 20 distributed-system scenarios, 10 behavioral/workstyle, 40 ML/inference, and 20 review. That is 140 minutes on OA practice/review and 40 on domain fundamentals. Day 14 is a lighter 90-minute review or the actual assessment if scheduled.

For two coding problems: 5 minutes reading, about 25 minutes on the first, 30 on the second and 10 testing. Three-problem days use 20 minutes each plus 10 testing. On learning days, log a blocker before consulting an explanation; on mock days, finish the entire timed block without hints. The mock's two-question format is a training choice, not a confirmed assessment question count.

In each 20-minute design block, answer four named scenarios in five minutes each: requirement → choice → failure mode → tradeoff. Hide the answer checkpoints first. AI practice uses the specified small bug/task with an assistant; inspect its patch and run tests yourself. Standard coding practice is unassisted. The official packet governs actual assessment tool use.

**Fixture setup:** AI drills are specifications, not prebuilt repositories. Before Day 1, allow up to 20 additional minutes to have a helper create a tiny local app, test runner and the AI-01 defect without showing you its solution. Use the same scaffold thereafter; let the helper seed the next bounded defect outside the timed attempt. Do not build a complete backend during a 20-minute drill. If setup cannot be made ready, use the day's AI block to establish it, log that as setup, and carry the missed drill to the next review block rather than pretending it was a timed solve.

**Review block:** record actual time, hint use, failing cases and cause in the trackers. Choose one highest-impact miss for a short closed-book repair; schedule a full re-solve 48 hours later. If re-solves accumulate, replace the day's second new coding question with the oldest failed P0 question. Do not add hours to catch up. For domain exercises, end with a small derivation, tested function or a five-bullet explanation.

#### Day-by-day assignments

##### Day 1 — Wed Oct 28 · Baseline and attention shapes

- **Coding 70:** LC 560 Subarray Sum Equals K + LC 994 Rotting Oranges (bank LC-04/13). Record independent baseline before seeing solutions.
- **AI 20:** AI-01, created movie cannot be retrieved. Trace route → service → persistence; test create/read and missing ID.
- **Design 20:** SD-01–04: audience counter, last inventory item, payment retry, duplicate delivery.
- **Behavioral 10:** write three truthful examples of taking ownership; outline one with your personal action and observed result. No invented metrics.
- **Domain 40:** CON-01/02/04. Draw attention tensor shapes, explain causal versus padding masks, and derive the KV example to **4 GiB** without looking at checkpoints.
- **Review 20:** record the baseline and one next action per weakness.

##### Day 2 — Thu Oct 29 · Hashing and stable softmax

- **Coding 70:** LC 3 Longest Substring Without Repeating Characters + LC 49 Group Anagrams (LC-01/02). Explain window invariants and frequency signatures.
- **AI 20:** AI-02, route collision and null-result handling.
- **Design 20:** SD-05–08: cache expiry, read-after-write, retry storm, worker backlog.
- **Behavioral 10:** one example of learning an unfamiliar system; explain how you verified understanding.
- **Domain 40:** CODE-01 stable masked softmax in NumPy/PyTorch primitives; test extreme logits, padding and all-masked rows returning zero.
- **Review 20:** test boundaries and log hint use.

##### Day 3 — Fri Oct 30 · Prefix/suffix and head sharing

- **Coding 70:** LC 238 Product of Array Except Self + LC 347 Top K Frequent Elements (LC-03/05).
- **AI 20:** AI-03, validation boundaries and null input.
- **Design 20:** SD-09–12: rate limiter, partition key, upload consistency, AZ failure.
- **Behavioral 10:** one disagreement: explain the evidence, decision and how you worked with the other person.
- **Domain 40:** CON-03/05/08: GQA/MQA/MHA, RoPE positions and prefill versus decode. Draw 32 query heads mapped to 8 KV heads; compare cache memory with 32 KV heads.
- **Review 20:** closed-book repair of a Day 1 miss; if it needs more time, apply the replacement rule.

##### Day 4 — Sat Oct 31 · Partitioning, intervals and attention code

- **Coding 70:** LC 75 Sort Colors + LC 56 Merge Intervals (LC-06/07).
- **AI 20:** AI-04, shipment events with ordering and deadline boundaries.
- **Design 20:** SD-13–16: event ordering, transactional outbox, search lag, inference overload.
- **Behavioral 10:** one decision made with incomplete information; separate assumptions from facts.
- **Domain 40:** CODE-02, implement single-batch/single-head causal attention first, then add batched heads if time permits. Validate a future-token perturbation test. Log incomplete padding support explicitly.
- **Review 20:** repair a Day 2 miss and inspect attention shape/mask errors.

##### Day 5 — Sun Nov 1 · Greedy, stacks and cache correctness

- **Coding 70:** LC 435 Non-overlapping Intervals + LC 739 Daily Temperatures (LC-08/09).
- **AI 20:** AI-05, sequential idempotent create and conflicting payloads.
- **Design 20:** SD-17–20: deadline budgets, recovery targets, config rollout, leaderboard.
- **Behavioral 10:** describe a mistake, its impact and the correction you personally made.
- **Domain 40:** CODE-03, a one-token KV-cache decode reference. Compare several cached steps against full recomputation; keep dropout disabled and positions consistent.
- **Review 20:** repair a Day 3 miss; distinguish failing code from an unclear invariant.

##### Day 6 — Mon Nov 2 · Binary search and performance reasoning

- **Coding 70:** LC 875 Koko Eating Bananas + LC 1011 Capacity To Ship Packages Within D Days (LC-10/11). State and prove each monotone feasibility predicate.
- **AI 20:** AI-06, fixed-window rate limiter boundaries.
- **Design 20:** SD-21–24: pagination, observability, poison messages, partition/inventory invariant.
- **Behavioral 10:** a time you prioritized competing requests; explain the customer impact and tradeoff.
- **Domain 40:** CON-17/18/24: GPU memory hierarchy, roofline arithmetic and profiling workflow. Derive the hypothetical **1 ms** bound and name what could make measured time longer.
- **Review 20:** repair a Day 4 miss. Reserve tomorrow's coding pair unread.

##### Day 7 — Tue Nov 3 · Full mock 1

- **OA 120, continuous:** coding **LC 215 Kth Largest Element + LC 763 Partition Labels** (70); AI-07 pagination (20); SD-02/07/10/14 (20); behavioral below (10). Use no hints during coding; AI only in its practice section. Coding pair is unseen only if you have not already solved it.
- **Behavioral inside mock:** five brief workplace scenarios: conflicting deadlines, a suspected bug, disagreement, incomplete requirements, and a missed commitment. Give the next action plus rationale; this is practice, not a prediction of the test UI.
- **Domain 40:** CON-09/10/11: TTFT and token metrics, continuous batching, paging versus prefix reuse. Explain why throughput can improve while TTFT gets worse.
- **Review 20:** score correctness, time lost and failure causes. Pick the top two repair priorities. Previously studied design prompts measure recall/application, not unseen performance.

##### Day 8 — Wed Nov 4 · Graphs and numerical validation

- **Coding 70:** LC 200 Number of Islands + LC 207 Course Schedule (LC-12/14); replace the second if Mock 1 exposed a more urgent failed P0 skill.
- **AI 20:** AI-08, timezone-aware deadline comparison.
- **Design 20:** SD-03/04/13/23: idempotency, redelivery, ordering and poison messages.
- **Behavioral 10:** explain a quality issue you caught and how you established its impact.
- **Domain 40:** CON-23 + ML-04/05: tolerances, training-serving skew and NaN localization. Write a numerical test checklist for your attention reference.
- **Review 20:** repair a Day 6 miss; retain actual failing inputs.

##### Day 9 — Thu Nov 5 · DP foundations and FlashAttention

- **Coding 70:** LC 198 House Robber + LC 322 Coin Change (LC-15/16). State state, transition, base case and iteration order before coding.
- **AI 20:** AI-09, bounded retries and nonretryable errors.
- **Design 20:** SD-01/05/06/15: counts, caching, read consistency and search freshness.
- **Behavioral 10:** one example of investigating beyond the initial symptom.
- **Domain 40:** CON-06/07: derive online softmax updates; explain why FlashAttention saves memory traffic but does not make dense attention linear-time. Use two small score tiles to check the recurrence numerically.
- **Review 20:** re-solve a Mock 1 miss, choosing correctness issues before micro-optimization.

##### Day 10 — Fri Nov 6 · DP/greedy and measured fusion

- **Coding 70:** LC 139 Word Break + LC 55 Jump Game (LC-17/18).
- **AI 20:** AI-10, duplicate processing and transactional failure.
- **Design 20:** SD-08/09/16/17: backlog, quotas, overload and deadlines.
- **Behavioral 10:** a time you simplified a process or implementation; identify what improved without overstating scope.
- **Domain 40:** CON-19/20/21 + CASE-12. Explain occupancy, fusion tradeoffs and tiling; derive the **1.111×** end-to-end speedup bound for a 2× optimization of a 20% component.
- **Review 20:** repair a Day 8 miss; review regression-test coverage in the AI patch.

##### Day 11 — Sat Nov 7 · Finish core coverage and ML evaluation

- **Coding 70:** LC 134 Gas Station + LC 300 Longest Increasing Subsequence (LC-19/20). For LIS, implement O(n²) DP correctly before discussing the O(n log n) alternative if needed.
- **AI 20:** AI-11, TTL expiry and falsy cached values.
- **Design 20:** SD-11/12/18/19: storage, failover, recovery and rollout.
- **Behavioral 10:** rehearse two previously written examples in 90 seconds each, then answer “what did you personally do?”
- **Domain 40:** ML-01/02/06: leakage, text-to-SQL evaluation and cost per successful task. Make a small comparison table with quality, latency and total cost; do not use invented production results.
- **Review 20:** repair a Day 9 miss. Keep tomorrow's mock problems unread.

##### Day 12 — Sun Nov 8 · Full mock 2 and readiness decision

- **OA 120, continuous:** coding **LC 973 K Closest Points to Origin + LC 621 Task Scheduler** (70); AI-12 batch lookup/N+1 fix (20); SD-06/12/16/24 (20); behavioral (10).
- **Behavioral inside mock:** repeat the five Day 7 scenario categories with changed constraints. Evaluate consistency and practical action, not a memorized “ideal personality.”
- **Domain 40:** CASE-01/06: diagnose TTFT regression and critique a suspicious GPU timing claim. For each, write three hypotheses and a measurement that could disprove each.
- **Review 20:** apply the readiness checks below. If ready and the invitation permits, schedule/take the OA on Day 13 or 14; the plan never authorizes starting a live assessment through an assistant.

##### Day 13 — Mon Nov 9 · Repair and consolidate, or assessment

- **Coding 70:** re-solve the two highest-impact failures from the mocks, closed book. If neither mock had coding failures, solve **R-05 prefix adjustments to zero + LC 128 Longest Consecutive Sequence**. R-05 is not LC1526; the operation differs.
- **AI 20:** repeat the lowest-scoring AI drill with changed inputs; tie-break by earliest ID. If all passed, repeat AI-04 with shuffled/duplicate events.
- **Design 20:** repeat the four lowest-scoring scenarios; tie-break by earliest ID. If no scores exist, use SD-02/04/08/16.
- **Behavioral 10:** review factual consistency of the examples; remove claims you cannot substantiate.
- **Domain 40:** CON-12/22 + CASE-09: SGLang prefix reuse, precompiled dispatch keys and cold-start diagnosis. Finish with a two-minute explanation tying one concept to a real contribution, without inventing measurements.
- **Review 20:** verify the actual deadline, allowed language/tools, environment instructions and required identification from the official packet. No new hard topics.
- **If taking the real OA today:** it replaces all study blocks; do not do a three-hour cram session first.

##### Day 14 — Tue Nov 10 · Light review or assessment

**90 minutes maximum if not taking the OA:** 25 minutes reviewing your coding error log and standard-library APIs; 15 minutes AI debugging workflow; 15 minutes SD-02/04/16; 10 minutes truthful behavioral examples; 15 minutes attention shapes/KV arithmetic/TTFT recall; 10 minutes invitation/environment check. No new problems or kernels.

If the OA is scheduled today, it replaces this review. Its actual duration and rules come from the official packet. Leave a buffer before the verified expiry; do not rely on an assumed November 11 deadline. If practice is still weak, focus remaining time on the two biggest error categories rather than trying to finish either entire question bank.

#### Readiness checks and adaptation

These are preparation heuristics, not Amazon's passing criteria:

- Coding: both mock solutions correct with stated complexity and boundary tests, within the 70-minute practice block. If a problem was familiar, mark it familiar; use an unseen reserve instead to assess transfer.
- AI: diagnose and fix a bounded issue, review the assistant's diff and run meaningful regression tests within 20 minutes.
- Design: four defensible decisions in 20 minutes, each with a failure mode and tradeoff.
- Behavioral: honest, consistent responses grounded in actual actions; don't memorize assessment answers.

**Unseen coding reserves:** LC 33 Search in Rotated Sorted Array; LC 15 3Sum; LC 1561 Maximum Number of Coins You Can Get; LC 743 Network Delay Time. Use them only if a mock pair is already familiar. Difficulty/time vary; failure is diagnostic, not a predicted hiring outcome.

**If you have only two hours:** coding 70 + AI 15 + design 15 + behavioral 5 + domain recall 10 + log 5. The 15-minute AI practice is a shortened study drill; retain full 120-minute uninterrupted mocks on Days 7/12 and omit domain work those days if necessary. Cut fresh domain coding and P1/stretch questions before core OA work. Do not compress sleep to complete the bank.

**Defer until after OA:** full GPU GEMM/attention-kernel implementation, advanced speculative-decoding proofs, MoE deep dives and 45-minute domain system-design mocks. In this fortnight, learn their foundations without displacing coding practice. A compatible GPU is not required for this plan's domain assignments.

#### Materials and records

- [OA bank: LC IDs and links](#material-19)
- [OA design and AI drill specifications](#material-20)
- [ML/inference bank: CON, CODE, CASE, ML IDs](#material-05)
- [OA attempts](#material-23) · [Domain attempts](#material-11)

Keep one row of factual outcomes per item, adding attempt detail in notes or a separate dated practice log when repeating. This document is a schedule, not evidence that any work has been completed. Existing three-day research refreshes should preserve the schedule and only change it for stronger evidence, official instructions or observed weaknesses.

---

<a id="material-23"></a>

## 23. Historical OA practice tracker

**Source:** [amazon-10587705-oa-attempts.csv](amazon-10587705-oa-attempts.csv) · **Section:** historical

> Historical material. Its OA assumptions, past dates and daily schedules are superseded by the current November 12 phone-interview plan. Questions remain available as practice.

````csv
id,status,attempt_date,minutes,independent,result,error_category,notes,revisit_date
LC-01,unattempted,,,,,,,
LC-02,unattempted,,,,,,,
LC-03,unattempted,,,,,,,
LC-04,unattempted,,,,,,,
LC-05,unattempted,,,,,,,
LC-06,unattempted,,,,,,,
LC-07,unattempted,,,,,,,
LC-08,unattempted,,,,,,,
LC-09,unattempted,,,,,,,
LC-10,unattempted,,,,,,,
LC-11,unattempted,,,,,,,
LC-12,unattempted,,,,,,,
LC-13,unattempted,,,,,,,
LC-14,unattempted,,,,,,,
LC-15,unattempted,,,,,,,
LC-16,unattempted,,,,,,,
LC-17,unattempted,,,,,,,
LC-18,unattempted,,,,,,,
LC-19,unattempted,,,,,,,
LC-20,unattempted,,,,,,,
LC-21,unattempted,,,,,,,
LC-22,unattempted,,,,,,,
LC-23,unattempted,,,,,,,
LC-24,unattempted,,,,,,,
LC-25,unattempted,,,,,,,
LC-26,unattempted,,,,,,,
LC-27,unattempted,,,,,,,
LC-28,unattempted,,,,,,,
LC-29,unattempted,,,,,,,
LC-30,unattempted,,,,,,,
LC-31,unattempted,,,,,,,
LC-32,unattempted,,,,,,,
LC-33,unattempted,,,,,,,
LC-34,unattempted,,,,,,,
LC-35,unattempted,,,,,,,
LC-36,unattempted,,,,,,,
LC-37,unattempted,,,,,,,
LC-38,unattempted,,,,,,,
R-01,unattempted,,,,,,,
R-02,unattempted,,,,,,,
R-03,unattempted,,,,,,,
R-04,unattempted,,,,,,,
R-05,unattempted,,,,,,,
R-06,unattempted,,,,,,,
R-07,unattempted,,,,,,,
SD-01,unattempted,,,,,,,
SD-02,unattempted,,,,,,,
SD-03,unattempted,,,,,,,
SD-04,unattempted,,,,,,,
SD-05,unattempted,,,,,,,
SD-06,unattempted,,,,,,,
SD-07,unattempted,,,,,,,
SD-08,unattempted,,,,,,,
SD-09,unattempted,,,,,,,
SD-10,unattempted,,,,,,,
SD-11,unattempted,,,,,,,
SD-12,unattempted,,,,,,,
SD-13,unattempted,,,,,,,
SD-14,unattempted,,,,,,,
SD-15,unattempted,,,,,,,
SD-16,unattempted,,,,,,,
SD-17,unattempted,,,,,,,
SD-18,unattempted,,,,,,,
SD-19,unattempted,,,,,,,
SD-20,unattempted,,,,,,,
SD-21,unattempted,,,,,,,
SD-22,unattempted,,,,,,,
SD-23,unattempted,,,,,,,
SD-24,unattempted,,,,,,,
AI-01,unattempted,,,,,,,
AI-02,unattempted,,,,,,,
AI-03,unattempted,,,,,,,
AI-04,unattempted,,,,,,,
AI-05,unattempted,,,,,,,
AI-06,unattempted,,,,,,,
AI-07,unattempted,,,,,,,
AI-08,unattempted,,,,,,,
AI-09,unattempted,,,,,,,
AI-10,unattempted,,,,,,,
AI-11,unattempted,,,,,,,
AI-12,unattempted,,,,,,,
````

---

<a id="material-24"></a>

## 24. Archived role description

**Source:** [aws-inference-optimization-10587705-2026-10-26.md](supporting/aws-inference-optimization-10587705-2026-10-26.md) · **Section:** supporting

Posted: not visible in source

### Machine learning engineer II, AWS Inference Optimization

**URL:** https://amazon.jobs/en/jobs/10587705/machine-learning-engineer-ii-aws-inference-optimization
**Job ID:** 10587705
**Employer:** Amazon Development Center U.S., Inc.
**Location:** USA, CA, Santa Clara
**Captured:** 2026-10-26 from the live Amazon.jobs page through Chrome accessibility text. Apply now was visible. Dates in recommended jobs belong to other requisitions.

#### Description

Amazon AI is looking for a machine learning engineer to be part of inference optimization team working on optimizing large language OSS models like Qwen, Gemma, gptoss, improving inference performance by development on inference stacks like vLLM, SGLAng, performance tuning of GenAI inference on Amazon Sagemaker, Bedrock and Hyperpod. Work includes implementation of inference optimization techniques like Speculative decoding, Disaggregated Inference and CUDA kernel tuning.

As part of the team, you will own price-performance of amazon LLM inference on Sagemaker, Hyperpod and Bedrock. You will be working in a fast-paced, cross-disciplinary team of engineers and researchers who are leaders in the field. You will take on challenging problems, distill real requirements, and then deliver solutions that either leverage existing academic and industrial research, or utilize your own out-of-the-box pragmatic thinking. In addition to coming up with novel solutions and prototypes, you will deliver these to production in customer facing products.

Inclusive Team Culture

Here at AWS, we embrace our differences. We are committed to furthering our culture of inclusion. We have ten employee-led affinity groups, reaching 40,000 employees in over 190 chapters globally. We have innovative benefit offerings, and host annual and ongoing learning experiences, including our Conversations on Race and Ethnicity (CORE) and AmazeCon (gender diversity) conferences.

Work/Life Balance

Our team puts a high value on work-life balance. It isn’t about how many hours you spend at home or at work; it’s about the flow you establish that brings energy to both parts of your life. We believe striking the right balance between your personal and professional life is critical to life-long happiness and fulfillment. We offer flexibility in working hours and encourage you to find your own balance between your work and personal lives.

Mentorship & Career Growth

Our team is dedicated to supporting new members. We have a broad mix of experience levels and tenures, and we’re building an environment that celebrates knowledge sharing and mentorship. We care about your career growth and strive to assign projects based on what will help each team member develop into a better-rounded engineer and enable them to take on more complex tasks in the future.

Key job responsibilities

As a MLE in Inference Optimization team you will be responsible for the major portion of existing and/or new inference software. List of responsibilities includes but is not limited to developing model servers, developing CUDA kernels in vLLM, SGLang, developing services for GenAI optimization and benchmarking, creating and modifying a mid-size application, or service.

#### Basic Qualifications

- 3+ years of non-internship professional software development experience
- 2+ years of non-internship design or architecture (design patterns, reliability and scaling) of new and existing systems experience
- 1+ years of software development engineer or related occupational experience
- 1+ years of designing and developing large-scale, multi-tiered, multi-threaded, embedded or distributed software applications, tools, systems, and services using: C#, C++, Java, or Perl experience
- Bachelor's degree or foreign equivalent in Computer Science, Engineering, Mathematics, or a related field
- Knowledge of Machine Learning and LLM fundamentals, including transformer architecture, training/inference lifecycles, and optimization techniques

#### Preferred Qualifications

- 3+ years of full software development life cycle, including coding standards, code reviews, source control management, build processes, testing, and operations experience
- Bachelor's degree in computer science or equivalent

Amazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability, or other legally protected status.

Los Angeles County applicants: Job duties for this position include: work safely and cooperatively with other employees, supervisors, and staff; adhere to standards of excellence despite stressful conditions; communicate effectively and respectfully with employees, supervisors, and staff to ensure exceptional customer service; and follow all federal, state, and local laws and Company policies. Criminal history may have a direct, adverse, and negative relationship with some of the material job duties of this position. These include the duties and responsibilities listed above, as well as the abilities to adhere to company policies, exercise sound judgment, effectively manage stress and work safely and respectfully with others, exhibit trustworthiness and professionalism, and safeguard business operations and the Company’s reputation. Pursuant to the Los Angeles County Fair Chance Ordinance, we will consider for employment qualified applicants with arrest and conviction records.

Our inclusive culture empowers Amazonians to deliver the best results for our customers. If you have a disability and need a workplace accommodation or adjustment during the application and hiring process, including support for the interview or onboarding process, please visit https://amazon.jobs/content/en/how-we-hire/accommodations for more information. If the country/region you’re applying in isn’t listed, please contact your Recruiting Partner.

The base salary range for this position is listed below. Your Amazon package will include sign-on payments and restricted stock units (RSUs). Final compensation will be determined based on factors including experience, qualifications, and location. Amazon also offers comprehensive benefits including health insurance (medical, dental, vision, prescription, Basic Life & AD&D insurance and option for Supplemental life plans, EAP, Mental Health Support, Medical Advice Line, Flexible Spending Accounts, Adoption and Surrogacy Reimbursement coverage), 401(k) matching, paid time off, and parental leave. Learn more about our benefits at https://amazon.jobs/en/benefits.

USA, CA, Santa Clara - 165,200.00 - 223,600.00 USD annually

---

<a id="material-25"></a>

## 25. Role-specific resume source

**Source:** [suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.md](supporting/suraj-mishra-amazon-aws-inference-optimization-10587705-2026-10-26.md) · **Section:** supporting

Suraj Mishra

New York, NY | 551-371-2172

sm12377@nyu.edu

Software engineer focused on GPU kernel optimization and LLM inference, with nearly four years of professional software development at Oracle and Incture and a master's from NYU. Built Triton attention and KV-cache kernels validated by 210 H100 tests and authored merged vLLM/SGLang contributions to serving observability and benchmark correctness. Combines GPU profiling, reproducible performance measurement, backend development and infrastructure automation to make inference faster and more dependable.

New York University

Masters in Computer and Information Systems | GPA: 3.72/4.00

Sept 2024 - May 2026;

Deep Learning

Machine Learning

Building LLM Reasoners

Operating Systems

National Institute of Technology, Bhopal

B.Tech in Computer Science and Engineering

Jul 2016 - Jun 2020;

Oracle

Member Technical Staff

Jan 2022 - Aug 2024

Redesigned **JUnit 5/Jupiter test execution and object lifecycles**, reducing end-to-end execution of the then-existing full pipeline from **approximately 10-11 hours to within 3 hours**; enabled expansion into functional, load, stress and long-running suites.

Moved dependent Recovery Appliance, policy, network and protected-database interface objects into shared setup; separated verification from state-changing tests, grouped compatible tests for parallel/sequential reuse and distributed suites across compute instances through **TeamCity**.

Adapted existing **Terraform** provisioning scripts for tenancy/network settings; authored readiness and artifact-collection scripts plus cleanup that ran despite earlier failures, and deployed development code/images with **Ansible**.

Automated Recovery Appliance migration test workflows from provisioning through teardown, checking recovery windows, data-loss exposure, protected states and backup continuity; expanded specification-based functional coverage on representative hardware.

Researched Java logging libraries for automatic test-class/function attribution and wrote a shell script organizing interleaved output into class-based logs to investigate service error-code, message and resource-field discrepancies.

Tested **Oracle Database Zero Data Loss Autonomous Recovery Service** in Azure and Google Cloud environments.

Validated new rack and bare-metal hardware with point-in-time recovery and functional tests; documented procedures and partially automated them for TeamCity integration.

Incture Technologies

Software Engineer

Sept 2020 - Dec 2021

Built stateless **Java/Spring Boot** backend microservices for enterprise supply-chain analytics supporting **5× traffic growth**; reduced API **p99 latency by about 70%** through SQL plan profiling, indexing and connection-pool tuning.

Led root-cause investigations into data consistency failures and orchestration deadlocks; automated **Jenkins/Ansible blue-green deployments**, eliminating release downtime and reducing customer-reported incidents by **about 85%**.

TritonAttn: Attention and KV-Cache Kernels

Triton, CUDA, PyTorch, H100

2026

Built a from-scratch GPU attention library reproducing FlashAttention-2, Flash-Decoding, GQA, StreamingLLM and KIVI as fused Triton kernels across prefill and decode; **210/210 tests passing on H100 (sm_90)**.

Engineered a FlashAttention-2 prefill kernel reaching **433 TFLOP/s BF16** and **1.1-1.3× PyTorch SDPA at long sequence lengths** through online-softmax tiling, base-2 exp2 and Hopper autotuning.

Implemented split-KV Flash-Decoding with an occupancy-aware split policy and tensor-core GQA/MQA path; achieved **up to 13.6× versus naive decode** and **peak 1.29× versus SDPA in target GQA regimes**.

Implemented KIVI INT8/INT4/INT2 KV-cache quantization with in-kernel bit-unpacking; achieved **5.2× KV compression** and **+0.33% INT4 perplexity**, with bit-for-bit validation against dequantize-then-attend.

Used **NVIDIA Nsight Compute** to diagnose register-pressure-capped occupancy; integrated kernels into Hugging Face Transformers and validated token-identical greedy generation.

Merged vLLM Contributions

Python, async HTTP, pytest, model serving

Sept 2026 - Present

Authored merged **vLLM #55508**, correcting time-to-first-token (TTFT), end-to-end latency and time-per-output-token (TPOT) accounting across completion, chat, audio and legacy inference benchmark clients.

Unified the first-token timestamp, stopped non-token usage trailers from extending request latency and rejected usage-only streams; enforced the decode-window timing invariant with **12 new and 8 sibling tests passing**.

Authored merged **vLLM #62205**, adding request-ID-correlated completion output logging for streaming deltas, non-streaming responses and final accumulated output; validated **53 focused and 281 broader regression tests**.

Authored merged **vLLM #62204** to document and regression-test remote-media retry byte-budget accounting across synchronous/asynchronous downloads; improved operator-facing guidance with **9 focused tests passing**.

Merged SGLang Scheduler Metrics Fix

Python, request lifecycle, Prometheus

Sept 2026

Authored merged **SGLang #39312**, reproducing negative queue-time metrics and a scheduler assertion when retracted or preempted requests re-entered the waiting queue.

Accumulated every wait interval, closed waits idempotently across chunked prefill and preserved values across process-clock rebasing; retained scheduling decisions and the existing Prometheus histogram contract.

Added six regression/contract tests; validated **303 related unit tests and 20,000 randomized lifecycles** across unified/disaggregated modes, preserving behavior on **9,504 non-retracted cases**.

LLM Inference Control Plane

Go, Kubernetes, Kubebuilder, Prometheus

Aug 2026 - Present

Built a Kubernetes operator deploying self-hosted LLMs as an OpenAI-compatible service; gated canary promotion, rollback or hold on measured serving quality while keeping the last good revision available.

Implemented an SSE sidecar measuring TTFT, errors, concurrency and queue depth; separated queue/concurrency-based autoscaling from rollout decisions and packaged dashboards with multi-window SLO alerts.

Established p95 TTFT stability in a CPU feasibility study before using it as a release gate; hardened the operator with admission checks, deterministic tests and CI checks for generated API/documentation drift.

Languages and GPU: Python, C++, Java, Go, SQL; Triton, CUDA, H100/A100, tensor cores, FP16/BF16, shared/global/L2 memory, occupancy and register-pressure analysis

Inference optimization: FlashAttention, split-KV decoding, GQA/MQA, INT2/INT4/INT8 KV-cache quantization, fusion, autotuning, Nsight Compute/Systems, CUDA events, roofline analysis

LLM systems: PyTorch, Transformers, vLLM, SGLang, llama.cpp, TensorRT-LLM, transformer architecture, TTFT/E2E/TPOT, continuous/dynamic batching, async HTTP, SSE

Training and testing: FSDP, DeepSpeed, NCCL, RDMA, GRPO, LoRA/QLoRA, W&B; pytest, JUnit 5, timing-invariant and randomized lifecycle testing, reproducible benchmarking

Infrastructure: Kubernetes, Kubebuilder, Docker, Terraform, Ansible, SLURM, Prometheus, Grafana, SLOs, Git/GitHub Actions, TeamCity, Jenkins, canary and blue-green delivery

---

<a id="material-26"></a>

## 26. Current STAR rehearsal stories — relevant excerpt

**Source:** [story-bank.md](../story-bank.md) · **Section:** supporting · **Relevant excerpt only**

#### Interview-ready STAR bank — October 26, 2026

**Provenance:** user-stated 2026-10-23 through 2026-10-26; supported by the detailed practice transcript and current primary CV/profile. Results are approximate recollections, not independently inspected CI reports. This section is the current rehearsal version; detailed evidence and earlier clarifications remain below.

**Assessment:** enough for two substantial project stories and a focused debugging story within the first project. Functional validation, migration, and hardware work supply additional examples, but some are incomplete STAR stories. Do not present every angle of the same project as a separate project, invent conflict/leadership anecdotes, or claim this evidence guarantees a particular hiring outcome.

**Resume correction comes first:** The uploaded resume contains a production-throughput claim the user explicitly says was false. The test-runtime result cannot substantiate that claim. Use the correction in [the resume claim audit](../oracle-resume-claim-audit.md), then explain the real work. The retracted claim is permanently recorded in [retracted claims](../retracted-claims.md); it must not return through historical dossier material.

| ID | Story | Best use | Readiness |
|---|---|---|---|
| O1 | Parallel test execution and object lifecycle redesign | Most impactful work; performance; ownership; tradeoffs; lessons | Strongest, with approximate runtime result |
| O2 | Restoring useful logs during parallel execution | Debugging; observability; an unforeseen problem | Ready, related to O1 |
| O3 | Test-environment lifecycle automation | Automation; reuse; failure handling; resource management | Ready with qualitative outcome and explicit limitation |
| O4 | Service-contract validation | Test design; collaboration with developers | Supporting example; no single defect/fix result reconstructed |
| O5 | Recovery Appliance migration testing | Recovery correctness; customer scenarios | Partial STAR; implementation/result depth still limited |
| O6 | Rack/bare-metal PITR validation | Hands-on validation; documentation; incremental automation | Partial STAR; exact procedure/result still limited |

##### O1 — Redesigning test execution and reducing feedback time

**S — Situation:** Oracle's then-existing test pipeline took roughly 10–11 hours end to end. Individual tests repeatedly created/deleted dependent test-interface objects. The test and development repositories continued growing during the work.

**T — Task:** Improve the execution infrastructure and object lifecycle so compatible tests could run concurrently while separating tests that changed shared state. This was testing infrastructure ownership, not ownership of the production backup scheduler.

**A — Actions personally implemented:**

- Used JUnit 5/Jupiter parallel test-method execution.
- Moved interface-object creation and health checks into pre-test setup. RA objects supported RSNI and Policy objects; both supported Protected Database objects.
- Grouped verification tests that did not modify the required shared state; they reused objects and ran concurrently. Cleanup followed the verification group.
- Ran tests that changed parameters or created/deleted objects in a separate pipeline step. Later grouped those tests to run sequentially with compatible object sets and changed objects between groups.
- Also worked on suite distribution through TeamCity. Keep later splitting/expansion separate from the earlier complete-pipeline timing comparison.

**R — Result:** The entire pipeline then in place went from approximately 10–11 hours to within 3 hours of end-to-end test execution. Some classes went from over 20 minutes to 3–4 minutes; others from 2–3 hours to about 40 minutes. Saved time gave headroom for later functional, load, stress, and long-running suites. No unchanged-hardware, lower-cost, precise percentage, or production-throughput claim is supported.

**Reflection — user-stated:** Work took roughly five to six months. New tests kept arriving and required refactoring. Establish test-writing guidelines earlier and account for suite growth in compute estimates. For this project, focus on finding bugs faster by shortening the feedback cycle.

**Spoken answer:**

> At Oracle, I redesigned parts of our test infrastructure because the full pipeline took roughly 10–11 hours. Tests were repeatedly creating and deleting dependent interface objects. I moved object creation and health checks into shared setup and separated verification tests from tests that changed parameters or created and deleted objects. Compatible verification tests reused those objects and ran in parallel using JUnit 5, with cleanup after the group completed. I later grouped the other tests to run sequentially against compatible object sets. End-to-end test execution for the full pipeline at that time fell to within three hours, which gave us room to expand testing. The project took about five to six months while the repository grew. Looking back, I would set test-writing guidelines earlier and account for that growth in capacity planning.

**Follow-ups you can defend:** object dependency graph; verification versus mutating tests; group-end cleanup; approximate timing scope; later expansion; personal lesson. **Unknown:** exact JUnit annotation/settings, worker counts, equal-hardware comparison, detailed timer components, concurrency validation beyond recalled behavior/logs. State uncertainty rather than filling it.

##### O2 — Making parallel-test output usable for debugging

**Relationship:** a challenge within O1, not an unrelated project.

**S:** Concurrent tests interleaved output, making individual test executions difficult to follow.

**T:** Make output attributable to the right test so the team could investigate failures.

**A:** Researched Java logging libraries and selected one that automatically prefixed entries with test-class and function details. Personally wrote a shell script that processed the combined output into class-based log files and separated function output within each file. The library's name is not remembered.

**R:** During test development and PR testing, the grouped logs helped identify parameters associated with mismatches in error messages, error codes, and returned resource fields. This is a qualitative diagnostic outcome; no measured reduction in debugging time, specific fixed defect, or production-monitoring system is established.

**Reflection — coaching synthesis, not a claimed historical statement:** Observability needs to remain usable as concurrency increases. You can discuss this as a present-day takeaway; do not invent a retrospective design document.

**Spoken answer:**

> One problem introduced by parallel testing was interleaved logs. I researched Java logging libraries and found one that automatically attached the test class and function to each entry. I then wrote a shell script to split the combined output into class-based files and separate the functions within them. During test development and PR testing, this helped us trace mismatched error codes, messages, or resource fields to the relevant parameter. We checked the expected behavior against the developer-provided specification and contacted the development point of contact when clarification was needed.

**Limits:** no assumed MDC/ThreadLocal, unique invocation IDs, exact parser commands, parameterized-test disambiguation, dashboards, on-call reduction, or restored global log order. Correct test attribution is the demonstrated mechanism.

##### O3 — Adapting provisioning and implementing environment lifecycle scripts

**S:** Test environments required OCI instances, readiness checks, and post-test cleanup. Earlier preparation included manual instance creation/restarts. Compute was shared across test pipelines.

**T:** Adapt provisioning for the team's environment and implement the surrounding lifecycle workflow, including failure evidence and cleanup.

**A:** Adapted existing Terraform scripts from parallel teams by changing authentication and tenancy/network configuration. Personally wrote the readiness-check script, the script enabling TeamCity log/artifact collection, and the instance-deletion script. Failed tests marked the pipeline failed and recorded error details in a separate artifact file. Cleanup ran despite earlier-step failures, including artifact-copy failure, to avoid holding compute needed by other pipelines.

**R:** Delivered that automated lifecycle workflow and a failure-record mechanism available to developers/testers. No measured cost saving, provisioning-speed reduction, fleet size, or release-cadence improvement is established. Cleanup execution is confirmed; guaranteed deletion success is not.

**Reflection:** The user recalls no artifact-collection issues and reported no retry/alternative-destination mechanism. The design prioritized cleanup, but could lose instance-local evidence if copying failed. A future improvement could use bounded collection retries or a separate durable log sink; these are hypothetical options, not work already done. Candidate's own proposed improvement has not yet been elicited.

**Spoken answer:**

> For test-environment automation, I adapted Terraform provisioning scripts from another team to our tenancy and network configuration. I personally wrote the surrounding scripts for instance readiness, TeamCity log and artifact collection, and compute-instance deletion. When tests failed, the pipeline remained failed and saved error details for investigation. Cleanup still ran so failed runs would not keep holding capacity needed by other pipelines. One limitation was that cleanup also proceeded if artifact collection failed. We did not encounter collection issues in my recollection, but I would acknowledge that risk rather than claim the workflow preserved every artifact under every failure.

**Limits:** readiness checks around instance state/storage/OS are tentative; exact scripts, commands and Terraform destroy are unconfirmed. “Reserving” was uncertain wording, not established OCI capacity-reservation work. Terraform's original scripts were reused; personal authorship concerns the surrounding scripts. Ansible details still need their own example.

##### O4 — Negative service-input validation: supporting mini-story

**S/T:** Validate service behavior against the development team's specification in the Docker-based test environment.

**A:** Sent a Protected Database creation request with a blank RSNI or recovery-policy identifier to the actual running service. Asserted the expected error code and message. Used test-attributed logs and the specification to investigate mismatches; contacted the development POC for ambiguity.

**R:** Implemented executable checks for the specified rejection behavior. No named defect, particular fix, defect count, or side-effect assertion has been reconstructed.

**Speak briefly:** “One example was validating rejection of Protected Database creation when a required RSNI or recovery-policy identifier was blank. These were tests against the actual service, with assertions on its error code and message. Expected behavior came from the development specification.”

**Coverage boundary:** The user recalls increases in service/function/line coverage but cannot reconstruct baselines or calculation. Lead with expanded coverage qualitatively. Do not substitute coverage for actionable-defect detection.

##### O5 — Migration validation: partial STAR

**S:** Customers migrated between Recovery Appliance environments.
**T:** Test protection and backup behavior through those scenarios.
**A:** Automated provisioning of required test resources, scenario execution, checks around recovery windows/data-loss exposure/protected states/backup continuity, and teardown.
**R:** Automated the described test workflow; exact defects found, assertion mechanics, and actual restore/recovery checks remain unknown.
**Reflection:** not yet reconstructed.

Use this as a scope description until a concrete scenario is recalled. Do not claim authorship of migration internals, physical-rack provisioning, or successful recovery from every pre-migration backup.

##### O6 — Hardware/PITR validation: partial STAR

**S/T:** Validate newly provided rack/bare-metal environments with PITR and functional tests.
**A:** Performed manual validation, documented procedures, and partially automated them toward TeamCity integration.
**R:** Validation/documentation and some automation completed; exact acceptance criteria, labor saved, automation coverage and incidents remain unknown.
**Reflection:** not yet reconstructed.

Do not assert formal certification authority, full unattended operation, or exact recovery commands from research alone.

##### How to use this bank

1. Lead with O1 for impact/performance and O3 for automation/failure handling.
2. Use O2 when asked about an obstacle or debugging, explicitly identifying it as part of O1.
3. Use O4 for a concrete example of test behavior; O5/O6 support broader scope but are not yet deep incident stories.
4. For missing details: “I don't recall the exact setting; what I implemented was …” Then stay within the known mechanism. Do not use confidentiality as an explanation for invented ownership.
5. Discuss a genuine weakness openly: delayed authoring guidelines, underestimated compute growth, or unconditional cleanup's diagnostic tradeoff. Do not manufacture a conflict, outage, or corrective feature.
6. Correct the inaccurate resume claim before using the test result. Do not describe a change of system and metric as merely clarifying the same accomplishment.

---
