# Technical Deep Dive — Final 90-Minute Preparation

## Round structure

The 45-minute interview has three goals:

1. **Take-home:** Can you explain and defend a customer-facing system you recently designed?
2. **Past project:** Can you go deeply enough to demonstrate real technical understanding, judgment, and learning?
3. **About you:** Is there a coherent connection between your background, interests, and approach to building systems?

Your objective is not to recite every implementation detail. For each topic, consistently communicate:

> **Problem → constraints → design → evidence → trade-off → limitation → lesson**

## Use the next 90 minutes

### Minutes 0–15: rehearse the two opening pitches

- Take-home: 90 seconds.
- FlashAttention2: 90 seconds.
- Record yourself once if possible.

### Minutes 15–35: take-home defense

- Architecture and request path.
- Routing decision.
- Retrieval stack.
- Evaluation corrections.
- Production/private deployment.

### Minutes 35–60: FlashAttention2 defense

- Derive online softmax on paper.
- Prefill versus decode.
- Correctness strategy.
- Results and limitations.
- Two debugging stories.

### Minutes 60–72: personal story

- Two-minute background.
- Why this role.
- How you build systems.
- How you use AI tools.

### Minutes 72–82: rapid-fire practice

Answer the questions at the end aloud, in 30–60 seconds each.

### Minutes 82–90: stop

Hydrate, close unnecessary applications, and reset. Do not learn new topics in the final eight minutes.

---

# Part 1 — Take-Home Assignment

## 90-second pitch

> “The customer wanted a local research assistant over two complementary sources: a SQLite database containing exact structured financials and six 10-K filings containing narrative explanations and lower-level disclosures. I built a FastAPI application around a bounded tool-calling agent. It can execute read-only SQL, search the filings, or read verbatim page ranges, and every response includes an inspectable evidence trail.
>
> “Offline, I extracted and section-tagged the filings into 438 chunks and created a 438-by-4096 embedding matrix of roughly 7.2 MB. Because the corpus is small, I kept the index in process. Retrieval combines BM25 and dense similarity with reciprocal rank fusion, takes 25 candidates, and reranks them to eight.
>
> “The central decision was letting the agent choose and sequence tools rather than using a one-shot classifier. Mixed questions often require an exact SQL calculation followed by a filing search based on that result. The trade-off is cost and latency: recorded questions took roughly 13 to 21 seconds and could consume about 23K tokens.
>
> “The system passed all 10 public questions and my 14-question stress suite, with required tool modalities covered. I treat those as encouraging regression results, not a precise generalization estimate: the samples are small and I authored the second set. The largest remaining gaps are claim-level grounding, evaluator calibration, retrieval ablations, context cost, and production controls.”

## Architecture mental map

```text
Offline path
PDFs → page extraction → 10-K item detection → overlapping chunks
     → embeddings → local NumPy index + BM25 index

Online path
Question → FastAPI → bounded agent loop
                    ├─ query_database
                    ├─ search_filings
                    └─ read_pages
              → evidence collection → final answer → API/UI

Evaluation path
Question set → real agent → answer + tool evidence
             → typed/deterministic grader or LLM judge
             → routing, latency, and token reports
```

## Why an agent rather than an upfront router?

### Chosen design

The model decides which tool to call and can revisit routing after seeing intermediate results.

### Reason

A question can be quantitatively phrased but require a filing because the number is below the database’s aggregation level. Mixed questions also require interleaving:

```text
SQL calculation → identify winning company/change
                → search that company’s filing for explanation
```

### Trade-off

- Better flexibility on multi-step and mixed-modality questions.
- More model round trips, context growth, latency, and cost.
- Prompt routing rules guide behavior but do not guarantee compliance.

### Honest runtime limitation

The deterministic guardrail only retries when a numeric-looking answer has no SQL or PDF evidence at all. It does not enforce that every claim or sub-question has appropriate evidence.

## Retrieval talking points

### BM25

Strong for exact labels, tickers, rare terminology, and table headings.

### Dense retrieval

Strong for paraphrases and semantically related wording without lexical overlap.

### RRF

BM25 and cosine scores are not calibrated to the same scale. Reciprocal rank fusion combines rank positions rather than raw scores, avoiding an unjustified blend weight.

### Reranker

