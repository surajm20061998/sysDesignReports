# Technical Deep-Dive Mock 1 — Part 1 Report

**Interview format:** Fireworks AI Technical Deep Dive (45 minutes)  
**Coverage completed:** Take-home assignment and opening of FlashAttention2 discussion  
**Status:** Paused before the online-softmax derivation; continue from the resume point at the end of this report

## Executive assessment

The take-home portion demonstrated a solid understanding of the product problem, the high-level architecture, the reason for agent-directed tool routing, and the motivation for hybrid retrieval. The strongest moments came when the discussion became concrete: the redesigned typed-quantity evaluator, evidence-aware judging, mutation tests, Recall@8, and the retrieval ablation ladder were all strong interview answers.

The largest risk was implementation fidelity. Several initial claims contradicted the submitted code: the held-out set was described as proving the system was not overfit; the numeric evaluator was described as distinguishing percentages from currencies; the LLM judge was described as having database and document access; and prompt routing rules were described as runtime guarantees. After being shown the relevant behavior, the answers improved substantially, but a real interviewer may treat these mismatches as evidence that the candidate does not fully own or remember the implementation.

The second major risk emerged at the start of the FlashAttention2 discussion. The answer that most code was AI-generated was appropriately honest, but it creates a high bar for demonstrating personal technical ownership. The project can still be presented strongly, but ownership must be framed around problem selection, paper comprehension, architecture, experiment design, validation, debugging, performance interpretation, and the ability to derive the algorithms—not around personally typing every line.

## Approximate scorecard so far

| Area | Current signal | Assessment |
|---|---:|---|
| Product and customer framing | 4/5 | Clear analyst pain point, local prototype, structured and unstructured sources, evidence visibility |
| High-level architecture | 3.5/5 | Correct end-to-end flow; a few claims about guardrails and evidence were stronger than the code supports |
| Design trade-offs | 3.5/5 | Strong defense of agent routing and local in-process retrieval; production answers became generic under pressure |
| Retrieval understanding | 4/5 by the end | Initial explanation was imprecise, but RRF, Recall@8, and the ablation ladder were explained well |
| Evaluation discipline | 3/5 | Strong redesign answer; original interpretation of 14/14 and recollection of evaluator behavior were inaccurate |
| Code-level ownership | 2.5/5 | Important submitted behaviors were initially remembered incorrectly |
| Handling correction | 4/5 | Accepted concrete evidence and produced substantially better designs rather than continuing to defend errors |
| Production thinking | 2.5/5 | Identified gateways, queues, scheduling, model stores, and rollback, but lacked prioritization and precise SLO metrics |
| Communication | 3.5/5 | Generally understandable and candid; answers should become more structured and less absolute |
| FlashAttention2 ownership | Not yet scored | Only the opening answer was completed |

These scores are diagnostic rather than final. The FlashAttention2 and personal-background portions remain incomplete.

## What went well

### 1. Customer-oriented framing

The opening correctly framed the take-home as reducing the burden on financial analysts who otherwise cross-reference structured financial data and narrative 10-K disclosures manually. Mentioning the inspectable evidence trail connected the technical design directly to analyst trust.

### 2. Clear architecture narrative

The response covered the important stages:

1. PDF ingestion and chunking.
2. A small local index: 438 chunks with 4,096-dimensional embeddings and approximately 7–8 MB of embedding data.
3. A tool-calling agent with SQL, filing search, and page-reading tools.
4. Iterative tool calls followed by answer synthesis.
5. Evidence returned alongside the answer.

This was a good high-level flow for a two-minute introduction.

### 3. Correct identification of the central routing trade-off

The choice to let the agent select and sequence tools was defended using the right workload characteristic: mixed-modality questions may require SQL first, followed by filing retrieval based on the intermediate result. That is stronger than saying merely that an LLM router is more flexible.

### 4. Strong evaluator redesign after correction

