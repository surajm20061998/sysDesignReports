# OA scenario and AI coding drills

> **SUPERSEDED STAGE — October 28 update:** OA waived based on Suraj’s prior pass. Retain questions as practice; OA timing, deadline and daily schedule are historical. Follow the [November 12 live-interview plan](amazon-10587705-phone-study-plan.md).

Updated October 28, 2026. Companion to [the question bank](amazon-10587705-oa-question-bank.md). Every prompt here is an **original practice exercise**. Checkpoints are suggested answers under the stated assumptions, not Amazon scoring keys. Hide them during a mock.

## Distributed systems scenarios

Score each practice response 0–2 on requirement fit, correctness under failure, and explicit tradeoff (6 total). This is a learning rubric, not an assessment cutoff. P0: SD-01–16. P1: SD-17–24.

### SD-01 — Live audience counter
A broadcast attracts 2 million viewers. The displayed audience count may lag five seconds, but a single popular broadcast must not overload one database key. Pick between one synchronous counter, sharded counters with periodic aggregation, and calculating the count by scanning all sessions on every request.

**Checkpoint:** Shard increments and aggregate for display; define viewer/session expiry and duplicate handling. A single counter can become hot; scanning is expensive. An approximate display requirement differs from billing accuracy. Synthetic scenario inspired by S08's broad counter theme.

### SD-02 — Last item in inventory
Two customers buy the last unit concurrently. Both previously read stock=1. Is adding a strongly consistent read sufficient? Propose the write path.

**Checkpoint:** No: a read followed by a separate write still races. Use an atomic conditional decrement or transaction, with request idempotency. Decide reservation expiry and cancellation semantics. Strong reads help freshness, not atomicity of a later action.

### SD-03 — Payment timeout
A payment request times out after the server might have committed it. Compare blind retry, abandoning the order, and retrying with a stable request key.

