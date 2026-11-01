# Amazon MLE II — online assessment question bank

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](amazon-10587705-phone-study-plan.md).

**Current daily schedule:** [Combined two-week study plan](amazon-10587705-two-week-study-plan.md). This supersedes earlier daily sequencing; question IDs remain unchanged.

**Updated:** October 28, 2026 · **Role:** AWS Inference Optimization, 10587705  
**Scope:** OA only. Research-informed practice, not a prediction of an exact test. No verified account for this exact requisition was found.

## Start here

The recruiter call went well, per Suraj. His report sets the working format: **70 minutes coding + 20 minutes AI coding + 20 minutes system design + 10 minutes behavioral**. The number of coding questions, platform, permitted languages/frameworks, AI boundaries, scoring, and whether sections are separately timed remain unconfirmed. The official invitation will supersede this plan.

Suraj has two weeks to take the assessment. **November 11 is a planning estimate**, not a verified expiry. Target a practice-ready date of November 8; use the actual invitation for the deadline. Later telephone and loop rounds are recorded in the main dossier but are outside this bank.

Amazon's public **SDE II** OA page describes a different structure (90-minute coding, design and workstyle). That is adjacent guidance, not authority for this MLE invitation. [Official SDE II OA guidance](https://www.amazon.jobs/content/en/how-we-hire/sde-ii-oa-prep)

**Priority:** P0 = first pass; P1 = coverage after P0; P2 = stretch after diagnosing weaknesses. Priority measures training value, not claimed Amazon frequency. All LC rows below are **practice recommendations**; report mappings are separately identified. Use [NeetCode's curriculum](https://neetcode.io/practice/practice/neetcode150) for explanations after an attempt, not as evidence of Amazon frequency.

**Today:** attempt LC 560 and 994 in one 70-minute session, then AI-01 (20 min), SD-01–04 (20 min total), and a 10-minute workstyle practice. Log errors before reading solutions. These form a diagnostic; they are not a pass prediction.

## Supplementary domain preparation

The [cross-company ML/inference bank](ml-inference-engineering-question-bank.md) covers transformers, attention, vLLM/SGLang, kernel optimization and ML engineering in coding, design, conceptual and case-study formats. These are broader technical-round exercises, not newly confirmed OA requirements.

## A. LeetCode practice bank — 38 questions

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

## B. Candidate-reported OA families — separate from canonical practice

Sources and limitations are in [the research ledger](amazon-10587705-oa-sources.md). All accounts are self-reported and adjacent to this role. Prompts below are brief paraphrases; follow the linked original for supplied constraints. Do not silently fill missing constraints.

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

## C. Distributed systems — 24 short scenarios

These are **original practice scenarios**, not claimed leaked/reported Amazon questions. An older candidate described a live-view-counter simulation with storage/prioritization choices (S08); recent discussion also mentions effectiveness ratings (S07). That supports practicing concise decisions, but does not establish your exact UI.

Use [scenario prompts and answer checkpoints](amazon-10587705-oa-scenarios.md). Each SD question takes 4–5 minutes: identify the requirement, pick a design, name its failure mode, and explain one tradeoff. Four scenarios make a 20-minute block. Do not spend this block drawing an entire large-system architecture unless the official instructions request it.

## D. AI-assisted coding — 12 drills

Use [the detailed drill specifications](amazon-10587705-oa-scenarios.md#ai-assisted-coding-drills). These are original bounded practice tasks inspired by repo debugging reports, not a claim that this MLE test uses a particular backend framework. Reported 40/60 or 100-minute assessments differ from your 20-minute AI section; train to your recruiter's timing.

Practice in an existing small local application and its tests. For a fresh mock, have a helper seed the described defect without showing the patch. The bank supplies requirements and acceptance cases, not a runnable hidden-test repository. Choose the strongest offered language after the packet arrives; do not spend the next fortnight learning an unconfirmed framework.

20-minute routine: 0–3 read task/run baseline; 3–6 reproduce and inspect the failing path; 6–13 request and review a small patch; 13–18 run targeted plus regression tests; 18–20 inspect diff and explain remaining limitations. During practice use AI for this section only; the invitation decides what assistance is allowed in the actual assessment.

Useful prompt: “Read these requirements and failing tests. Identify the smallest likely cause, cite the relevant code, and propose a minimal patch. Preserve public APIs. Add a regression case for the failure; explain behavior at boundaries.” Reject patches that weaken tests, hard-code examples, or rewrite unrelated modules.

## E. Two-week sequence

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

**Practice readiness heuristic (not Amazon's bar):** two fresh timed coding sessions with correct implementations and boundary tests; a bounded AI fix without regressions in 20 minutes; four design decisions in 20 minutes with explicit tradeoffs. Log actual outcomes in [attempts.csv](amazon-10587705-oa-attempts.csv). All items start unattempted; no readiness inferred from existing job experience.

## Maintenance

Research baseline: Oct 28. Desired refresh every three days: Oct 31, Nov 3, Nov 6, Nov 9, continuing until OA completion or a user change. Consult the automation's displayed schedule for actual run timing. Preserve IDs and attempts; add dated evidence and retire weak claims rather than silently replacing them. See the source ledger for selection rules.

### Change log
- 2026-10-28: Initial OA-only bank: 38 canonical coding exercises, 7 reported families, 24 distributed-system scenarios, 12 AI coding drills; recruiter format recorded pending official packet.