The best answer in the mock was the three-part evaluator redesign:

- Typed quantities such as `MONEY`, `PERCENT`, `RATIO`, and `YEAR`.
- Unit-compatible matching and adversarial unit tests.
- Passing actual SQL rows and filing passages to the judge.
- Returning unsupported claims rather than only booleans.
- Mutation tests, wrong-gold negative controls, and fresh DB-derived questions.
- Treating the 14-question set as a frozen regression suite instead of proof of generalization.

This answer showed concrete engineering thinking and should be retained almost verbatim.

### 5. Strong retrieval ablation answer

The later Recall@8 answer was precise and correctly separated component evaluation from end-to-end evaluation. The proposed ladder was appropriate:

1. BM25 only.
2. Dense only.
3. BM25 + dense through RRF.
4. RRF followed by reranking.
5. Optionally repeat with and without metadata filters.

The explanation that end-to-end accuracy can hide a retrieval miss because the agent can reformulate or call another tool was particularly strong.

### 6. Candor under uncertainty

Saying “I am not sure” on semantic obligation verification was better than inventing a false guarantee. The next improvement is to bound the uncertainty and still propose an experiment or minimal design.

## Important factual corrections

### 1. The held-out set does not prove absence of overfitting

The 14 questions were written by the system builder after observing the development set and the application. They are useful as:

- Regression tests.
- Probes for underrepresented behaviors.
- Evidence that specific failure modes have passing examples.
- An overfitting tripwire.

They do **not** establish an unbiased generalization rate. A better phrasing is:

> “The 14-question set broadened behavioral coverage and caught real defects, but because I authored it after development, I treat it as a regression and stress suite—not as a statistically independent held-out benchmark. The customer’s hidden evaluation is the truly blind test.”

### 2. The numeric evaluator currently confuses quantity types

The submitted `fuzzy_numeric_match` scale-expands every extracted number, including percentages. Therefore, text containing `4.2%` can incorrectly match a gold value of `4.2e9`. The report and interview answer must describe this as a known evaluator bug, not as already solved behavior.

### 3. The LLM judge cannot independently verify grounding

The judge receives the question, gold answer, and candidate answer. It does not receive:

- The executed SQL and returned rows.
- Retrieved filing passages.
- Page text.
- The agent’s evidence trail.
- Tools that let it access the local database or filings.

Its `grounded` boolean therefore measures whether the response appears grounded relative to the gold, not whether each claim is supported by the actual retrieved evidence.

### 4. Prompt rules are policies, not enforcement guarantees

The prompt says quantitative-plus-explanatory questions require both SQL and filings. This encourages correct behavior but does not guarantee it.

The actual deterministic retry is narrower:

```text
answer contains a recognized numeric claim
AND
no SQL or PDF evidence was collected
```

After one SQL call, the guardrail is satisfied even if the narrative explanation is supplied from model memory. Routing coverage is checked during evaluation, not enforced in the live request path.

### 5. The guardrail does not deterministically return “insufficient data” after a failed retry

The code retries once with a required first tool call when a numeric answer has no evidence. The final response is still generated by the model. The application does not deterministically replace an unsupported response with “insufficient data.”

### 6. “Local” has an important qualification

The application, database, PDFs, BM25 index, and NumPy embedding index are local. Chat inference, query embeddings, and reranking use hosted APIs. For confidential documents, those services would need to move to a private deployment or customer-hosted inference environment.

## Where the answers became weak

### 1. Obligation-level enforcement remained underspecified

The proposed deterministic guardrail service was asked to understand whether an arbitrary natural-language answer was complete. Without a semantic model, that becomes a brittle rules or classification problem. With another LLM, reliability is improved only probabilistically.

A more defensible design boundary is:

1. Use a probabilistic planner to produce structured obligations, for example:

   ```json
   {
     "obligations": [
       {"id": "o1", "type": "numeric_comparison", "required_source": "sql"},
       {"id": "o2", "type": "management_explanation", "required_source": "filing"}
     ]
   }
   ```

