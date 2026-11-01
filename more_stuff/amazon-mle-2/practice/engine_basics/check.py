"""Run public exercise checks. Reference success does not imply user mastery."""
import argparse
import importlib
import unittest

parser = argparse.ArgumentParser()
parser.add_argument("stage", choices=["first", "streaming", "queue", "scheduler", "all"])
parser.add_argument("--reference", action="store_true", help="verify teaching reference instead")
args = parser.parse_args()
subject = importlib.import_module("reference" if args.reference else "exercises")


class FirstChecks(unittest.TestCase):
    def test_leading_metadata(self):
        self.assertEqual(subject.first_token_time([(10, 0), (12, 1), (15, 2)]), 12)

    def test_zero_timestamp(self):
        self.assertEqual(subject.first_token_time([(0, 2), (3, 1)]), 0)

    def test_no_output(self):
        self.assertIsNone(subject.first_token_time([]))
        self.assertIsNone(subject.first_token_time([(1, 0), (2, 0)]))


class StreamingChecks(unittest.TestCase):
    def test_trailer_and_chunk_semantics(self):
        result = subject.streaming_summary(10, [(10, 0), (12, 1), (15, 3), (19, 0)])
        self.assertEqual(result, {"ttft": 2, "e2e": 5, "event_gaps": [3], "total_tokens": 4})

    def test_single_event(self):
        self.assertEqual(subject.streaming_summary(0, [(2, 5)]),
                         {"ttft": 2, "e2e": 2, "event_gaps": [], "total_tokens": 5})

    def test_no_tokens(self):
        expected = {"ttft": None, "e2e": None, "event_gaps": [], "total_tokens": 0}
        self.assertEqual(subject.streaming_summary(0, []), expected)
        self.assertEqual(subject.streaming_summary(0, [(1, 0)]), expected)

    def test_equal_times(self):
        self.assertEqual(subject.streaming_summary(0, [(0, 1), (0, 1)])["event_gaps"], [0])


class QueueChecks(unittest.TestCase):
    def test_two_waits_running_time_excluded(self):
        q = subject.QueueWait()
        q.start(1)
        q.admit(4)
        q.start(8)
        q.admit(10)
        self.assertEqual(q.total, 5)

    def test_rejected_operations_preserve_state(self):
        q = subject.QueueWait()
        with self.assertRaises(ValueError):
            q.admit(0)
        q.start(1)
        with self.assertRaises(ValueError):
            q.start(3)
        with self.assertRaises(ValueError):
            q.admit(0)
        q.admit(4)
        self.assertEqual(q.total, 3)
        with self.assertRaises(ValueError):
            q.admit(4)
        with self.assertRaises(ValueError):
            q.start(2)
        q.start(5)
        q.admit(6)
        self.assertEqual(q.total, 4)

    def test_reset_and_zero_wait(self):
        q = subject.QueueWait()
        q.start(10)
        q.reset()
        self.assertEqual(q.total, 0)
        q.start(0)
        q.admit(0)
        self.assertEqual(q.total, 0)


class SchedulerChecks(unittest.TestCase):
    def test_twelve_token_trace(self):
        result = subject.choose_batch(["a", "b", "c", "d"], [("p", 10), ("q", 6)], 12)
        self.assertEqual(result, ([("a", 1), ("b", 1), ("c", 1), ("d", 1), ("p", 8)],
                                  [("p", 2), ("q", 6)]))

    def test_finish_then_partial(self):
        self.assertEqual(subject.choose_batch(["a"], [("p", 2), ("q", 5)], 5),
                         ([("a", 1), ("p", 2), ("q", 2)], [("q", 3)]))

    def test_capacity_and_no_mutation(self):
        ids, prompts = ["a"], [("p", 2)]
        self.assertEqual(subject.choose_batch(ids, prompts, 3), ([("a", 1), ("p", 2)], []))
        self.assertEqual(ids, ["a"])
        self.assertEqual(prompts, [("p", 2)])

    def test_zero_and_unused_budget(self):
        self.assertEqual(subject.choose_batch([], [("p", 2)], 0), ([], [("p", 2)]))
        self.assertEqual(subject.choose_batch([], [], 10), ([], []))

    def test_insufficient_decode_budget(self):
        with self.assertRaises(ValueError):
            subject.choose_batch(["a", "b"], [], 1)


stages = {"first": FirstChecks, "streaming": StreamingChecks,
          "queue": QueueChecks, "scheduler": SchedulerChecks}
selected = stages.values() if args.stage == "all" else [stages[args.stage]]
suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(cls) for cls in selected)
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
