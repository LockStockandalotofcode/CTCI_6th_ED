from collections import deque

# LOGIC / CODE
# level order traversal
# creating a new linked list at each level
# appending head it to result of linked_lists

class ListNode:
    def __init__(self, val, next_val=None):
        self.val = val
        self.next = next_val

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def list_of_depths_fn(root: TreeNode) ->list[ListNode]:
    # absolute base case: empty case
    if not root:
        return []
    
    #initialise queue
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        # error 1 head_node points right bofore the actual head of linked list
        # error 2 queue[0] gives entire treeNode, we need only its value to create the linked list node
        head_node = list_node = ListNode(queue[0].val)
        for _ in range(level_size):
            # pop and execute current/top node
            curr = queue.popleft()
            # make listnode, and increment the running variable to tail node
            list_node.next = ListNode(curr.val)
            list_node = list_node.next
            # append all child nodes of current node
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        
        # after level-order traversal
        # as a correction to error 1, subsequently append the actual head to result list
        result.append(head_node.next)

    return result

# =====================================================================
# UNIVERSAL TEST SUITE: CTCI 4.3 LIST OF DEPTHS (DECOUPLED)
# =====================================================================

class TreeNode:
    """Standard Binary Tree Node structure used to construct test inputs."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _normalize_output(raw_result) -> list[list]:
    """
    Intelligent Adapter: Normalizes any custom data structure (LinkedLists,
    lists of TreeNodes, primitive lists, or depth dicts) into a standard list of value lists.
    """
    if raw_result is None or raw_result == [] or raw_result == {}:
        return []

    if isinstance(raw_result, dict):
        raw_result = [raw_result[k] for k in sorted(raw_result.keys())]

    matrix = []
    for level in raw_result:
        level_vals = []
        curr = level

        # Custom Linked List Head (has .val and .next)
        if hasattr(curr, "next"):
            while curr:
                val = curr.val
                level_vals.append(val.val if hasattr(val, "val") else val)
                curr = curr.next

        # List or tuple of items
        elif isinstance(curr, (list, tuple)):
            for item in curr:
                level_vals.append(item.val if hasattr(item, "val") else item)

        # Single Node or Primitive value
        else:
            level_vals.append(curr.val if hasattr(curr, "val") else curr)

        matrix.append(level_vals)

    return matrix


def run_tests(list_of_depths_function):
    """
    Executes universal tests against any solution function with signature:
    list_of_depths_function(root: TreeNode) -> Any
    """
    print("=" * 65)
    print(" RUNNING UNIVERSAL TEST SUITE FOR 4.3: LIST OF DEPTHS")
    print("=" * 65 + "\n")

    # Tree Fixtures
    complete_tree = TreeNode(1,
        left=TreeNode(2, TreeNode(4), TreeNode(5)),
        right=TreeNode(3, TreeNode(6), TreeNode(7))
    )
    right_skewed = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4))))
    left_skewed = TreeNode(10, left=TreeNode(20, left=TreeNode(30)))
    zigzag_tree = TreeNode(1,
        left=TreeNode(2, right=TreeNode(4)),
        right=TreeNode(3, left=TreeNode(5))
    )

    test_cases = [
        # --- CATEGORY 1: STANDARD CASES ---
        {
            "category": "Standard",
            "desc": "Complete Binary Tree (Depth 3)",
            "root": complete_tree,
            "expected": [[1], [2, 3], [4, 5, 6, 7]]
        },
        {
            "category": "Standard",
            "desc": "Asymmetric / Zigzag Tree",
            "root": zigzag_tree,
            "expected": [[1], [2, 3], [4, 5]]
        },

        # --- CATEGORY 2: UNBALANCED & SKEWED TREES ---
        {
            "category": "Unbalanced",
            "desc": "Right-Skewed Tree (Linked-list shape)",
            "root": right_skewed,
            "expected": [[1], [2], [3], [4]]
        },
        {
            "category": "Unbalanced",
            "desc": "Left-Skewed Tree",
            "root": left_skewed,
            "expected": [[10], [20], [30]]
        },

        # --- CATEGORY 3: BOUNDARY & EDGE CASES ---
        {
            "category": "Boundary",
            "desc": "Single Node Tree (Depth 1)",
            "root": TreeNode(42),
            "expected": [[42]]
        },

        # --- CATEGORY 4: EMPTY / NULL INPUT ---
        {
            "category": "Empty",
            "desc": "Null Root Input (None)",
            "root": None,
            "expected": []
        }
    ]

    all_passed = True
    passed_count = 0

    for idx, tc in enumerate(test_cases, 1):
        try:
            raw_result = list_of_depths_function(tc["root"])
            normalized_result = _normalize_output(raw_result)

            if normalized_result == tc["expected"]:
                print(f"✓ Test {idx:02d} [{tc['category']}] PASSED: {tc['desc']}")
                passed_count += 1
            else:
                all_passed = False
                print(f"✗ Test {idx:02d} [{tc['category']}] FAILED: {tc['desc']}")
                print(f"   Expected Depths : {tc['expected']}")
                print(f"   Got Depths      : {normalized_result}\n")
        except Exception as e:
            all_passed = False
            print(f"✗ Test {idx:02d} [{tc['category']}] ERROR: {tc['desc']}")
            print(f"   Raised Exception: {type(e).__name__}: {e}\n")

    print("\n" + "=" * 65)
    print(f" SUMMARY: {passed_count}/{len(test_cases)} Tests Passed")
    if all_passed:
        print(" RESULT:  ALL TESTS PASSED! 🎉")
    else:
        print(" RESULT:  SOME TESTS FAILED ❌")
    print("=" * 65 + "\n")

    return all_passed

if __name__ == "__main__":
    run_tests(list_of_depths_fn)