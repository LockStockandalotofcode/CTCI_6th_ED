from typing import Optional

class TreeNode:
    def __init__(self, val: int =0, left: int =None, right: int =None):
        self.val = val
        self.left = left
        self.right = right

def bst_sequences(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []
    
    # A valid choice is not just the direct relatives of a node (sibling node, or child nodes)
    # any unvisited node in the tree whose parent is added to the list, is a valid choice
    # root is always the starting point for such traversals
    result = []

    def helper(curr_path: list[int], valid_uncovered_nodes: list[TreeNode]):
        if len(valid_uncovered_nodes) == 0:
            result.append(list(curr_path))
            # need to append a copy of the current path,
            # appending curr_path appends the pointer to this curr_path, instead and doesnot append a list to the final result
            #  since the variable curr_path points to something that is constantly modified throughout until the the function gets executed
            #  list() creates a shallow copy to the current state of curr_path
            return

        # choose a valid node, append its children
        # this list that is passed into bakcktrack function serves as a set to check all visited nodes and helps to continue build the path forward
        for i, node in enumerate(valid_uncovered_nodes):
            next_valid_nodes = valid_uncovered_nodes[:i] + valid_uncovered_nodes[i + 1: ]
            # we should not use valid_uncovered_nodes.remove() or .pop() even temporarily
            # since that would mean modifying the iterable, over which we are iterating

            # append current node's children
            if node.left:
                next_valid_nodes.append(node.left)
            if node.right:
                next_valid_nodes.append(node.right)

            # recurse
            curr_path.append(node.val)
            helper(curr_path, next_valid_nodes)

            # backtrack
            curr_path.pop()
    
    helper([], [root])
    return result
    

def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


def are_trees_identical(
    t1: Optional[TreeNode], t2: Optional[TreeNode]
) -> bool:
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (
        t1.val == t2.val
        and are_trees_identical(t1.left, t2.left)
        and are_trees_identical(t1.right, t2.right)
    )


def run_bst_sequences_tests():
    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 4.9: BST SEQUENCES TESTS")
    print("=" * 60)

    # 1. Empty Tree
    # 2. Single Node Tree: [2]
    # 3. Skewed Tree: 1 -> 2 -> 3 (Only 1 valid sequence: [1, 2, 3])
    # 4. Balanced Tree: 2 with children 1, 3 (2 valid sequences: [2, 1, 3], [2, 3, 1])
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    balanced_root = TreeNode(2, left=n1, right=n3)

    skewed_root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))

    test_cases = [
        (None, 0, "Empty tree"),
        (TreeNode(10), 1, "Single node tree"),
        (skewed_root, 1, "Right-skewed tree (strict linear insertion sequence)"),
        (balanced_root, 2, "Simple balanced tree (2 valid woven sequences)"),
    ]

    for i, (root, expected_count, desc) in enumerate(test_cases, 1):
        try:
            seqs = bst_sequences(root)

            # Standardize empty representation ([[]] or [])
            if root is None:
                assert seqs in ([], [[]]), (
                    f"Expected [] or [[]] for empty tree, got {seqs}"
                )
            else:
                assert len(seqs) == expected_count, (
                    f"Expected {expected_count} sequences, got {len(seqs)}:"
                    f" {seqs}"
                )

                # Uniqueness check
                tuple_seqs = [tuple(s) for s in seqs]
                assert len(tuple_seqs) == len(
                    set(tuple_seqs)
                ), f"Duplicate sequences found in output: {seqs}"

                # Reconstruct BST for each generated sequence to prove exact tree fidelity
                for s in seqs:
                    reconstructed = None
                    for val in s:
                        reconstructed = insert_into_bst(reconstructed, val)
                    assert are_trees_identical(root, reconstructed), (
                        f"Sequence {s} failed to reconstruct identical BST"
                        " structure!"
                    )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.9 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_bst_sequences_tests()