class TreeNode:
    def __init__(self, val:int = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def count_paths_with_sum(root: TreeNode, target_sum: int) -> int:
    if not root or target_sum is None:
        return 0

    prefix_sums = {0 : 1}
    def dfs(node: TreeNode | None, curr_sum: int):
        # base case
        if node is None:
            return 0
        curr_sum += node.val
        valid_paths = prefix_sums.get(curr_sum - target_sum, 0)
        # add this prefix sum for recuursion on child nodes
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum , 0) + 1
        # recurse 
        valid_paths += dfs(node.left, curr_sum)
        valid_paths += dfs(node.right, curr_sum)
        # backtrack
        prefix_sums[curr_sum] -= 1
        # curr_sum -= node.val
        return valid_paths

    return dfs(root,0)

def run_paths_with_sum_tests():
    # Tree 1 Construction (CTCI Example):
    #          10
    #        /    \
    #       5      -3
    #      / \       \
    #     3   2       11
    #    / \   \
    #   3  -2   1
    n3_l = TreeNode(3)
    n2_neg = TreeNode(-2)
    n1_r = TreeNode(1)
    n3 = TreeNode(3, left=n3_l, right=n2_neg)
    n2 = TreeNode(2, right=n1_r)
    n5 = TreeNode(5, left=n3, right=n2)
    n11 = TreeNode(11)
    n3_neg = TreeNode(-3, right=n11)
    root = TreeNode(10, left=n5, right=n3_neg)

    # Tree 2: Zero values (1 -> 0 -> 0 -> -1) target = 1
    # Paths: [1], [1,0], [1,0,0], [0,0,-1], [0,-1]...
    z_neg1 = TreeNode(-1)
    z0_2 = TreeNode(0, left=z_neg1)
    z0_1 = TreeNode(0, left=z0_2)
    zero_root = TreeNode(1, left=z0_1)

    test_cases = [
        (None, 8, 0, "Empty tree"),
        (TreeNode(5), 5, 1, "Single node matching target"),
        (TreeNode(5), 10, 0, "Single node not matching target"),
        (root, 8, 3, "CTCI example tree (Target 8 -> 3 paths)"),
        (root, 18, 3, "Path starting at root (10 -> 5 -> 3)"),
        (zero_root, 1, 3, "Tree with 0s generating multiple valid prefix paths"),
        (
            root,
            -3,
            1,
            "Target sum negative (Path with single node -3)",
        ),
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 4.12: PATHS WITH SUM TESTS")
    print("=" * 60)

    for i, (t_root, target, expected, desc) in enumerate(test_cases, 1):
        try:
            res = count_paths_with_sum(t_root, target)
            assert (
                res == expected
            ), f"Target {target}: Expected {expected} paths, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.12 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_paths_with_sum_tests()