A cross-encoder sees query and candidate together and can improve final ordering, but the project did not run a proper reranker ablation. Do not claim that the reranker caused the observed accuracy.

### Proper ablation

Compare:

1. BM25 only.
2. Dense only.
3. BM25 + dense through RRF.
4. RRF followed by reranking.
5. Optionally each with and without metadata filters.

Measure Recall@8, MRR/nDCG@8, end-to-end answer quality, retrieval latency, total latency, and API cost on a labeled evidence set.

## Evaluation talking points

### What the results prove

- Every probed behavior has a passing example.
- The system selected all required modalities on the recorded questions.
- The stress suite caught real issues, including the Alphabet hedging mistake.
- The end-to-end pipeline worked on the tested corpus.

### What the results do not prove

- A statistically precise production accuracy rate.
- No overfitting.
- Claim-level grounding.
- That the reranker improves retrieval.
- Robustness to a broad distribution of unseen financial questions.

### Submitted-evaluator weaknesses

1. The numeric matcher scale-expands percentages and can confuse `4.2%` with `4.2 billion`.
2. The LLM judge receives the question, gold answer, and candidate answer, but not the SQL rows or filing passages. It cannot genuinely verify grounding.
3. The 14-question suite was authored after development and is a stress/regression set, not a blind benchmark.

### How to improve it

- Extract typed quantities: money, percent, ratio, year.
- Require unit compatibility before numeric comparison.
- Pass actual evidence to the judge.
- Ask for unsupported-claim output, not only booleans.
- Add answer-mutation tests and wrong-gold negative controls.
- Build a larger human-labeled evidence and answer set.
- Freeze evaluation questions before further prompt tuning.

## Strong debugging stories

### Missing Item 7 / MD&A

- Symptom: ingestion appeared to work, but Item 7 was absent.
- Cause: curly apostrophes and headers whose title appeared on the next line.
- Detection: instrumented and inspected detected section distributions.
- Fix: alphanumeric normalization and newline-tolerant header matching.
- Lesson: silent ingestion failures can produce plausible retrieval over the wrong corpus; instrument data pipelines.

### Alphabet hedging reconciliation

- Symptom: the agent counted a hedging row as an operating segment even while retrieving text saying it was unallocated.
- Fix: clarified the semantic role of the hedging line and regression-tested the related question.
- Lesson: correct retrieval does not guarantee correct reasoning.

### Gold-answer error

- A judge failure revealed that the system included a valid fourth revenue component omitted from the hand-written gold.
- Lesson: inspect every evaluation failure; ground truth can be wrong.

## Production/private-deployment answer

The local database, PDF extraction, BM25, and NumPy index can remain unchanged. The external chat, embedding, and reranking services move behind private endpoints.

Production needs:

- Authenticated API and tenant authorization.
- Private networking and encrypted traffic.
- GPU-backed serving replicas for chat, embedding, and reranking models.
- Admission control, bounded queues, and timeouts.
- Health checks, restart/failover, and capacity monitoring.
- Versioned model deployments, canaries, evaluation gates, and rollback.
- Metrics: queue time, TTFT, token latency, tokens/second, errors, GPU memory/utilization, retrieval latency, and model-version quality.

## Take-home facts to recall

- Six filings: AAPL, MSFT, GOOGL; FY2024–FY2025.
- Database coverage: FY2023–FY2025.
- 438 chunks; 4,096-dimensional embeddings; approximately 7.2 MB.
- BM25 + dense → RRF top 25 → reranker top 8.
- Maximum 12 tool-loop iterations.
- SQLite `mode=ro`; 200-row cap.
- Page reads capped at eight pages.
- Dev: 10/10, 20.8-second mean, 225,679 total tokens.
- Stress set: 14/14, 13.1-second mean, 109,886 total tokens.
- Numeric guardrail fired zero times.
- Reranker contribution was not ablated.

## Avoid saying

- “The stress set proves the system did not overfit.”
- “The model has to follow the routing prompt.”
- “The LLM judge inspected the database and documents.”
- “The evidence trail proves every claim is grounded.”
- “The reranker improved accuracy.”

---

# Part 2 — FlashAttention2 Project

## Honest 90-second pitch

