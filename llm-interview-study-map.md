# LLM Interview Question Study Map

This guide reorganizes the supplied question bank by concept rather than by the order in which the questions appeared. The numeric suffixes in the source text appeared to be unresolved citation markers, so they have been omitted here.

## Recommended study order

1. LLM behavior and context
2. RAG foundations and debugging
3. Evaluation and hallucination control
4. Agents and tool use
5. Safety and guardrails
6. Production monitoring
7. Cost and latency
8. Fine-tuning and model internals only when the role requires them

The first seven areas are the core AI-engineering interview curriculum. Fine-tuning, training, and transformer internals are the specialization layer.

---

## 1. LLM behavior and control

### Bucket 1A — Generation mental model and sampling

Questions:

- How do LLMs work?
- What are temperature and top-p sampling, and how do they affect outputs?

What to learn: next-token prediction, tokens, logits/probabilities, autoregressive generation, deterministic versus stochastic decoding, temperature scaling, nucleus sampling, and why low temperature is not a factuality guarantee.

Sources:

- [Andrej Karpathy — Intro to Large Language Models (video)](https://www.youtube.com/watch?v=zjkBMFhNj_g) — the best high-level mental model before studying application design.
- [Hugging Face LLM Course — Transformer models](https://huggingface.co/learn/llm-course/chapter1/1) — structured reading on model behavior and inference.
- [Hugging Face — Text generation strategies](https://huggingface.co/docs/transformers/generation_strategies) — practical decoding and sampling reference.

### Bucket 1B — Context windows, long documents, and memory

Questions:

- What is the context window, and what happens when you exceed it? How do you handle long documents?
- How do you do memory management and context management with LLMs?

What to learn: input/output token budgets, truncation, lost-in-the-middle behavior, chunking, retrieval, rolling summaries, compaction, episodic versus semantic memory, external state stores, and the distinction between model context and durable application memory.

Sources:

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — practical context selection, compression, and memory patterns.
- [Hugging Face — Handling multiple sequences](https://huggingface.co/learn/llm-course/en/chapter2/5) — padding, truncation, and model input limits.
- [OpenAI — Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) — useful for understanding repeated long-context cost and latency.

---

## 2. RAG systems

### Bucket 2A — End-to-end RAG and retrieval choices

Questions:

- What is RAG? Explain the complete process.
- Text search versus vector search: when would you use each?
- What are the key trade-offs when designing a RAG system?

What to learn: ingestion, cleaning, chunking, metadata, embeddings, indexing, sparse/BM25 retrieval, dense retrieval, hybrid retrieval, reranking, context packing, grounded generation, and latency/quality/freshness trade-offs.

Sources:

- [AWS — Understanding retrieval-augmented generation](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html) — clean end-to-end overview.
- [Microsoft — Build advanced RAG systems](https://learn.microsoft.com/en-au/azure/developer/ai/advanced-retrieval-augmented-generation) — production design and mitigation strategies.
- [Full Stack Deep Learning — LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/) — video-based application curriculum, including augmented language models and LLMOps.

### Bucket 2B — Document ingestion, PDFs, chunking, and citations

Questions:

- You are making a system for huge PDF reports. How would you process them?
- How do you handle citations and source attribution in a RAG system?

What to learn: layout-aware parsing, OCR, tables and figures, section-aware chunking, page/section metadata, stable chunk identifiers, parent-child retrieval, claim-to-source mapping, citation validation, and document access control.

Sources:

- [Microsoft Azure Architecture Center — RAG information-retrieval phase](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval) — ingestion, chunking, retrieval, and evaluation architecture.
- [Unstructured documentation — Partitioning](https://docs.unstructured.io/open-source/core-functionality/partitioning) — practical PDF and document parsing concepts.
- [AWS RAG guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html) — review the cleaning, chunking, embedding, and metadata stages together.

### Bucket 2C — Grounding, abstention, failure analysis, and debugging

Questions:

- How would you handle a model hallucinating when no information is found in the given context?
- What are common RAG failure points, and how do you debug them?

What to learn: explicit abstention policy, answerability detection, confidence calibration, retrieval miss versus generation failure, query rewriting, chunk inspection, retrieval traces, top-k/reranker analysis, access-filter errors, stale indexes, and adversarial test cases.

Sources:

- [Microsoft Foundry — RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) — separates retrieval relevance, groundedness, completeness, and final-answer quality.
- [Microsoft Fabric — Assessing RAG performance](https://learn.microsoft.com/en-us/fabric/data-science/tutorial-evaluate-rag-performance) — practical top-N retrieval and end-to-end testing.
- [Anthropic — Contextual retrieval](https://www.anthropic.com/news/contextual-retrieval) — techniques for reducing retrieval failures caused by context-poor chunks.

### Bucket 2D — Caching and large-scale retrieval

Questions:

- What is semantic caching?
- How do you scale a RAG system to more than 10 million articles?

What to learn: exact versus semantic caches, similarity thresholds, tenant and permission isolation, invalidation, freshness, approximate nearest-neighbor indexes, sharding, replication, metadata filtering, hybrid retrieval, reranking, incremental indexing, and capacity planning.

Sources:

- [Redis — Semantic caching](https://redis.io/blog/what-is-semantic-caching/) — accessible explanation of cache keys based on semantic similarity.
- [Pinecone — Understanding vector indexes](https://docs.pinecone.io/guides/indexes/understanding-indexes) — operational concepts for vector search at scale.
- [Microsoft — RAG information-retrieval phase](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval) — retrieval metrics and index-design considerations.

---

## 3. Agents and tool use

### Bucket 3A — What agents are and when to use them

Questions:

- What makes an AI system agentic?
- What are the essential components of an agent beyond an LLM?
- When is an agent the wrong solution?
- How do you explain agentic systems to non-technical stakeholders?

What to learn: the agent loop, model/harness/tools/environment, workflows versus agents, autonomy levels, state and memory, permissions, human oversight, and the latency/cost/predictability trade-off.

Sources:

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — the primary resource for workflows versus agents, patterns, and when not to use an agent.
- [Anthropic — Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents) — model, harness, tools, environment, autonomy, and oversight.

### Bucket 3B — Tool selection and reliable execution

Questions:

- How do agents decide which tool to use?
- How do you handle tool failures, retries, and idempotency?

What to learn: tool schemas and descriptions, argument validation, constrained outputs, routing, tool-result interpretation, timeouts, retry classes, exponential backoff, idempotency keys, deduplication, compensation, and audit logs.

Sources:

- [OpenAI — Function calling](https://developers.openai.com/api/docs/guides/function-calling) — tool definition, schema, and tool-call lifecycle.
- [Anthropic — Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — how tool interfaces affect selection and agent performance.
- [AWS Builders' Library — Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) — essential distributed-systems background.

### Bucket 3C — Loops, termination, sandboxing, and agent security

Questions:

- How do you detect and stop infinite planning loops?
- How do you implement termination conditions in long-running agents?
- How do you sandbox tool execution safely?
- What are the biggest security risks with tool-using agents?

What to learn: explicit success criteria, step/tool/token/time/cost budgets, repeated-state detection, no-progress detection, circuit breakers, checkpoints, human escalation, least privilege, capability allowlists, network/filesystem isolation, prompt injection, excessive agency, and complete mediation.

Sources:

- [OWASP — Excessive agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html) — concrete failure modes and mitigations for tool-using systems.
- [LangChain — Prebuilt middleware](https://docs.langchain.com/oss/javascript/langchain/middleware/built-in) — examples of tool-call limits and human-in-the-loop controls.
- [Anthropic — Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents) — permissions, approvals, prompt injection, and user control.

### Bucket 3D — Agent system-design exercises

Questions:

- Design an agent that analyzes customer-support tickets, drafts responses, and escalates complex issues.
- Build an agent that reviews code and suggests improvements.

What to learn: convert the product requirement into inputs, workflow stages, tools, state, decision points, approval boundaries, escalation paths, evaluation criteria, failure handling, observability, privacy, and rollout strategy. For both exercises, first explain whether a deterministic workflow is sufficient before adding autonomy.

Sources:

- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — map the problem to routing, parallelization, orchestrator-worker, or evaluator-optimizer patterns.
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — design task-level and trajectory-level tests with the system.

---

## 4. Testing and evaluation

### Bucket 4A — Evaluation strategy, datasets, and metrics

Questions:

- How do you ensure outputs from LLMs are consistent and accurate?
- How do you evaluate a chatbot?
- What metrics do you consider when evaluating LLM performance?
- How do you build a golden dataset for evaluation?

What to learn: task definition, representative slices, happy/edge/adversarial cases, deterministic checks, reference-based metrics, rubric-based human evaluation, calibrated LLM judges, pairwise comparison, inter-rater agreement, regression thresholds, and versioned golden datasets.

Sources:

- [OpenAI — Working with evals](https://developers.openai.com/api/docs/guides/evals) — practical evaluation lifecycle and grader design.
- [OpenAI Cookbook — Evaluation examples](https://cookbook.openai.com/topic/evals) — runnable patterns for datasets, graders, and comparisons.
- [Hugging Face — Model evaluation course](https://huggingface.co/learn/smol-course/unit4/1) — model and task evaluation concepts.

### Bucket 4B — Hallucination and factuality

Questions:

- How do you detect and mitigate hallucinations?
- How would you prevent factual errors in a summarization system?
- How do you debug a RAG chatbot that gives confident but wrong answers?

What to learn: classify hallucinations, source-grounded claims, entailment/faithfulness checks, citation verification, abstention, retrieval diagnostics, constrained summarization, human review for high-risk cases, and production sampling.

Sources:

- [Microsoft Foundry — Groundedness and RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) — direct mapping from these questions to measurable dimensions.
- [NIST — Generative AI risk-management profile](https://www.nist.gov/itl/ai-risk-management-framework) — broader treatment of confabulation and measurement risk.
- [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — test design and grader reliability.

### Bucket 4C — Component-level RAG and agent evaluation

Questions:

- How do you evaluate a RAG pipeline?
- How do you evaluate agent performance? What metrics matter, including tool-selection quality, action advancement, and context adherence?

What to learn: evaluate retrieval and generation separately; recall@k, precision@k, MRR, NDCG, context relevance, groundedness, answer completeness, citation correctness, task success, tool correctness, argument correctness, trajectory efficiency, side effects, recovery, policy compliance, and cost/latency.

Sources:

- [Microsoft Foundry — RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) — component and system metrics.
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — multi-turn environments, transcripts, grading, and agent-specific failure modes.

---

## 5. Production monitoring

### Bucket 5A — Offline-to-online evaluation and rollout

Questions:

- What operational and business metrics matter for AI systems?
- How would you evaluate and monitor a model in production, not just offline?
- How would you test a new model before full deployment?

What to learn: quality, safety, latency, availability, error rate, token usage, cost, escalation, containment, conversion, resolution, retention, user feedback, offline gates, shadow traffic, canaries, A/B tests, rollback, and segment-level dashboards.

Sources:

- [Weights & Biases — Evaluating LLMs in production](https://site.wandb.ai/articles/evaluating-llms-in-production/) — connects traces, drift, eval sets, and continuous monitoring.
- [Weights & Biases — LLM observability](https://wandb.ai/site/articles/llm-observability/) — distinguishes monitoring from debugging-oriented observability.

### Bucket 5B — Hallucination and autonomous-agent monitoring

Questions:

- How do you measure hallucination rate in production?
- How do you monitor and observe autonomous-agent behavior in production?

What to learn: sampled online grading, human audits, user reports, citation/grounding checks, confidence intervals, trace/span schemas, prompt/model/tool versions, full trajectories, side effects, loop and no-progress alerts, anomalous tool use, and privacy-preserving logs.

Sources:

- [W&B — Online evaluations](https://wandb.ai/site/online-evaluations/) — sampling and continuous scoring of production traces.
- [W&B documentation — Monitors](https://docs.wandb.ai/weave/guides/evaluation/monitors) — passive scoring and trend analysis.
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — what an agent transcript must capture for meaningful analysis.

---

## 6. Cost and latency optimization

### Bucket 6A — Latency measurement and pipeline optimization

Questions:

- How do you reduce latency in generative-AI applications?
- What is time to first token, and why does it matter for user experience?
- How would you benchmark each LLM call in a multi-step pipeline to identify latency bottlenecks?

What to learn: TTFT versus inter-token latency versus end-to-end latency, streaming, critical paths, parallel calls, fewer calls, smaller prompts, output-length control, caching, speculative work, tracing spans, percentiles, cold starts, queuing, and service-level objectives.

Sources:

- [OpenAI — Latency optimization](https://developers.openai.com/api/docs/guides/latency-optimization) — practical seven-principle optimization guide.
- [vLLM — Optimization and tuning](https://docs.vllm.ai/en/stable/configuration/optimization/) — serving-level batching, prefill, and parallelism.

### Bucket 6B — Token cost, model routing, and quality trade-offs

Questions:

- How do you reduce token costs?
- Cost versus quality: when is a small open-source model good enough?
- What is model tiering? When do you route to a small distilled model versus a large LLM?

What to learn: prompt/output reduction, caching, batching, model pricing, routing features, confidence thresholds, cascades, fallback policies, distillation, quantization, task-specific evals, and total cost of ownership for hosted versus self-hosted models.

Sources:

- [OpenAI — Cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization) — token, model, cache, batch, and workload strategies.
- [Hugging Face — LLM inference optimization](https://huggingface.co/docs/transformers/v4.44.0/en/llm_optims) — KV cache and serving optimizations for open models.
- [Hugging Face — Quantization](https://huggingface.co/docs/transformers/main_classes/quantization) — memory/speed/quality trade-offs.

### Bucket 6C — Capacity planning and cost estimation

Questions:

- Your application receives one million queries per day. How do you optimize cost?
- Estimate the budget for a RAG pipeline at enterprise scale, such as 300,000 legal contracts.

What to learn: state assumptions explicitly; separate one-time ingestion/OCR/embedding/index costs from recurring query/retrieval/reranking/generation/storage/observability costs; use average and p95 tokens; model cache hit rate, concurrency, retries, growth, and evaluation overhead; then present base/expected/worst-case scenarios.

Sources:

- [OpenAI — Cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization) — recurring inference levers.
- [AWS — RAG guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html) — use the pipeline stages as the cost-model line items.
- [vLLM — Anatomy of a high-throughput inference system](https://vllm-project.github.io/2025/09/05/anatomy-of-vllm.html) — useful when comparing hosted APIs with self-hosted capacity.

---

## 7. Safety and guardrails

### Bucket 7A — Guardrail architecture and content policy

Questions:

- When and how would you implement LLM guardrails?
- How would you build a system that detects whether content violates policy or contains offensive material?

What to learn: input, retrieval, tool, and output controls; deterministic validation; classifiers/moderation models; policy taxonomies; thresholds; multilabel classification; calibration; human review; false-positive/false-negative trade-offs; red teaming; and auditability.

Sources:

- [NIST — AI Risk Management Framework and Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework) — governance and risk framing.
- [OpenAI — Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices) — application-level safety controls.
- [OWASP — Top 10 for LLM applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — threat-driven guardrail checklist.

### Bucket 7B — Privacy, PII, prompt injection, and jailbreaking

Questions:

- How do you handle data privacy and PII in prompts and logs?
- How do you protect against prompt injection and jailbreaking?

What to learn: data minimization, consent and purpose limitation, redaction/tokenization, encryption, retention, access controls, tenant isolation, vendor data policies, audit logs, direct versus indirect injection, trust boundaries, instruction/data separation, allowlisted tools, least privilege, human approval, and why prompt-only defenses are insufficient.

Sources:

- [OWASP — Prompt injection](https://owasp.org/www-community/attacks/PromptInjection) — attack taxonomy and practical mitigations.
- [OWASP — Top 10 for LLM applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — sensitive-information disclosure, prompt injection, and excessive agency.
- [NIST — Generative AI risk-management profile](https://www.nist.gov/itl/ai-risk-management-framework) — privacy and security risk treatment.

### Bucket 7C — Safe generated-code execution

Questions:

- Your application generates code that gets executed. How do you prevent malicious code generation and execution?

What to learn: never treat model output as trusted code; isolate processes/VMs/containers; deny network by default; use ephemeral filesystems; mount only required data read-only; drop privileges; allowlist operations; cap CPU/memory/time/output; scan dependencies and code; protect secrets; require approval for consequential actions; and retain auditable execution traces.

Sources:

- [OWASP — Insecure output handling and excessive agency](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — the security model behind safe execution.
- [gVisor documentation](https://gvisor.dev/docs/) — concrete sandbox-isolation architecture.
- [Firecracker documentation](https://firecracker-microvm.github.io/) — microVM isolation for untrusted workloads.

---

## 8. Classical ML fundamentals

### Bucket 8A — Core machine-learning interview theory

Topics:

- Supervised versus unsupervised learning
- Bias-variance trade-off
- Regularization
- Data handling and leakage
- Model architectures
- Interpretability
- Probability and statistics

Primary source from the supplied list:

- [Alexey Grigorev — Data Science Interviews](https://github.com/alexeygrigorev/data-science-interviews)

Suggested companion:

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — structured refreshers and exercises.

---

## 9. Fine-tuning and training — specialization

### Bucket 9A — Choosing prompt engineering, RAG, or fine-tuning

Questions:

- When would you fine-tune versus use prompt engineering versus RAG?
- What is instruction tuning, and how does it differ from pretraining?

What to learn: changing knowledge versus changing behavior, freshness and citations, labeled-data requirements, maintenance cost, evaluation gates, pretraining objectives, supervised fine-tuning, and instruction-response datasets.

Sources:

- [Hugging Face — Fine-tuning course](https://huggingface.co/learn/smol-course/unit0/1) — instruction tuning through preference alignment.
- [Hugging Face LLM Course — Fine-tuning a pretrained model](https://huggingface.co/learn/llm-course/chapter3/1) — practical fine-tuning foundation.

### Bucket 9B — PEFT, LoRA, quantization, and efficiency

Questions:

- What are PEFT and LoRA, and when would you use them?
- Explain quantization. What are the trade-offs among model size, speed, and accuracy?

What to learn: frozen base weights, low-rank adapters, rank and target modules, adapter serving, QLoRA, weight/activation/KV-cache quantization, INT8/INT4/FP8, calibration, memory savings, hardware support, and quality regression testing.

Sources:

- [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/index) — conceptual and implementation reference.
- [Hugging Face bitsandbytes documentation](https://huggingface.co/docs/bitsandbytes/index) — 8-bit inference and QLoRA.
- [Hugging Face — Quantization](https://huggingface.co/docs/transformers/main_classes/quantization) — supported approaches and configuration.

### Bucket 9C — RLHF, DPO, and behavioral feedback

Questions:

- Explain the RLHF pipeline: supervised fine-tuning, reward-model training, and PPO. How does DPO simplify this?
- How do you convert implicit user behavior—edits, acceptance, and rejection—into training signals for model improvement?

What to learn: preference-pair construction, selection bias, noisy implicit feedback, propensity/confounding, reward modeling, policy optimization, KL control, DPO's reference policy, holdouts, offline evaluation, and safe feedback flywheels.

Sources:

- [Hugging Face — Illustrating RLHF](https://huggingface.co/blog/rlhf) — SFT, reward modeling, and PPO overview.
- [Hugging Face — Preference alignment and DPO](https://huggingface.co/learn/smol-course/unit2/1) — why DPO removes the explicit reward-model/PPO stages.
- [Direct Preference Optimization paper](https://arxiv.org/abs/2305.18290) — primary research source.

### Bucket 9D — End-to-end training system design

Questions:

- How would you design a model that can solve math problems? Walk through data collection, supervised fine-tuning, post-training, and evaluation.

What to learn: define target tasks and difficulty slices, collect/licence/deduplicate data, verify answers and reasoning traces, prevent contamination, choose base model, run SFT, add preference or verifier-based post-training, use tool augmentation where appropriate, evaluate exact answer and process separately, red-team, and monitor regressions.

Sources:

- [Hugging Face — Build reasoning models](https://huggingface.co/learn/llm-course/chapter12/1) — focused reasoning-model curriculum.
- [Hugging Face fine-tuning course](https://huggingface.co/learn/smol-course/unit0/1) — training and evaluation workflow.

---

## 10. LLM theory — specialization

### Bucket 10A — Transformers, attention, and architecture families

Questions:

- How do transformers work?
- What is the self-attention mechanism?
- What is the difference among encoder-only, decoder-only, and encoder-decoder Transformer architectures? When would you use each?

What to learn: embeddings, positional information, Q/K/V projections, scaled dot-product attention, multi-head attention, MLP blocks, residual connections, normalization, causal masks, training objectives, and architecture/task fit.

Sources:

- [Jay Alammar — The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — the clearest visual introduction.
- [Hugging Face LLM Course — How Transformers work](https://huggingface.co/learn/llm-course/chapter1/4) — structured explanation tied to implementations.
- [Andrej Karpathy — Let’s build GPT from scratch (video)](https://www.youtube.com/watch?v=kCc8FmEb1nY) — code-level intuition for attention and decoder-only models.

### Bucket 10B — Inference internals: KV cache and Mixture of Experts

Questions:

- What is the KV cache? How does it help LLM inference?
- What is Mixture of Experts? How does it improve efficiency?

What to learn: prefill versus decode, reuse of attention keys/values, memory growth with sequence length and batch size, paged KV caches, expert routing, sparse activation, load balancing, communication overhead, and total-parameter versus active-parameter counts.

Sources:

- [Hugging Face — LLM inference optimization](https://huggingface.co/docs/transformers/v4.44.0/en/llm_optims) — KV-cache behavior and optimization.
- [vLLM — Anatomy of a high-throughput inference system](https://vllm-project.github.io/2025/09/05/anatomy-of-vllm.html) — scheduling, paged attention, and continuous batching.
- [Hugging Face — Mixture of Experts explained](https://huggingface.co/blog/moe) — accessible MoE overview.

### Bucket 10C — Tokenization

Questions:

- What are the differences among BPE, WordPiece, and character-level tokenization? What are the trade-offs?

What to learn: vocabulary size, sequence length, unknown tokens, subword reuse, byte fallback, multilingual/code behavior, training algorithms, and how tokenization affects cost and context use.

Sources:

- [Hugging Face LLM Course — Tokenizers](https://huggingface.co/learn/llm-course/chapter6/1) — BPE, WordPiece, Unigram, normalization, and pre-tokenization.
- [Hugging Face — Tokenizer summary](https://huggingface.co/docs/transformers/tokenizer_summary) — concise algorithm comparison.

---

## Fast preparation plan

If time is limited, use this sequence:

### Pass 1 — Mental models

Watch Karpathy's LLM introduction, read the AWS RAG overview, and read Anthropic's Building Effective Agents.

### Pass 2 — Reliability

Study OpenAI's eval guide, Microsoft's RAG evaluators, OWASP's LLM Top 10, and the W&B production-monitoring article.

### Pass 3 — System design

Practice one RAG design, one support-ticket agent, one model rollout, and one million-query-per-day cost estimate. For every answer, cover requirements, architecture, failure modes, metrics, security, cost, and rollout.

### Pass 4 — Role-dependent depth

Only then study fine-tuning, RLHF/DPO, attention, KV caches, MoE, quantization, and tokenization unless the job description explicitly emphasizes model training or inference systems.

## Interview answer template

For almost every applied question, answer in this order:

1. Clarify the user, risk level, scale, latency target, freshness, and available data.
2. State the simplest viable design and why it fits.
3. Walk through the data and control flow.
4. Name the main failure modes and mitigations.
5. Define offline, online, technical, and business metrics.
6. Explain security, privacy, and human-approval boundaries.
7. Describe rollout, observability, rollback, and cost trade-offs.

That structure turns a definition-level response into a strong AI-engineering system-design answer.
