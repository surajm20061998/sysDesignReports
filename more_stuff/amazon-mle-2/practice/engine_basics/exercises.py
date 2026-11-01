"""Small inference-engine practice tasks. Implement one function at a time.

Use ordinary Python only. Read README.md for the contracts and worked traces.
Do not open reference.py until after your own attempt.
"""


def first_token_time(events):
    """Return the timestamp of the first event with count > 0, or None.

    events is a list of (timestamp, token_count) pairs in time order.
    """
    raise NotImplementedError("Start here: inspect one event at a time")


def streaming_summary(start_time, events):
    """Return ttft, e2e, event_gaps, and total_tokens as a dictionary.

    Event times are nondecreasing and >= start_time; counts are nonnegative.
    TTFT/E2E end at the first/last positive-token event. No tokens means
    ttft=None, e2e=None, event_gaps=[], total_tokens=0.
    """
    raise NotImplementedError("Build this after first_token_time")


class QueueWait:
    """Track completed waiting intervals with explicit start/admit operations.

    Expose total (initially 0). Reject start while waiting, admit while not
    waiting, or a timestamp earlier than the last accepted operation.
    Rejected operations must not change state. reset() clears everything.
    """

    def __init__(self):
        self.total = 0.0
        # Add the state you need here.

    def start(self, timestamp):
        raise NotImplementedError("Open a wait interval")

    def admit(self, timestamp):
        raise NotImplementedError("Close and accumulate a wait interval")

    def reset(self):
        raise NotImplementedError("Reset accumulated time and lifecycle state")


def choose_batch(decode_ids, prefills, budget):
    """Return (allocations, remaining_prefills) without changing inputs.

    decode_ids: unique request IDs, each needing one token this iteration.
    prefills: [(id, positive_remaining_token_count), ...], in FCFS order.
    IDs are unique across both collections. budget is a nonnegative integer.
    Reject budget < len(decode_ids) with ValueError.
    allocations is [(id, token_count), ...], decode first, then FCFS prefill.
    remaining_prefills includes unfinished prompts only, in original order.
    """
    raise NotImplementedError("Manually allocate the 12-token example first")
