"""Reference solutions: inspect only after trying exercises.py."""


def first_token_time(events):
    for timestamp, count in events:
        if count > 0:
            return timestamp
    return None


def streaming_summary(start_time, events):
    first = None
    last = None
    gaps = []
    total = 0
    for timestamp, count in events:
        if count == 0:
            continue
        if first is None:
            first = timestamp
        if last is not None:
            gaps.append(timestamp - last)
        last = timestamp
        total += count
    return {
        "ttft": None if first is None else first - start_time,
        "e2e": None if last is None else last - start_time,
        "event_gaps": gaps,
        "total_tokens": total,
    }


class QueueWait:
    def __init__(self):
        self.reset()

    def start(self, timestamp):
        if self._opened_at is not None:
            raise ValueError("already waiting")
        if self._last_event is not None and timestamp < self._last_event:
            raise ValueError("time moved backward")
        self._opened_at = timestamp
        self._last_event = timestamp

    def admit(self, timestamp):
        if self._opened_at is None:
            raise ValueError("not waiting")
        if timestamp < self._last_event:
            raise ValueError("time moved backward")
        self.total += timestamp - self._opened_at
        self._opened_at = None
        self._last_event = timestamp

    def reset(self):
        self.total = 0.0
        self._opened_at = None
        self._last_event = None


def choose_batch(decode_ids, prefills, budget):
    if budget < len(decode_ids):
        raise ValueError("budget cannot cover active decodes")
    allocations = [(request_id, 1) for request_id in decode_ids]
    available = budget - len(decode_ids)
    remaining = []
    for request_id, tokens in prefills:
        scheduled = min(tokens, available)
        if scheduled > 0:
            allocations.append((request_id, scheduled))
        available -= scheduled
        if tokens > scheduled:
            remaining.append((request_id, tokens - scheduled))
    return allocations, remaining