> “The project started from an RL systems problem: policy-model generation was slowing rollout collection, which made me want to understand where LLM inference time and memory actually go. I built an experimental Triton attention library covering FlashAttention-2 prefill and backward, Flash-Decoding with GQA/MQA, StreamingLLM-style bounded caches, and KIVI-style quantized KV caches.
>
> “The unifying technical idea is the online-softmax state `(m, l, acc)`. FlashAttention tiles that recurrence across KV blocks, Flash-Decoding partitions it across KV splits, streaming attention runs it over a retained token set, and quantized decode merges quantized and full-precision regions through the same recurrence.
>
> “The strongest result was the prefill kernel: 433 BF16 TFLOP/s on H100 and competitive performance against SDPA at medium and long sequence lengths. Split-KV also produced up to 13.6× speedup over my naive single-program decode.
>
> “The most important negative result is that my custom decode still lost to SDPA in 70 of 72 configurations. Nsight showed why: high register pressure limited occupancy, so the kernel could not hide HBM latency. That result changed the project from ‘I implemented the papers’ into ‘I can explain the performance boundary and what would need to change.’ The project is a correctness-first experimental prototype, not a production serving engine.”

## AI-assistance and ownership

Be completely honest. Use only claims that reflect what you personally did.

> “I used AI heavily for implementation, so I do not claim that I manually authored every Triton line. My contribution was selecting the problem, studying the papers, directing the architecture and experiments, validating generated implementations, interpreting benchmark and profiler results, and deciding which claims the evidence supported. The standard I hold is that I should be able to derive the central algorithms, explain the design decisions, identify limitations, and reproduce or challenge the measurements.”

If some part of that is not personally true, remove it. Never turn heavy AI assistance into a false hand-authorship claim.

## Online-softmax derivation

For a query row, attention is:

```text
O = Σ exp(s_j) V_j / Σ exp(s_j)
```

Stable softmax subtracts the maximum. After processing earlier blocks, retain:

- `m`: maximum score seen.
- `l = Σ exp(s_j - m)`: running normalizer.
- `acc = Σ exp(s_j - m) V_j`: running weighted-value sum.

For a new score block `s` and values `V`:

```text
m_new = max(m, max(s))
alpha = exp(m - m_new)
p     = exp(s - m_new)
l_new   = alpha * l   + sum(p)
acc_new = alpha * acc + p @ V
O = acc_new / l_new
```

Why rescale the old state:

```text
exp(old_score - m) * exp(m - m_new)
= exp(old_score - m_new)
```

The old and new terms must use the same reference maximum before they can be added. This preserves exact softmax algebra without materializing the full score matrix.

### Split-LSE merge

For split `i`, retain normalized partial output `O_i` and:

```text
LSE_i = log Σ(j in split i) exp(s_j)
```

Then:

```text
L* = logsumexp(LSE_1, ..., LSE_n)
O  = Σ_i exp(LSE_i - L*) O_i
```

This is why the result should be invariant to the number of KV splits, up to floating-point ordering effects.

## Prefill versus decode

### Prefill

- Many query tokens attend to many key tokens.
- Work resembles large matrix multiplications.
- High arithmetic intensity and tensor-core utilization.
- Usually compute-bound at sufficiently large sequence lengths.
- FlashAttention saves memory traffic by never materializing the `N × N` attention matrix.

### Decode

- One new query token attends over the entire existing KV cache.
- Every step reads large K/V tensors for relatively little computation.
- Low arithmetic intensity; memory-bandwidth and latency bound.
- At low batch, there may be too few programs to fill all SMs.
- Split-KV creates parallel work across the context; continuous batching creates work across requests.

## Flash-Decoding and GQA

### Split-KV

- Partition the KV sequence into independent splits.
- Each split computes a partial output and LSE.
- A reduction kernel merges them with the stable split-LSE identity.
- Benefit: more programs and better GPU occupancy at long contexts and low batch.
- Cost: temporary partial buffers and reduction overhead; oversplitting short contexts hurts.

### GQA tensor-core path

Multiple query heads share one KV head. Stack the sharing query heads into the matrix `M` dimension so QK and PV become tensor-core-compatible matrix multiplies. The KV tile is loaded once for several query heads.

## Correctness strategy

