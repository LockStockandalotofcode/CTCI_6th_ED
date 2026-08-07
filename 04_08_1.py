# Assumption: 
# access to link to parent nodes
# presence of node in the tree guaranteed

from typing import Optional, Callable

class ParentTreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def is_ancestor(node1: Optional[ParentTreeNode], node2: Optional[ParentTreeNode]) -> Optional[ParentTreeNode]:
    # if node1 is ancestor to node2, then node2's parent climbs up and meets node1
    # if node1 is not ancestor to node2, then node2's parent climbs up and reaches root, with no parents
    ancestor = node2
    while ancestor and ancestor != node1:
        ancestor = ancestor.parent
    return True if ancestor == node1 else False

def solver_fn(root: Optional[ParentTreeNode], p: Optional[ParentTreeNode], q: Optional[ParentTreeNode]) -> Optional[ParentTreeNode]:
    if not root: return None
    # if root == p or root == q: return root

    # base case for recursive algorithm
    # if is_ancestor(p, q): return p
    # if is_ancestor(q, p): return q

    # is_ancestor(p.parent, q)
    # is_ancestor(p, q.parent)
    ancestor_p = p
    ancestor_q = q

    while not is_ancestor(ancestor_p, q):
        ancestor_p = ancestor_p.parent

    return ancestor_p

def build_parent_tree():
    """
    Constructs tree with bi-directional parent pointers:
              1
            /   \
           2     3
          / \     \
         4   5     6
            / \
           7   8
    """
    n7 = ParentTreeNode(7)
    n8 = ParentTreeNode(8)
    n4 = ParentTreeNode(4)
    n5 = ParentTreeNode(5, left=n7, right=n8)
    n6 = ParentTreeNode(6)
    n2 = ParentTreeNode(2, left=n4, right=n5)
    n3 = ParentTreeNode(3, right=n6)
    root = ParentTreeNode(1, left=n2, right=n3)

    # Wire up parent pointers
    n7.parent = n5; n8.parent = n5
    n4.parent = n2; n5.parent = n2
    n2.parent = root; n6.parent = n3; n3.parent = root

    return root, n2, n3, n4, n5, n6, n7, n8


def run_parent_pointer_suite(solver_fn: Callable):
    """
    Accepts functions with signature:
      - solver_fn(p, q)
      - OR solver_fn(root, p, q)
    """
    root, n2, n3, n4, n5, n6, n7, n8 = build_parent_tree()

    # Skewed tree setup
    s40 = ParentTreeNode(40)
    s30 = ParentTreeNode(30, left=s40); s40.parent = s30
    s20 = ParentTreeNode(20, left=s30); s30.parent = s20
    s10 = ParentTreeNode(10, left=s20); s20.parent = s10

    # Single node tree setup
    single = ParentTreeNode(99)

    test_cases = [
        # (root, p, q, expected, description)
        (root, n4, n8, n2, "Across subtrees (4 and 8 -> 2)"),
        (root, n7, n8, n5, "Immediate siblings (7 and 8 -> 5)"),
        (root, n4, n6, root, "Main subtrees split (4 and 6 -> 1)"),
        (root, n2, n7, n2, "p is direct ancestor of q (2 and 7 -> 2)"),
        (root, root, n7, root, "p is root, q is deep node (1 and 7 -> 1)"),
        (root, n5, n5, n5, "Identity: p and q are exact same node (5 and 5 -> 5)"),
        (s10, s30, s40, s30, "Left-skewed line tree ancestor (30 and 40 -> 30)"),
        (single, single, single, single, "Single node tree (99 and 99 -> 99)"),
    ]

    print("\n" + "=" * 65)
    print("RUNNING SUITE 1: WITH PARENT POINTERS (Solutions 1 & 2)")
    print("=" * 65)

    passed = 0
    for i, (rt, p, q, expected, desc) in enumerate(test_cases, 1):
        try:
            # Flexible invocation (handles both f(p, q) and f(root, p, q))
            try:
                res = solver_fn(p, q)
            except TypeError:
                res = solver_fn(rt, p, q)

            assert res is expected, f"Expected {expected.val if expected else None}, got {res.val if res else None}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> {e}")

    print("-" * 65)
    print(f"SUITE 1 RESULT: {passed}/{len(test_cases)} Passed\n")


if __name__ == "__main__":
    run_parent_pointer_suite(solver_fn)