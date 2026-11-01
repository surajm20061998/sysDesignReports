# Inference-engine interview research — evidence and study resources

**Researched October 28, 2026.** Focus: inference, optimization and vLLM/SGLang. Companion to [32 targeted questions](inference-engines-question-bank.md). Exact target remains Amazon MLE II AWS Inference Optimization, live interview November 12. Interview questions from other companies support preparation, not predictions about Amazon.

## What interview accounts actually support

1. **NVIDIA inference phone screen — specific firsthand account.** [LeetCode original](https://leetcode.com/discuss/post/6809037/), Sukanya Saha, published June 4, 2025. Role Deep Learning Software Engineer—Inference; hiring-manager phone screen, exact seniority/location/interview date unspecified. Reports CUDA kernel/optimization challenges, model-serving/vLLM follow-ups, exact project contributions, and tree serialization coding. This is the same source already in the domain ledger, not a new independent corroboration. It supports project defense plus systems understanding; it provides no precise vLLM scheduler coding prompt.
2. **Fireworks applied ML — adjacent reported themes.** [Glassdoor reviews](https://www.glassdoor.com/Interview/Fireworks-AI-Interview-Questions-E9514416.htm): Jul 31, 2026 Applied MLE account discusses RAG optimizations and TTFT; Aug 17 review describes an Aug 2026 AI Engineer interview in New York with evaluation/model-selection/latency questions. Previous search-visible review extracts are retained; current direct page retrieval did not expose equivalent full review bodies. No exact kernel-engineer attribution.
3. **Anthropic SWE onsite — anonymous specific account.** [Reddit](https://www.reddit.com/r/Technical_Interview/comments/1wswnys/sweanthropic_anthropic_onsite_interview_experience/), recent October 2026, actual interview date/level/location unconfirmed. Describes inference design review, batching/rate limits and fixed-capacity scheduling for one-unit versus eight-unit models. Same source already recorded in the domain ledger. Supports scheduling/capacity follow-ups.
4. **Anthropic Fellowship OA — additional low-confidence lead.** [Reddit InterviewDB](https://www.reddit.com/r/InterviewDB/comments/1vm1ooz/anthropic_fellow_program_assessment_questions/), page says two months ago as of access, exact posting/interview date unclear; November cohort mentioned, no independently verified year. Account describes a supplied vLLM-like codebase involving cache/prefill and undocumented APIs. Author is a question-aggregation account; [Karavine repost](https://www.reddit.com/r/Karavine/comments/1w3lpf0/anthropic_fellowship_oa_interview_experience_vllm/) promotes a paid pack. Treat as a low-confidence possibly overlapping cluster, not two independent confirmations. This is an OA for a different program, not evidence Amazon will use a repository exercise.

**Evidence boundary:** no attributable exact SGLang interview transcript or reliable vLLM/SGLang question-frequency data was found. Searches covered NVIDIA, Together AI, Fireworks, Anthropic and general inference-engineer reports in LeetCode, Reddit, Glassdoor-indexed pages and Chinese interview-note indexes. Commercial guides and LinkedIn “asked at NVIDIA” content often lack candidate/date/round provenance. Do not promote them to verified question reports.

A Deep-ML inference path sometimes labels papers, role postings or tutorial sites as “reportedly asked at.” Those labels alone are not interview evidence. Use its coding exercises as educational practice; verify employer claims against an original candidate account. Source duplication and web freshness do not establish repeated interview frequency.

## Primary references for engine practice

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
| P01 | [Local project/PR audit](amazon-10587705-project-pr-review.md) | vLLM timing/logging/resource-budget scope and Triton experiment limits. Evidence audit, not fresh experiment reproduction. |
| P02 | [SGLang contribution section of the same audit](amazon-10587705-project-pr-review.md) | Queue re-entry accumulation, serialization/reset and recorded PD caller-path caveat. No fresh upstream-resolution verification performed. |

Some SGLang `.md` links from the official index returned unsupported-content-type errors in the web reader. Their corresponding HTML pages were successfully opened above. No unavailable content was reconstructed.

## Learning order — make code understandable

**First:** explain prefill/decode with a two-token prompt and one generation step. Draw Q/K/V shapes and what remains in the cache.

**Next:** work through ECODE-01/02/03 using lists, dictionaries and explicit timestamps. These teach engine state changes without NumPy broadcasting. Then do ECODE-04/05 for cache ownership/prefix matching. Finally add a model computation using the existing CODE-02/03 attention references.

**Read and discuss:** E01 and E02 for vLLM; E08 and E10 for SGLang; then E13 for experimental practice. You should be able to draw the mechanism and name a workload that benefits and one that may not.

**Resources to practice implementation:** [Deep-ML K-means](https://www.deep-ml.com/problems/17), [softmax](https://www.deep-ml.com/problems/23), [simple self-attention](https://www.deep-ml.com/problems/955), and [multi-head attention](https://www.deep-ml.com/problems/94). Read each contract: the simplified self-attention task is not a full causal decoder implementation. Employer labels on educational pages are not used as evidence here.

## Research update rules

Preserve this bank's IDs, attempt history and source uncertainty. Add dated original reports when available; do not repackage the same NVIDIA report as several independent signals. Prefer pinned code/version references for implementation claims. Keep confirmed interview constraints above speculative research. Use actual practice errors to narrow revision; no unobserved skill/readiness claims.

Research outcome: existing evidence reinforces project ownership, latency/evaluation reasoning and scheduling depth. The main additions are a low-confidence repository-exercise lead, current engine-specific references, 32 targeted prompts and a smaller-step coding sequence. No new exact Amazon team question list was found.


## Research refresh — October 31, 2026

Rechecked inference-engine interview searches and reopened the original NVIDIA screen account (https://leetcode.com/discuss/post/6809037/). This remains one June 2025 report, not fresh independent corroboration. No new original vLLM/SGLang question account met the evidence threshold. Candidate preparation requests, educational question lists, promotional reposts and papers mislabeled as interview evidence were not promoted.

Revalidated the existing mechanisms against the current vLLM tuning page (https://docs.vllm.ai/en/latest/configuration/optimization/) and SGLang tuning page (https://docs.sglang.io/docs/advanced_features/hyperparameter_tuning). vLLM's current V1 guidance still describes decode-prioritized chunked prefill and default recomputation preemption; SGLang still distinguishes static weights/cache allocation from graph/activation headroom. No plan-changing technical correction was identified. Keep implementations version-aware and measure workload tradeoffs. All 32 IDs and the small-function learning sequence retained; no attempt outcomes added.