1. **Mathematical oracle:** explicit high-precision attention with exact mask, cache, and GQA semantics.
2. **Framework oracle:** PyTorch scaled-dot-product attention.
3. **Metamorphic properties:** partition invariance, split-count invariance, GQA equals repeated KV, ring wraparound equals logical gather, pack/unpack bit exactness, and fused decode equals dequantize-then-attend.
4. **Integration gate:** token-identical greedy generation on the constrained Hugging Face path.

Tests passing are not the complete answer; explain why the oracles are independent and which bug class each catches.

## Performance results — state them precisely

### Strong results

- FA2 prefill: peak 433 BF16 TFLOP/s on H100.
- Competitive with SDPA mainly at medium and long sequence lengths.
- Split-KV: up to 13.6× versus the project’s single-program decode at long context.
- Tensor-core GQA decode: 2/72 tested configurations beat SDPA, peak 1.29×.
- INT4 KV: approximately 3.2× effective compression and +0.33% perplexity.
- INT2 KV: approximately 5.2× effective compression but around +19.6% perplexity.

### Important negative results

- Custom decode lost to SDPA in 70/72 tested configurations.
- Short prefill is launch-bound and should dispatch to SDPA.
- Streaming quality numbers are provisional because the evaluation path has an unresolved RoPE/position seam.
- The implementation does not prove that the original RL pipeline became faster end to end.

## Nsight explanation

- Decode’s approximately 1.5% L2 hit rate is expected: each KV element is generally read once for a token, so there is little temporal reuse.
- The problem is insufficient latency hiding.
- High register counts limited occupancy to roughly 12–20% across the inspected kernels.
- Low occupancy means too few resident warps to hide HBM latency.
- The next optimization is reducing register pressure, improving schedules/data movement, and adding more serving-level parallelism—not trying to force cache reuse that does not exist.

## Best debugging stories

### Wrong profiler target

- A stale kernel-name filter captured the small reduction kernel rather than the compute kernel.
- The resulting metrics were precise but described the wrong work.
- The mismatch between expected mechanism and reported numbers prompted a recheck.
- Lesson: a profiler aimed at the wrong kernel is worse than no profiler; verify kernel identity and correlate with the execution trace.

### Oversplitting short contexts

- The initial policy created too many splits to fill GPU waves.
- At short context, reduction overhead exceeded useful work and made auto-split 2–3× slower.
- The policy was changed to require meaningful work per split, including a 4,096-token floor and a roughly four-wave target.
- Lesson: parallelism policies require minimum-work floors.

### Int32 pointer overflow

- Very large tensors exceeded 32-bit pointer-offset arithmetic.
- Result: illegal memory access/corruption at long contexts.
- Fix: cast program identifiers and pointer arithmetic to int64.
- Lesson: shape tests must cover index-space boundaries, not only tile boundaries.

## Biggest limitations

- Contiguous KV cache; no block-table/PagedAttention layout.
- No production continuous batching.
- `q_len > 1` speculative decoding unsupported.
- Device synchronization from `lengths.max().item()` in decode.
- KIVI path lacks split-KV.
- Streaming host-side gather and RoPE overhead.
- Streaming evaluation validity needs a position-parity fix.
- No CUDA graphs or persistent decode kernel.
- Hopper hardware is not fully exploited through TMA/WGMMA/clusters.

## What you learned

> “The papers explain the recurrence, but the engineering lives in the contracts and edge cases: fully masked rows, natural versus base-2 LSE, causal alignment, empty split merging, pointer width, and whether profiler data describes the correct kernel. I also learned to separate mechanism validation from baseline competitiveness. Split-KV can work exactly as intended and still lose to a production kernel because occupancy and serving-level execution dominate.”

---

# Part 3 — About You

## Two-minute background

> “My background started in production distributed systems. At Inture, I worked on Spring Boot services for supply-chain analytics, scaling through roughly five-times traffic growth and reducing API p99 latency through SQL and connection-pool profiling. At Oracle, I worked on fault-tolerant backup and recovery infrastructure at petabyte scale under strict SLAs, and improved throughput through CPU/IO profiling and resource-aware parallel scheduling.
>
> “During my master’s at NYU, I moved deeper into ML systems and research. My projects now span three layers: understanding model behavior through interpretability and safety research, understanding how training changes reasoning through GRPO instrumentation, and understanding inference performance through attention kernels. The Fireworks take-home added the customer-facing layer: turning model and retrieval capabilities into an application with clear evidence, evaluation, and trade-offs.
>
> “The common theme is that I like systems where correctness and performance have to be measured, not assumed. I’m most interested in roles that connect models, inference infrastructure, evaluation, and real customer workloads.”