**Checkpoint:** Persist an idempotency key and operation outcome atomically where possible; reuse it for the same intent and reject conflicting payloads. Reconcile uncertain outcomes. “Timeout” does not prove failure. [AWS idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

### SD-04 — Duplicate queue delivery
A worker sends a notification and crashes before acknowledging the queue message. How should a redelivery be handled?

**Checkpoint:** Record a durable operation identity and make the effect deduplicatable. A database flag written after an external send leaves a crash window; use a downstream idempotency capability or an explicit reconciliation design. Do not claim queue selection alone makes external effects exactly once. [SQS delivery semantics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html)

### SD-05 — Product page cache
Catalog reads tolerate 30 seconds of staleness. A promotion creates a surge on one item. Select a caching policy and explain what happens when that entry expires.

**Checkpoint:** Cache-aside with bounded TTL; coalesce concurrent refreshes and jitter expiration to avoid a stampede. Define invalidation on writes and fallback behavior. A cache must not become the authority for stock correctness.

### SD-06 — Read after profile update
A customer saves a new display name and immediately sees the old value from a replica. What are two remedies, and what do they cost?

**Checkpoint:** Read from an authoritative/strongly consistent path, or preserve session read-your-writes with a version/token strategy. Avoid promising strong reads on unsupported indexes. A DynamoDB GSI is eventually consistent. [DynamoDB consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)

### SD-07 — Retry storm
A dependency's error rate rises, and clients retry immediately three times at every service layer. What do you change first?

**Checkpoint:** Bound attempts and total elapsed time, apply backoff/jitter, retry only appropriate failures and safe operations, and prevent retry multiplication across layers. Admission control may be needed. More retries can worsen overload. [AWS retries and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)

### SD-08 — Worker backlog
Arrival rate is 1,200 jobs/s; 40 workers each complete 20 jobs/s. Estimate backlog growth and choose a signal for scaling.

**Checkpoint:** Capacity 800/s; backlog grows 400/s, or 24,000/min under these assumptions. Track oldest-job age and queue depth alongside throughput. At least 60 workers merely match average arrival, with no safety margin or backlog drainage. Scaling is constrained by downstream capacity.

### SD-09 — Tenant rate limits
Ten application instances serve a customer with a global 100 requests/s limit. Would a local 100/s limiter on each instance enforce it?

**Checkpoint:** No, the aggregate could approach 1,000/s. Use shared atomic state or partitioned quotas with a defined error bound. Token bucket allows bounded bursts; strict fixed windows have boundary effects. Define fail-open versus fail-closed based on product requirements.

### SD-10 — Partition key choice
Order records are mostly fetched by order ID; one enterprise customer creates half the traffic. Compare customer ID and high-cardinality order ID as primary partition keys.

**Checkpoint:** Start from access patterns and load distribution. Customer ID may create a hot partition; order ID spreads traffic but customer listing needs another index or bounded fan-out. Salting also imposes read complexity.

### SD-11 — Durable upload
Users upload 500 MB videos and edit small metadata. Choose storage and describe the failure between uploading bytes and saving metadata.

**Checkpoint:** Object storage for bytes, a database for metadata, explicit upload states and checksums, and cleanup for orphaned objects. Prefer direct signed upload when appropriate. Do not promise an atomic transaction across unrelated services; reconcile partial completion.

### SD-12 — AZ failure
The service must survive losing one availability zone. Why are three app replicas in the same zone insufficient?

**Checkpoint:** Spread app and data replicas across failure domains, provision failover capacity, and use health-aware routing. Test database quorum/failover behavior, not just the web tier. Replicas are also not a substitute for recoverable backups.

### SD-13 — Ordering shipments
Shipment events arrive out of order; ordering matters per shipment, not across all shipments. Pick partitioning and state-update rules.

**Checkpoint:** Partition by shipment identity; retain event sequence/version, reject stale state transitions, and deduplicate. Event time alone may tie or reflect skew. Global ordering reduces parallelism unnecessarily for this requirement.

### SD-14 — Commit plus publish
An order is committed in the database, but publishing its event fails. What avoids silently losing the event?

**Checkpoint:** Transactionally write order and outbox record together; relay asynchronously with retries and idempotent consumers. Account for relay duplicates and lag. A simple “save then publish” sequence has a failure gap.

### SD-15 — Search index lag
A product write succeeds, but search does not show it for ten seconds. Is this necessarily data loss? How should the product behave?

**Checkpoint:** Distinguish indexing lag from loss, measure freshness and failed indexing, and provide authoritative detail reads when required. Eventual search is acceptable only if the requirement permits it. Rebuild/replay capability helps recovery.

### SD-16 — Inference overload
Requests must finish within two seconds. The GPU worker queue is already five seconds deep. Choose between queueing indefinitely, rejecting excess traffic, and increasing batch size without a bound.

**Checkpoint:** Deadline-aware bounded admission, backpressure, and explicit overload responses; autoscaling helps future capacity but cannot erase current latency. Batch size trades throughput against latency. This is role-relevant practice inferred from the JD, not a reported OA question.

### SD-17 — Slowest dependency
An API makes three sequential calls that can each take 800 ms; its end-to-end budget is 1.5 seconds. What is wrong with giving each call a 1.5-second timeout?

**Checkpoint:** Propagate remaining deadline and allocate budgets including overhead; parallelize independent calls where semantics allow. Cancel unnecessary work. A per-hop timeout is not an end-to-end guarantee.

### SD-18 — Regional recovery
The business requires RPO ≤5 minutes and RTO ≤30 minutes. Explain each and propose a recovery validation.

**Checkpoint:** RPO bounds tolerable lost data; RTO bounds restoration time. Verify replication/backup lag and timed restoration/failover under realistic failure. A backup schedule alone proves neither recovery time nor restore success.

### SD-19 — Configuration rollout
A malformed config can break every host. Compare immediate global replacement with versioned staged rollout.

**Checkpoint:** Validate schema and semantics; use a canary, observable health gates, versioning, and rollback to last-known-good. Plan compatibility when mixed versions coexist. Fast distribution alone is not a safe rollout.

### SD-20 — Expiring leaderboard
A top-100 ranking refreshes each second. Is a relational scan on every page view a good default? What if exact rankings during ties matter?

**Checkpoint:** Maintain a suitable ordered/aggregated read model; define deterministic tie breaks and update semantics. Separate authoritative events from the serving projection. Account for hot leaders, replay and freshness.

### SD-21 — Database pagination
A feed inserts new records constantly. Users see repeated rows with offset pagination. Propose an alternative.

**Checkpoint:** Stable cursor/keyset pagination with a total order such as timestamp plus unique ID; index accordingly. Define snapshot expectations and updates/deletions. Cursor pagination does not automatically guarantee a fixed historical snapshot.

### SD-22 — Observability priorities
p50 latency is steady, but complaints and timeouts increase. Which metrics would you inspect before buying more compute?

**Checkpoint:** p95/p99, error/timeout rates, queue age, per-endpoint and per-tenant load, saturation and dependency traces. Compare deployment changes. Averages can hide a subset of severe failures; scaling does not fix every cause.

### SD-23 — Poison messages
One invalid job is retried forever and blocks useful work. Design retry and quarantine behavior.

**Checkpoint:** Distinguish transient/permanent failure, cap retries, move exhausted jobs to a dead-letter path, alert with actionable context, and support safe replay after repair. Do not silently drop data or retry all jobs forever.

### SD-24 — Network partition
Two regions cannot communicate. A global inventory invariant must never oversell. Can both sides freely accept all sales and guarantee that invariant?

**Checkpoint:** Not without preallocated disjoint inventory/rights or another constraint that preserves the invariant. Otherwise restrict writes on a side that cannot coordinate. Explain availability versus coordination; don't say all distributed systems always choose just two properties regardless of partitions.

## AI-assisted coding drills

All 12 are **synthetic practice specifications**. P0: AI-01–08; P1: AI-09–12. Use a small existing app, a clean branch, and seed defects before starting the clock. Each task should involve one bounded fix, not building the whole app in 20 minutes. S03/S07/S09 support repo debugging as a practice theme; they do not establish these exact prompts or framework availability.

### AI-01 — Created record disappears
**Task:** `POST /movies` returns 201 but a subsequent `GET /movies/{id}` returns 404. Inspect controller/service/repository boundaries and fix the persistence path while preserving response shape.
**Acceptance:** create then retrieve yields the same ID/title; two creates receive distinct IDs; invalid input is not stored; missing ID returns 404. Distinguish persistence defects from cache or route defects rather than assuming a cause.

### AI-02 — Wrong route and null result
**Task:** A detail endpoint returns 500 for absent records; the list route is accidentally captured as a dynamic ID. Repair routing and missing-resource handling.
**Acceptance:** list succeeds; valid ID returns record; absent ID returns 404; malformed ID follows the specified 400 contract; no null dereference. Preserve unrelated routes.

### AI-03 — Validation boundaries
**Task:** A signup endpoint accepts passwords outside its specified inclusive 8–64 character range and crashes on null input. Repair validation. For this exercise, length means Unicode code points, not UTF-8 bytes.
**Acceptance:** 7 and 65 rejected; 8 and 64 accepted; null/non-string rejected with 400; valid existing flow stays green. This is a validation exercise, not a recommended production password policy.

### AI-04 — Latest shipment status
**Task:** Implement a missing pure function combining shipment deadlines and timestamped events. Choose the greatest `(timestamp,event_id)` per shipment. Delivered by deadline is ON_TIME, delivered later is LATE; undelivered is PENDING until deadline and LATE afterward. `now` is supplied. Unknown shipment events are ignored.
**Acceptance:** out-of-order events, duplicate events, equal timestamps, no events, delivery exactly at deadline, empty input; output sorted by shipment ID. This is our fully specified simplified variant of S03's theme, not its original prompt.

### AI-05 — Idempotent create
**Task:** A retry with the same request key creates a duplicate order. Add sequential-request idempotency to an existing repository API: same key/payload returns original result; same key/different payload returns 409.
**Acceptance:** repeat identical request; conflicting reuse; independent keys; persistence across service-object reconstruction. Discuss what atomic database support would additionally be needed for concurrent calls; do not claim a local dictionary makes it distributed-safe.

### AI-06 — Rate limiter boundary
**Task:** Fix an existing single-process fixed-window limiter allowing 5 requests per client per 10 seconds. Time is injected and monotonically increasing; a new window starts at integer multiples of 10.
**Acceptance:** first 5 allowed, sixth denied; separate clients independent; t=9.999 vs t=10; denial does not consume next-window quota. Explain boundary bursts and the single-process limitation.

### AI-07 — Stable pagination
**Task:** Repair a list endpoint whose page slicing skips records. Contract: page is one-based; size is 1–100; records ordered by `(created_at,id)`; invalid inputs return 400.
**Acceptance:** pages 1/2 don't overlap for static data; partial final page; empty results; zero/negative page and oversized size rejected. Do not promise stable pagination under concurrent writes for this offset-based API.

### AI-08 — UTC deadline parsing
**Task:** A deadline comparison mixes naive and aware timestamps. Contract: accept RFC3339 timestamps with `Z` or an explicit offset; reject missing offsets; compare instants, not display strings.
**Acceptance:** equivalent instants with different offsets; exactly-at-deadline; malformed input; missing timezone; daylight-saving ambiguity avoided by supplied offsets. Keep comparison independent of machine timezone.

### AI-09 — Bounded retries
**Task:** Repair a client that retries all failures forever. Contract: at most 3 attempts total; retry timeouts and 503 only; stop on other statuses; an injected delay function avoids real sleeps in tests.
**Acceptance:** immediate success; transient success on attempt 3; persistent failure makes exactly 3 calls; 400 is not retried; verify the number of delays. State that real side-effecting calls also require safe retry semantics.

### AI-10 — Duplicate event processing
**Task:** Fix a single-process event consumer that applies an increment twice for the same event ID. Existing transactional repository method can atomically record the ID and update the balance; use it.
**Acceptance:** repeated ID applied once; distinct IDs applied independently; repository failure leaves both marker and balance unchanged; replay after reloading repository state is deduplicated. Test failure before commit.

### AI-11 — TTL cache expiry
**Task:** Correct a cache that serves entries at their expiry instant and treats cached zero as a miss. Clock is injected; an entry expires when `now >= expires_at`.
**Acceptance:** before/at/after expiry; values 0, false and empty string; TTL=0; overwrite resets expiry. Do not introduce unrequested cross-process caching behavior.

### AI-12 — N+1 database calls
**Task:** A summary endpoint calls `get_user` once per order. Existing `get_users(ids)` returns a map; refactor to one batch request without changing order or response fields. Missing users display “Unknown.”
**Acceptance:** one batch call for nonempty orders; no call for empty input; repeated user IDs fetched once; missing user handled; output order preserved. Verify correctness before claiming a performance improvement.

For each drill record: baseline failure, files inspected, AI suggestion accepted/rejected and why, tests run, remaining uncertainty. Passing self-written cases is useful evidence, not proof of passing unknown assessment tests.
