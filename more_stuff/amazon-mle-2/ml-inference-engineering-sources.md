# Cross-company inference interview research — source ledger

**Accessed:** October 28, 2026. Companion to [the bank](ml-inference-engineering-question-bank.md). Reported questions are evidence of an individual account, not an employer promise or a frequency estimate. Technical references support our original exercises, not claims about what an interviewer asked.

## Candidate accounts

### R01 — NVIDIA inference phone screen

[Original LeetCode account](https://leetcode.com/discuss/post/6809037/), author Sukanya Saha, posted **June 4, 2025**. Role: Deep Learning Software Engineer—Inference. Round: first technical phone screen with hiring manager. Actual interview date, location and seniority not specified. Candidate reports CUDA/project ownership and vLLM-serving discussion plus tree serialization coding. Specific and relevant firsthand account; independently unverified and not a full loop. REP-01–03 come from this single account. Do not infer that NVIDIA always asks these questions or that their kernel round was a live CUDA exercise.

### R02 — Fireworks AI applied-ML interviews

[Glassdoor candidate reviews](https://www.glassdoor.com/Interview/Fireworks-AI-Interview-Questions-E9514416.htm). Search-visible review text was available; directly opening the current page returned its surrounding structure without the same full review bodies. This access limitation is retained.

- **Applied Machine Learning Engineer**, posted **July 31, 2026**: RAG take-home, project/take-home discussion, TTFT optimization. Exact interview date/location unstated; onsite still pending in the account.
- **AI Engineer, New York**, interview **August 2026**, posted **August 17, 2026**: text-to-SQL assignment, model/dataset evaluation and latency discussion.

These support applied-ML and serving-performance themes, not a claim about Fireworks kernel-engineer interviews. Anonymous candidate reports, not company-confirmed questions. REP-04–05 summarize these reviews. The current page's aggregate update date is not an interview date.

### R03 — Anthropic SWE onsite

[Reddit original account](https://www.reddit.com/r/Technical_Interview/comments/1wswnys/sweanthropic_anthropic_onsite_interview_experience/), u/CollegeBotHelper. Recent **October 2026** post based on relative page date; exact publication/interview day unconfirmed. Level/location unspecified. Describes multiprocessing and intermediate-prefix reuse, plus inference design review and scheduling with one-unit versus eight-unit model requirements. Anonymous self-report with useful specifics; authenticity not independently verified. REP-06–07 paraphrase a single account. Do not equate it with an ML/kernel specialist process.

### R04 — Together AI SWE onsite (low confidence)

[Reddit report](https://www.reddit.com/r/OfferEngineering/comments/1wj52vj/together_ai_swe_onsite_interview_experience_sep/), posted **September 17, 2026**, titled September onsite experience. Explicitly sourced from the commercial “Chill Interview” service: **secondhand promotional repost**, not a verified original candidate submission. Describes multi-cluster scheduling and timestamped key/value retrieval. Retained as optional inspiration for REP-08 only. The canonical coding analogue is [LeetCode 981](https://leetcode.com/problems/time-based-key-value-store/). No inference-specialist level or team established.

## Coverage and exclusions

- NVIDIA, Fireworks, Together AI and Anthropic had relevant public accounts or clearly limited adjacent material. These companies do not share one standardized interview process.
- [Together AI Glassdoor](https://www.glassdoor.com/Interview/together-ai-CA-Interview-Questions-E10746640.htm) exposed general project/background questions, not an attributable attention/kernel task. No domain prompt was manufactured from it.
- Cerebras searches surfaced [upcoming Kernel Reliability interview questions from a candidate](https://www.reddit.com/r/leetcode/comments/1sgvspt/interview_with_cerebras/) and [an AI Inference Core candidate seeking advice](https://www.reddit.com/r/leetcode/comments/1vftt7h/cerebras_infrastructure_swe_interview_insights/). Asking what to expect is not a report of questions asked; excluded as question evidence.
- Modular/GPU compiler searches did not yield a usable attributable domain-question account in this pass. No company-specific questions assigned.
- Generic interview guides, anonymous commercial question dumps and “starter” community posts were discovery leads, not independent evidence. No frequency/pass-rate claims copied.
- No paywalled or hidden interview text reconstructed. Broader general coding remains represented by the reported NVIDIA/Together examples; this bank focuses on domain preparation rather than duplicating the OA DSA curriculum.

## Primary technical references

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

## Refresh contract

When updating this bank, preserve IDs and attempts. Search original candidate accounts first, then use company-authored engineering sources to address coverage gaps. Date interview and publication separately. Record company, role, round, geography and confidence where available. Tag expanded prompts as original practice; never turn a broad theme into a supposedly verbatim question. Add stronger evidence to existing items before inflating the bank. Keep this domain bank distinct from confirmed Amazon OA requirements.

### Research log

- **2026-10-28:** Initial public-source research. Eight reported prompts/themes across four companies (three of the eight from one NVIDIA account; Together evidence low-confidence). Seventy-two original exercises backed by primary references or explicitly original engineering scenarios. No GPU testing performed.


- **2026-10-31 refresh:** No new sufficiently attributable exact-team or engine-specific candidate question qualified for addition. Existing NVIDIA account and engine tuning references rechecked; full search/exclusion record is in `inference-engines-research.md` and `amazon-10587705-phone-research.md`. Banks, IDs, schedule and attempt history preserved. No readiness conclusion drawn.