2. Validate the schema and allowed source types deterministically.
3. Require tool evidence to be tagged to obligation IDs.
4. Prevent finalization when a required obligation has no evidence.
5. Use semantic entailment or an LLM only for the narrower question of whether the cited evidence supports the claim.
6. Bound retries and return a partial answer that explicitly names unsupported obligations.
7. Evaluate decomposition recall and claim-evidence precision on a human-labeled set.

This is not a mathematical guarantee that decomposition is complete, but it creates deterministic enforcement over a visible plan and makes failures measurable.

### 2. Private-deployment answer became too generic

The existing retrieval and ingestion system would not need to be rewritten. The required change is to move three external services behind private endpoints:

- Chat/tool-calling model.
- Embedding model.
- Reranking model.

Operational concerns should be prioritized instead of listing generic components:

1. **Capacity and admission:** GPU-backed replicas, bounded queues, concurrency limits, and overload behavior.
2. **Reliability:** health checks, replica restart, request timeouts, retry semantics, and failure isolation.
3. **Security:** private networking, service authentication, encryption, audit logs, and least-privilege data access.
4. **Model lifecycle:** versioned model artifacts, canaries, evaluation gates, and rollback.
5. **Observability:** queue time, time to first token, output-token latency, requests and tokens per second, error rate, GPU memory/utilization, retrieval latency, and model-version quality metrics.

The existing OpenAI-compatible boundary and environment-driven endpoint configuration make this migration easier than the initial answer suggested.

### 3. Several claims were too absolute

Avoid phrases such as:

- “It proves the model does not overfit.”
- “The LLM has to follow the routing rules.”
- “The evidence trail makes the tool precise.”
- “The solution is 100% accurate.”

Prefer scoped claims:

- “It passed every question in these two small suites.”
- “The routing prompt produced the expected modalities on all recorded questions.”
- “The evidence trail improves inspectability, although it does not yet prove claim-level entailment.”
- “The tested pipeline achieved 10/10 and 14/14; the sample is too small for a precise generalization estimate.”

## Improved two-minute take-home answer

> “The customer wanted a local research assistant over two complementary sources: a SQLite database containing exact structured financials and six 10-K filings containing narrative explanations and lower-level disclosures. I built a FastAPI application around a bounded tool-calling agent. The agent can execute read-only SQL, run hybrid filing retrieval, or read verbatim page ranges, and the application exposes the SQL and filing evidence used for each answer.
>
> “Offline, I extracted and section-tagged the filings into 438 chunks, embedded them, and kept the approximately 7.2 MB index in process because the corpus was too small to justify vector-database infrastructure. Retrieval combines BM25 and dense similarity through reciprocal rank fusion, then reranks 25 candidates down to eight.
>
> “The central decision was using the agent’s native tool selection rather than a one-shot front-door classifier. Some questions require an exact SQL calculation and then a filing search driven by that result, so routing has to occur during the reasoning process. The trade-off is latency and cost: the recorded questions take roughly 13–21 seconds and can consume around 23K tokens.
>
> “The public set passed 10/10 and my 14-question stress suite passed 14/14, with correct required-modality coverage. I would not present that as a statistically robust accuracy estimate because the sets are small and I authored the second one. Its real value is that it exposed a hedging-reconciliation reasoning error and even an error in my own gold answer. The largest remaining gaps are claim-level grounding, evaluator calibration, retrieval ablations, and production concerns such as authentication, timeouts, backpressure, and private deployment.”

## Numbers and implementation facts to recall accurately

