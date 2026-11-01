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
