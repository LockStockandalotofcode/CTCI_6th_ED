from typing import Optional

class TreeNode:
    def __init__(self, val: int =0, left: int =None, right: int =None):
        self.val = val
        self.left = left
        self.right = right

# at every node, we have 3 choices between going and adding its sibling node or left child, or right child

def bst_sequences(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    # # recursion & backtracking
    # bst_sequences(root.left)
    # bst_sequences(root.right)

    final = [] # initialise with root node
    visited = set()
    visited.add(root.val, root.left.val)
    build_traversal(root, root.left, [root.val, root.left.val], visited, final)

    visited = set()
    visited.add(root.val, root.right.val)
    build_traversal(root, root.right, [root.val, root.right.val], visited, final)

    return final

def build_traversal(parent: TreeNode, node: TreeNode, curr_list: list[int], visited: set, final_lists: list[list[int]]) -> None:
    # when going forward recursively we add the element
    # we need to have a base case, when there are no more nodes, then we append that list to the result
    # once we recurse back, backtracking is done through popping all traversal from this node

    # def go_forward():


    
    # The below order in which they are executed doesnot matter, since we are convering all options of traversal

    # choice 1: next node is sibling node
                                                # if next_node.parent is not None: # except for root node
                                                # we are not covering root node here, since we want parent link in the tree for this to work, not guaranteed
    # if node is left child, to right child, otherwise vice versa
    next_node = parent.right if node == parent.left else parent.left

    # BASE CASE CHECK
    if next_node in visited and node.left in visited and node.right in visited:
        final_lists.append(curr_list)
        return
    
    curr_list.append(next_node.val)
    # recurse 
    build_traversal(parent, next_node, curr_list, visited, final_lists)
    # if reached end, append it to the final results list of lists
    # backtrack
    curr_list.pop()
    

    # choice 2: next node is left child node
    # if node is left child, to right child, otherwise vice versa
    next_node = node.left
    curr_list.append(next_node.val)
    # recurse 
    build_traversal(parent, next_node, curr_list, visited, final_lists)
    # backtrack
    curr_list.pop()
    
    
    # choice 3: next node is right child node
    # if node is left child, to right child, otherwise vice versa
    next_node = parent.right if node == parent.left else parent.left
    curr_list.append(next_node.val)
    # recurse 
    build_traversal(parent, next_node, curr_list)
    # backtrack
    curr_list.pop()

    return

# setup a function to incorporate going forward from any node, to get rid of the redundant code in above function















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