- Six filings: AAPL, MSFT, and GOOGL for FY2024 and FY2025.
- Structured database coverage: FY2023–FY2025.
- 438 filing chunks.
- Embedding matrix: 438 × 4,096 float32, approximately 7.2 MB.
- Retrieval: BM25 + dense → RRF top 25 → reranker top 8.
- Agent limit: up to 12 tool iterations.
- SQL: SQLite `mode=ro`, SELECT/WITH checks, 200-row cap.
- Page reader: maximum eight pages per call.
- Dev results: 10/10, mean latency 20.8 seconds, 225,679 total tokens.
- Self-authored stress results: 14/14, mean latency 13.1 seconds, 109,886 total tokens.
- The numeric evidence guardrail fired zero times in recorded evaluations.
- The stress suite is not an independent blind test.
- Reranker contribution was not ablated.

## FlashAttention2 opening assessment

The motivation was compelling: policy-model rollout generation was slowing an RL workflow, leading to a deeper investigation of inference performance. The project’s unifying thesis—online softmax as the recurrence underlying prefill, split-KV decode, streaming attention, and quantized-cache merging—is strong.

The opening answer needs two corrections:

1. `433 TFLOP/s` is a prefill kernel throughput result, not proof that end-to-end RL rollouts became faster. The project does not demonstrate the original RL pipeline’s wall-clock improvement.
2. The most important disappointing result is known and should be stated immediately: the custom decode implementation loses to SDPA in 70 of 72 tested configurations. The strongest interpretation is not “decode was fast,” but “split-KV recovered parallelism by up to 13.6× over the project’s single-program implementation, while Nsight showed why the implementation still trailed the production baseline.”

### How to frame AI assistance and ownership

Do not say only:

> “I did not implement the code; AI generated it.”

That is honest but leaves the interviewer with no evidence of personal contribution. A stronger, still-honest framing is:

> “I used AI heavily for implementation, so I would not claim that I manually authored every kernel. My ownership was choosing the research question, reading the five papers, defining the common online-softmax abstraction, setting correctness gates, directing the implementation sequence, running GPU experiments, challenging suspicious results, and deciding which performance claims the evidence actually supported. The standard I set for myself is that I must be able to derive the algorithm, explain each design trade-off, inspect failures, and reproduce the evidence even when AI wrote the first draft.”

Only use this framing if it accurately reflects the work performed. The rest of the FlashAttention2 mock will test it directly.

## Mental map for the remaining FlashAttention2 discussion

```text
Original motivation
    ↓
Prefill versus decode bottleneck
    ↓
Online-softmax recurrence
    ↓
FA2 forward and backward
    ↓
Flash-Decoding and split-KV
    ↓
GQA tensor-core reuse
    ↓
Streaming and quantized cache variants
    ↓
Three-level correctness strategy
    ↓
Benchmarks and Nsight interpretation
    ↓
Honest limitations and serving-system extensions
```

The interviewer will care less about memorizing kernel syntax than about whether each step follows from the math and hardware bottleneck.

## Resume point for the next session

The mock paused on this exact question:

> “Without referring to the project documentation, derive the online-softmax recurrence. For one query row, suppose you have already processed some key/value blocks and retained running maximum `m`, normalization sum `l`, and weighted-value accumulator `acc`. You now receive a new block of attention scores `s` and values `V`. Show how `m`, `l`, and `acc` are updated, and explain why the old accumulator must be rescaled when the maximum changes.”

When the mock resumes, begin with the derivation rather than repeating the FlashAttention2 overview.

## Highest-priority preparation before resuming

1. Derive online softmax on paper from ordinary stable softmax.
2. Explain the difference between prefill and decode using arithmetic intensity and parallelism.
3. Prepare the honest decode result: 2/72 wins versus SDPA, why it lost, and what Nsight showed.
4. Be able to explain split-LSE merging and why split count should not change the mathematical result.
5. Prepare a precise account of personal ownership when AI generated much of the implementation.
6. Review three debugging stories: bottom-right causal alignment, int32 pointer overflow, and the profiler matching the wrong kernel.
7. Know the weakest claims: streaming evaluation validity and lack of production serving features such as paged KV and continuous batching.

