# OA research ledger

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](amazon-10587705-phone-study-plan.md).

Last researched: **October 28, 2026**. Requisition 10587705, AWS Inference Optimization MLE II. No verified exact-team OA question report located. Public SDE accounts inform practice only. Publication dates are not interview dates. No question-frequency percentages can be supported by this sample.

## Sources used

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

## Requested sites and access limitations

- **LeetCode, NeetCode, Reddit:** used public original pages above. Reports are distinct from editorials and curriculum.
- **Glassdoor:** search-visible candidate extracts used cautiously, with interview date separated from post date. No invented full interview transcript or premium question list.
- **1point3acres:** searched Amazon/OA terms in English and Chinese. [Amazon tag listing](https://www.1point3acres.com/bbs/tag/amazon-56-119.html) exposes a brief OA-format entry but no usable complete current prompt. A URL ending `amazon-56-2026.html` is a pagination path, not evidence of year 2026; it surfaced old posts. A [2017 gated thread](https://www.1point3acres.com/bbs/thread-279101-1-1.html) is stale and excluded. No hidden text reconstructed. This source has not supplied a reliable current question to the bank.
- **Niche sources:** [amazon-oa.com](https://amazon-oa.com/) helped discover original reports; it is a third-party directory, not Amazon. Prefer original dates/text over its summaries. PracHub-related account S09 retained at low confidence. Promotional question dumps, cheating-tool posts, and unsupported frequency claims do not determine priorities.

## Exclusions that prevent misleading preparation

- [LeetCode SDE2 Bengaluru Aug 2026 report](https://leetcode.com/discuss/post/8499681/amazon-sde-2-selected-blr-aug-2026-by-dh-61y7/), posted Sep 3: grid/locker/config-sync questions belong to later interviews, not established OA questions.
- [LeetCode SDE2 July 2026 report](https://leetcode.com/discuss/post/8409230/interview-experience-amazon-sde-2-3-yoe-xkxue/): tree-distance, stack-middle and calculator questions came later. Its OA repo-task description is adjacent support only.
- [LeetCode upsolving thread](https://leetcode.com/discuss/post/7550047/upsolving-amazon-oa-by-anonymous_user-099n/): screenshot-only prompt not transcribed from unavailable content.
- [Reddit older OA thread](https://www.reddit.com/r/leetcode/comments/1htdjbf/): retrieval failed; no question adopted from this source. LC1561 is a curriculum recommendation, not a verified report from it.

## Technical references for synthetic exercises

These support principles, not claims about what Amazon asks:
- [AWS: idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
- [AWS: retries, timeouts and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/).
- [SQS: at-least-once delivery](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).
- [DynamoDB: read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

## Refresh procedure — every three days

1. Read the official packet if Suraj has provided it in this chat or the dossier. Record its date and replace conflicting assumptions, including task counts, timing, framework, assistance rules and expiry. Never open a live assessment to investigate its contents.
2. Search exact role/team first, then AWS/MLE II, then clearly labeled SDE II adjacent OA accounts. Use a recent window plus older sources only for gaps. Search LeetCode, Reddit, Glassdoor, 1point3acres, NeetCode updates and niche indexes; follow originals where accessible.
3. Capture publication date, actual interview date if known, level, geography, round, URL, access status and uncertainty. Distinguish firsthand reports, commenters, vendor summaries and inferred practice. Deduplicate authors/cross-posts. Exclude phone/loop-only prompts from OA evidence.
4. Prefer independently corroborated, relevant evidence over recency alone. A single new anecdote can justify one optional drill, not overhaul the plan. Do not attach invented frequency percentages.
5. Preserve question IDs, attempt history and corrected claims. Add questions only for a real coverage gap; retire superseded items with explanation. Update dated change log and source ledger. Refresh date is the actual research date, even if no changes qualify.
6. Prioritize the candidate's demonstrated error patterns when actual attempts exist; until then do not invent strengths, scores or readiness.
7. Notify only meaningful bank/format changes, an actionable access failure or a required clarification. If no meaningful change, update the research record quietly. Stop recurring OA work when the user confirms OA completion or asks to stop; do not infer completion from the planning date.
