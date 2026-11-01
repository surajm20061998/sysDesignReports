# Inference engines, one small function at a time

This is a learning lab for ECODE-01–03 in the inference-engine bank. It requires Python 3 only. It models a few state transitions; it is not an implementation of vLLM or SGLang and does not benchmark performance.

Open `exercises.py`. Work on one function, predict the output manually, then run its checks. `reference.py` contains complete answers for review after an attempt. Reference tests passed when the lab was prepared; this does not record a candidate solve.

Run commands from this directory:

```bash
cd /Users/surajmishra/workspace/careerops/career-ops/interview-prep/amazon-mle-2/practice/engine_basics
python3 check.py first
```

The starter intentionally raises `NotImplementedError`. That means the exercise needs implementation. It is not a dependency or environment failure. Keep other stages untouched until the current stage is understood.

## Stage 1 — Find the first generated output

Each event is `(timestamp, token_count)`. For this exercise, timestamps are supplied, times are ordered, and counts are nonnegative. An event with count zero contains no generated tokens. It can represent metadata rather than useful model output.

Example:

```python
events = [(10, 0), (12, 1), (15, 3), (19, 0)]
```

Trace:

| Event | Contains tokens? | What to do |
|---|---|---|
| `(10, 0)` | No | Continue looking |
| `(12, 1)` | Yes | This is the first token-bearing event |
| `(15, 3)` | Yes | Later output; irrelevant to finding the first |
| `(19, 0)` | No | A later metadata event |

Implement `first_token_time(events)`, returning `12` here and `None` if no event contains tokens. Return the timestamp, not the tuple, index or elapsed duration. Try with an empty list and with a first timestamp of zero.

Build it with a loop and an `if` statement. No NumPy or list comprehension is required. First explain which values a loop iteration unpacks.

```bash
python3 check.py first
```

Interview follow-up after your attempt: why would taking the first network event produce the wrong TTFT for some streams?

## Stage 2 — Derive streaming measurements

Implement `streaming_summary(start_time, events)` with the same valid-input assumptions.

For start time `10` and the example above, return:

```python
{
    "ttft": 2,
    "e2e": 5,
    "event_gaps": [3],
    "total_tokens": 4,
}
```

The final event at 19 adds no tokens and must not extend the measured output endpoint. If no tokens arrive, both durations are `None`, gaps are empty and the token total is zero. A single output event has no gap. Two output events at the same instant produce a zero gap.

Decide which running state you need before coding. Write down the state after each event. A three-token chunk does not tell you when its three individual tokens were produced; call the measured differences **event gaps**.

```bash
python3 check.py streaming
```

## Stage 3 — Account for repeated waiting

Complete `QueueWait`. A request can wait, run, then wait again. `total` sums completed waits only; running time is excluded.

```text
start(1) → admit(4): completed wait = 3
running from 4 to 8: no waiting added
start(8) → admit(10): completed wait = 2
total = 5
```

`start` opens a wait and `admit` closes it. Repeated start while open, admit while closed and time moving backward raise `ValueError` without altering state. Equal timestamps are allowed. `reset()` clears the total, open interval and timestamp history.

```bash
python3 check.py queue
```

Before writing methods, draw the two states: **not waiting** and **waiting**. Mark legal transitions. This connects to retraction/queue-time reasoning in SGLang; it does not reproduce that project's exact class or metrics contract.

## Stage 4 — Allocate a token budget

Implement `choose_batch`. Each active decode gets one token; remaining budget goes to waiting prefill requests in order. A prompt may be partially processed. Inputs must remain unchanged. A budget below the active-decode count raises `ValueError`.

Example:

```text
budget = 12
active decodes = a,b,c,d → spend 4
waiting prompts = p needs 10, q needs 6
budget remaining = 8 → p receives 8
unfinished prompts = p needs 2, q needs 6
```

Return:

```python
(
    [("a", 1), ("b", 1), ("c", 1), ("d", 1), ("p", 8)],
    [("p", 2), ("q", 6)],
)
```

The prompt counts are positive; IDs are unique across active and waiting requests. Completed prompts disappear from the remaining list. Unused budget is permitted if there is no work. This toy scheduler has no KV-capacity constraint, preemption or speculation.

```bash
python3 check.py scheduler
python3 check.py all
```

## Reviewing your attempt

After each stage: state what was confusing, explain one edge case, and describe the state your function maintains. Then compare against the reference if needed:

```bash
python3 check.py all --reference
```

Passing the reference checks validates the teaching implementation, not your starter file. Passing public checks on your own implementation is a learning milestone, not proof of production correctness or an interview outcome. Record actual attempts only; do not mark a walkthrough as an independent solve.
