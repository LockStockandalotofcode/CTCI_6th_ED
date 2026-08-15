from typing import Optional
import collections
import random

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1
        self._update_size()

    def _get_size(self):
        return self.size
    def _update_size(self):
        left_sz = self.left.size if self.left else 0
        right_sz = self.right.size if self.right else 0
        self.size = left_sz + right_sz + 1

    def _get_value(self):
        return self.val

    def insert_in_order(self, node_val: int):
        if node_val < self.val:
            if self.left is None:
                self.left = TreeNode(node_val)
            else:
                self.left.insert_in_order( node_val)
        else:
            if self.right is None:
                self.right = TreeNode(node_val)
            else:
                self.right.insert_in_order(node_val)

        self._update_size()

    def get_node_by_val(self, node_val: int):
        if self.val == node_val:
            return self
        elif node_val < self.val:
            return self.left.get_node_by_val(node_val) if self.left else None
        else:
            return self.right.get_node_by_val(node_val) if self.right else None

    def get_node_by_index(self, idx: int):
        left_size = self.left.size if self.left else 0

        if idx < left_size:
            return self.left.get_node_by_index(idx)
        elif idx == left_size:
            return self
        else:
            return self.right.get_node_by_index(idx - left_size - 1)

    def get_random_node(self):
        random_index = random.randint(0, self.size - 1)
        return self.get_node_by_index(random_index)

    def delete_node(self, node_val: int):
        if node_val < self.val:
            if self.left:
                self.left = self.left.delete_node(node_val)
        elif node_val > self.val:
            if self.right:
                self.right = self.right.delete_node( node_val)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # else node has 2 child both left and right
            successor = self.right
            while successor.left:
                successor = successor.left

            self.val = successor.val
            self.right = self.right.delete_node(successor.val)

        self._update_size()
        return self

def get_random_node(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Top-level wrapper to handle empty tree case safely."""
    if root is None:
        return None
    return root.get_random_node()
    
    
def run_random_node_tests():
    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 4.11: RANDOM NODE TESTS")
    print("=" * 60)

    # 1. Empty Tree Case
    try:
        assert (
            get_random_node(None) is None
        ), "Empty tree should return None for random node"
        print("  [PASS] Test 01: Empty tree returns None")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 01 -> ERROR: {e}")
        failed += 1

    # 2. Single Node Tree Case
    try:
        single_root = TreeNode(42)
        node = get_random_node(single_root)
        assert (
            node is single_root
        ), "Single node tree must always return root instance"
        print("  [PASS] Test 02: Single node tree returns identity")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 02 -> ERROR: {e}")
        failed += 1

    # 3. Uniform Distribution Statistical Test (10,000 Trials)
    try:
        n10 = TreeNode(10)
        n30 = TreeNode(30)
        n20 = TreeNode(20, left=n10, right=n30)
        n50 = TreeNode(50)
        root = TreeNode(40, left=n20, right=n50)

        counts = collections.defaultdict(int)
        trials = 10000

        for _ in range(trials):
            sampled_node = get_random_node(root)
            assert (
                sampled_node is not None
            ), "Random node returned None on valid tree"
            counts[sampled_node.val] += 1

        assert len(counts) == 5, f"Expected 5 distinct nodes, got {len(counts)}"

        expected_count = trials / 5  # 2000
        tolerance = 500  # Statistical tolerance interval

        for val, count in counts.items():
            assert abs(count - expected_count) < tolerance, (
                f"Node {val} distribution out of bounds: got {count} hits,"
                f" expected ~{expected_count}"
            )

        print(
            f"  [PASS] Test 03: Statistical Uniform Probability Across {trials}"
            f" Trials ({dict(counts)})"
        )
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 03 -> ERROR: {e}")
        failed += 1

    # 4. Deletion Integrity Test
    try:
        b_root = TreeNode(40)
        for val in [20, 10, 30, 50]:
            b_root.insert_in_order(val)

        assert b_root.size == 5, f"Expected size 5, got {b_root.size}"
        b_root = b_root.delete_node(20)
        assert b_root.size == 4, f"Expected size 4 after deletion, got {b_root.size}"
        assert (
            b_root.get_node_by_val(20) is None
        ), "Node 20 should no longer exist in tree"

        print("  [PASS] Test 04: Node deletion and size recalculation")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 04 -> ERROR: {e}")
        failed += 1

    print("-" * 60)
    print(f"4.11 SUMMARY: {passed} PASSED | {failed} FAILED | Total: 4")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_random_node_tests()