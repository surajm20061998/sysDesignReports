# November 12 phone interview — targeted AWS research and ML coding supplement

**Researched October 28, 2026.** Exact role: MLE II, AWS Inference Optimization, req 10587705. Research targets: SageMaker, Bedrock and HyperPod. These are relevant AWS product areas; neither the invitation nor public evidence establishes that the role belongs to all three teams. No verified question set for the exact role/interviewer was found.

## Evidence ranked by relevance

| Source | What is established | Limit and preparation consequence |
|---|---|---|
| User-supplied invitation | November 12, 2026, 2 PM Eastern (UTC−5), at least 60 minutes, interviewer Sathishkumar Sivashanmugam, phone/video call with live coding | Strongest scheduling evidence. Calls it a phone interview; user describes direct progression to interview loop. Do not resolve stage naming by guessing. |
| Recruiter guidance relayed by Suraj | Prepare both ML-based and LeetCode-style coding | Strongest content signal. No library availability, language, exact split, number of problems or AI assistance permission specified. |
| [SageMaker-adjacent candidate report](https://leetcode.com/discuss/post/6361672/Amazon-or-SDE-1-Fresher-or-India-or-Interview-Experience/) | SDE I fresher, India; Jan 16, 2025 DSA interview conducted by an SDE II from SageMaker: Minimum Path Sum and Generate Parentheses. Jan 23 machine-coding round and LPs. | Firsthand anonymous account, not MLE II. Interviewer's level is not candidate's level; interviewer team is not proof of hiring team. Add DP/backtracking coverage, not chess-game preparation. |
| [Amazon MLE II account](https://www.onsites.fyi/Amazon/Machine%20Learning%20Engineer/001DC8E474) | Onsite report labels MLE II and describes trees, monotonic stack, design, ML breadth and behavioral questions | Curated site, date/location/team unknown. Supports breadth only; do not label SageMaker/Bedrock/HyperPod. |
| [Amazon MLE phone/onsite account](https://prachub.com/interview-experiences/amazon-machine-learning-engineer-interview-experience-phone-screen-ml-deep-dive-then-a-five-round-onsite) | Described interview Dec 2025, published Aug 25, 2026. ML project/evaluation discussion and K-means in the screen; intervals/frequency coding later | Commercial curated/edited account, original author/team/level not established. Lower confidence. K-means merits practice; its claim that runnable code was unnecessary does NOT override your live-coding preparation. |
| [Official Amazon SDE II preparation](https://www.amazon.jobs/content/en/how-we-hire/sde-ii-interview-prep) | Technical problem solving and Leadership Principles both matter in adjacent engineering interviews | Official but SDE II, not this MLE packet. Do not restore OA requirements or assume its loop layout. |
| [Official Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles) | Behavioral framework | Practice actual decisions, evidence and lessons; no invented stories or metrics. |

### Search coverage and exclusions

Searched public LeetCode, Reddit, Glassdoor, 1point3acres-indexed material and niche candidate-report sites for SageMaker/MLE II, Amazon Bedrock and HyperPod interviews, including Chinese search terms. **No attributable, sufficiently specific Bedrock or HyperPod MLE II coding report was located.** Glassdoor/Reddit results often concerned engineers using AWS at other employers, general advice, or candidates asking what to expect. Some “Bedrock” results were unrelated companies, including robotics/property businesses. All excluded from AWS interview evidence. 1point3acres search-visible listings did not yield a usable complete exact-team prompt; hidden content was not reconstructed.

Do not treat a service tutorial, role advertisement or commercial “top questions” page as proof of an interview question. No frequencies or pass thresholds are supported. No interviewer background or question preferences inferred from their name.

## What to learn from the AWS products

These are **practice topics inferred from primary engineering documentation**, not reported interview questions. Spend bounded discussion time on mechanisms, not certification trivia or memorizing SDK parameters.

### AWS-01 — SageMaker deployment choice

A customer needs interactive low-latency inference, while another can wait for long jobs. Explain deployment choice, queueing, scaling, model startup and monitoring. Where do your container/runtime responsibilities end and managed infrastructure responsibilities begin?

**Checkpoint:** distinguish online latency requirements from asynchronous work; state workload and capacity assumptions before selecting an endpoint. Discuss cold starts and model resources, with no universal claim that every endpoint option supports every accelerator/model. [SageMaker deployment documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)

### AWS-02 — Bedrock latency and caching

A managed-model API workload repeatedly sends a large shared prefix. Design an experiment to reduce TTFT and cost without reducing answer quality. How do you distinguish prompt caching from caching complete responses?

**Checkpoint:** measure queue/network/prefill contributions and actual cache usage; keep reusable content stable. Cache eligibility/support differs by model/API, and a repeated request is not a guaranteed hit. Response caching also depends on full request semantics and freshness. [Bedrock overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html), [prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)

### AWS-03 — HyperPod resilience

A multi-GPU workload loses a worker. Explain detection, replacement, workload recovery, checkpoint integrity and what the application must still do. Why does a healthy cluster not guarantee a correct resumed job?

**Checkpoint:** HyperPod manages resilient ML clusters with Slurm or EKS options; application-level state and recovery semantics still need validation. Distinguish training checkpoints from transient inference KV state. [HyperPod documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)

### AWS-04 — HyperPod capacity and placement

An eight-GPU job shares a cluster with one-GPU jobs. Propose topology-aware gang admission, a starvation policy, quotas and failure recovery. How would online inference and offline work coexist?

**Checkpoint:** explicit resource ownership/leases, bounded queues, placement constraints and admission; evaluate utilization alongside fairness and latency. This scheduling problem is our synthesis, not a documented HyperPod interview question. Use the HyperPod overview for product context and the existing domain design bank for systems reasoning.

### AWS-05 — Performance release gate

You have a faster Triton kernel for some shapes. Design correctness and performance gates before serving it through a managed endpoint or cluster.

**Checkpoint:** representative shape/dtype/device matrix, numerical tolerances, pinned versions, compile versus warm time, end-to-end SLO and rollback. Explain precompiled variants/fallback and why a microbenchmark win is not enough. Original exercise grounded in the existing Triton/NVIDIA references in [the domain ledger](ml-inference-engineering-sources.md).

## Additional ML coding — bounded, runnable practice

These supplement the existing attention/kernel bank. They are **original specifications**; only the broad K-means theme has the lower-confidence reported support above. Default practice language: Python. NumPy is for rehearsal when available; be able to express loops and shapes without it. Actual libraries must be confirmed by the interviewer. Do not use sklearn estimators or built-in attention/loss functions to bypass the requested implementation.

### MC-01 — K-means, 45 minutes

Implement `kmeans(X, initial_centroids, max_iter, tol)` for finite X[N,D] and supplied centers[K,D], 1≤K≤N. Use squared Euclidean distance, assign ties to the smallest center index, update means, retain a previous center for an empty cluster, and stop on maximum center displacement ≤tol or iteration limit. Return centers and assignments recomputed against final centers.

Tests: two separated clusters, K=1, duplicate points, empty cluster, no movement, max_iter=1. Explain O(iterations*N*K*D) work and avoid needlessly materializing N*K*D intermediates. Reference: [scikit-learn's K-means explanation](https://scikit-learn.org/stable/modules/clustering.html#k-means); these interface/edge-case choices are ours.

### MC-02 — Logistic-regression step, 45 minutes

Given X[N,D], y[N] in {0,1}, w[D], b and learning rate, implement mean binary cross entropy from logits plus one batch-gradient step. Use a stable sigmoid and `max(z,0)-z*y+log1p(exp(-abs(z)))` for loss. No regularization in the base task.

Tests: zero weights, extreme positive/negative logits, N=1, finite-difference gradient on a tiny case, decreasing loss with a suitably small step. Follow-up: add L2 on w only, explicitly defining its coefficient convention.

### MC-03 — Linear-regression step, 35 minutes

Implement predictions, mean squared error and gradients for Xw+b; loss is mean((prediction-y)^2), without a 1/2 factor. Include shape validation.

Tests: exact fit, nonzero residual, N=1, finite differences; explain feature scaling and the learning-rate tradeoff. Follow-up: compare closed-form least squares without claiming explicit matrix inversion is required.

### MC-04 — Classification metrics, 30 minutes

Given binary labels and prediction scores, compute TP/FP/TN/FN, precision, recall and F1 at a supplied threshold; predict positive when score≥threshold. Define a zero denominator to return 0 for this exercise.

Tests: all negatives, no predicted positives, perfect predictions, threshold boundary and empty-input policy. Explain why accuracy can mislead with imbalance and why threshold selection must not use the held-out test set.

### MC-05 — Cosine top-k retrieval, 40 minutes

Given query[D], embeddings[N,D] and 1≤k≤N, return highest cosine scores and indices. Define zero-vector similarity as 0 and ties by ascending index.

Tests: identical/opposite vectors, zero vectors, ties and k=N. Compare sort versus bounded heap/selection and chunked computation when N is large. Do not accidentally rank by raw dot product when norms differ.

### MC-06 — Streaming latency metrics, 40 minutes

Input: request start time and time-ordered events `(timestamp, token_count)`, where token_count≥0. Return TTFT to the first positive-token event, E2E to the last positive-token event, gaps between positive-token events, and total token count. Tokenless trailers must not extend E2E. For no tokens, return None for TTFT/E2E and an empty gap list. Reject decreasing timestamps and timestamps before request start.

Tests: empty stream, tokenless first/trailing events, one positive event, multi-token chunks, equal timestamps. Explain why event gaps cannot reconstruct individual-token latency within a chunk. This is a synthetic task inspired by the candidate's vLLM measurement work, not a claim about an Amazon interview question.

## Practice mechanics

Each live solve: clarify contract → tiny example → approach/invariant and complexity → complete code → edge cases → follow-up. Use a plain local editor, speak aloud, and avoid AI during timed coding mocks. Ask which libraries are permitted rather than assuming NumPy/PyTorch. The invite's transcription feature is not permission to use an AI coding assistant.


## Research refresh — October 31, 2026

Searched recent-window and broader public LeetCode, Reddit, Glassdoor and 1point3acres-indexed results for Amazon MLE II, SageMaker, Bedrock and HyperPod. No new attributable exact-team/level coding report qualified for addition. Search recency filters also returned older posts; crawl dates were not treated as interview dates. Excluded an Aug 7 MLE-loop preparation request (https://www.reddit.com/r/amazonsdeprep/comments/1vhne6a/machine_learning_engineer_loop_prep/) because it asks what to expect rather than reports completed interviews, an older senior-level promotional account already encountered, unrelated employers using HyperPod, and broad commercial guides with no original prompt provenance. Reopened the existing curated Amazon MLE/K-means source; its team/level/date limitations remain.

November 12 live coding, ML implementations, DSA and truthful project/LP defense remain the priorities. Schedule and question IDs unchanged. Phone and question-bank trackers contain no recorded attempts as of this check; no independent mastery or readiness inferred from chat explanations. No private interview links opened.
