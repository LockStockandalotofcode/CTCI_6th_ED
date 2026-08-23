class RankNode:
    # Augmented BST
    # Rank Tree
    def __init__(self, val:int):
        self.val = val
        self.left_size = 0
        self.count = 1
        self.left = None
        self.right = None

    def track(self, x: int) -> None:
        """CTCI 10.10: Process a number from the stream."""
        if x == self.val:
            self.count += 1
        elif x < self.val:
            self.left_size += 1
            if not self.left:
                self.left = RankNode(x)
            else:
                return self.left.track(x)
        else:
            if not self.right:
                self.right = RankNode(x)
            else:
                return self.right.track(x)

    def get_rank_of_number(self, x: int) -> int:
        """CTCI 10.10: Return count of values <= x (excluding the instance itself once)."""
        # breakpoint()
        if x == self.val:
            return self.left_size + self.count - 1
        elif x < self.val:
            return self.left.get_rank_of_number(x) if self.left else -1
        else:
            if not self.right:
                return -1
            right_rank = self.right.get_rank_of_number(x)
            if right_rank == -1:
                return -1
            return self.left_size + self.count + right_rank
            # right_rank gives rank in the right subtree, with x at as this subtree's rootnode

class RankTracker:
    """Wrapper Class to handle stream initialisation"""
    def __init__(self):
        self.root = None

    def track(self, x: int) -> None:
        if not self.root:
            self.root = RankNode(x)
        else:
            self.root.track(x)

    def get_rank_of_number(self, x: int) -> int:
        if not self.root:
            return -1
        return self.root.get_rank_of_number(x)

def run_rank_from_stream_tests():
    # breakpoint()
    tracker = RankTracker()
    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

    for val in stream:
        tracker.track(val)

    test_queries = [
        (1, 0, "Rank of smallest element 1"),
        (3, 1, "Rank of element 3"),
        (4, 3, "Rank of duplicate element 4"),
        (5, 5, "Rank of duplicate element 5"),
        (13, 8, "Rank of maximum element 13"),
        (0, -1, "Rank of query element smaller than all in stream"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.10: RANK FROM STREAM TESTS")
    print("=" * 60)

    for i, (val, expected_rank, desc) in enumerate(test_queries, 1):
        try:
            res = tracker.get_rank_of_number(val)
            assert res == expected_rank, (
                f"Query {val}: Expected rank {expected_rank}, got {res}"
            )
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"10.10 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_queries)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_rank_from_stream_tests()