## One-sentence career narrative

> “I began by building reliable distributed infrastructure, then moved into ML to apply the same systems discipline to how models are trained, understood, served, and evaluated.”

## Why this kind of role?

- It combines customer problem decomposition with hands-on model/application work.
- It sits at the boundary between model behavior and production inference.
- It rewards measurement, debugging, and explicit trade-offs.
- It connects your distributed-systems experience with recent ML systems work.

Do not claim knowledge of a particular internal Fireworks architecture unless the interviewer provides it.

## How you build systems

Use this five-part answer:

1. Clarify the user-visible outcome and failure modes.
2. Build the simplest end-to-end baseline.
3. Instrument early so silent failures become visible.
4. Add complexity only when evaluation identifies a concrete gap.
5. State limitations and negative results as part of the design, not as footnotes.

Examples:

- Take-home: ingestion section instrumentation exposed missing MD&A.
- Take-home: the stress suite exposed correct retrieval with wrong reasoning.
- FlashAttention2: suspicious profiler and split-policy results triggered deeper investigation.
- Oracle: profiling identified CPU/IO and scheduling bottlenecks.

## How you use AI tools

> “I use AI heavily for repository navigation, scaffolding, implementation drafts, and test generation. I try to keep problem framing, architecture, acceptance criteria, experiment design, and final verification explicitly mine. A generated patch is not evidence until I can explain the behavior, run a test that could have caught the original defect, and identify compatibility or performance limitations. One lesson from practice is that I need to make that ownership visible earlier, rather than delegating investigation through handoff in one prompt.”

For FlashAttention2 specifically, do not imply manual authorship of code that was AI-generated.

## Questions to ask the interviewer

Choose one or two:

- “For Applied MLEs here, where is the boundary between customer application architecture and inference-platform work?”
- “What distinguishes someone who is effective in the first six months on this team?”
- “How does the team evaluate whether an application-level optimization should become a platform capability?”
- “When customer workloads expose a serving limitation, how do Applied MLEs collaborate with inference and research teams?”

---

# Rapid-Fire Questions

Answer each aloud in 30–60 seconds.

## Take-home

1. Why not use a deterministic router?
2. Why not use a vector database?
3. Why use RRF rather than weighted score fusion?
4. What proves the reranker helps?
5. What does 14/14 legitimately establish?
6. Can your judge actually verify grounding?
7. What happens when a mixed question stops after SQL?
8. How would this scale to one million chunks?
9. What breaks with confidential customer documents?
10. What would you improve first: quality, latency, or scale, and why?

## FlashAttention2

1. Derive online softmax.
2. Why must the old state be rescaled?
3. Why is prefill compute-bound and decode memory-bound?
4. What does split-KV buy, and when does it hurt?
5. How are split outputs merged?
6. Why does GQA enable a tensor-core path?
7. Why is low decode L2 hit expected?
8. Why did your kernel lose to SDPA?
9. How do you know the kernel is correct?
10. What is the weakest claim in the project?
11. What did AI generate, and what did you personally own?
12. What would you redesign if starting again?

## About you

1. Walk me through your background.
2. Why move from distributed systems to ML?
3. Why this role?
4. What project are you most proud of and why?
5. Tell me about a result that contradicted your expectations.
6. How do you decide when a prototype is good enough?
7. How do you use AI without losing ownership?

---

# Final Interview Rules

1. Lead with the answer, then justify it.
2. Separate measured facts from hypotheses.
3. Scope every performance claim to hardware, shape, and baseline.
4. A prompt instruction is not a deterministic guarantee.
5. A passing benchmark is not proof of generalization.
6. State negative results before the interviewer discovers them.
7. If you do not know, name what you know, the missing information, and the next experiment.
8. Never overstate personal authorship of AI-generated work.
9. Keep answers to roughly 60–90 seconds unless invited deeper.
10. Use the pattern: **decision, reason, rejected alternative, cost, evidence**.

