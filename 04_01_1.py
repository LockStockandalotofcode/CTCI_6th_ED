# clarification: 
# could there be duplicate nodes, diff nodes with same values

# LOGIC/ CODE
# ASSUMING adj list (implemented as dict in python) for the graph implementation
from collections import deque
def route_between_nodes(graph_dict, node1, node2) -> bool:
    # absolute base case
    if not graph_dict or node1 not in graph_dict or node2 not in graph_dict: 
        return False
    
    # trivial case both node1, and node2 are same
    if node1 == node2:
        return True
    
    # initialise queue, with starting node
    queue = deque([node1])
    found_path = False # flag for result
    # maintain a set of visited nodes
    visited = set()

    while queue: # std python way, if empty this returns false
        curr_node = queue.popleft()
        # base check
        if curr_node == node2 and curr_node != node1: # but this fails when duplicate nodes exist
            found_path = True
            return found_path
        
        # append all neighbors
        for neighbor in graph_dict[curr_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return found_path

# =====================================================================
# UNIVERSAL TEST TEMPLATE: CTCI 4.1 ROUTE BETWEEN NODES (DO NOT EDIT)
# =====================================================================

def run_tests(has_route_function):
    print("=" * 65)
    print(" RUNNING UNIVERSAL TEST SUITE FOR 4.1: ROUTE BETWEEN NODES")
    print("=" * 65 + "\n")

    test_cases = [
        # --- CATEGORY 1: STANDARD PATHS ---
        {
            "category": "Standard",
            "desc": "Direct path exists (A -> B -> D)",
            "graph": {"A": ["B", "C"], "B": ["D"], "C": [], "D": []},
            "start": "A", "end": "D",
            "expected": True
        },
        {
            "category": "Standard",
            "desc": "No path exists between disconnected components",
            "graph": {"A": ["B"], "B": [], "C": ["D"], "D": []},
            "start": "A", "end": "D",
            "expected": False
        },
        {
            "category": "Standard",
            "desc": "Dead-end branch requires backtracking to find path",
            "graph": {
                "A": ["B", "C"],
                "B": ["D"],  # Dead end
                "C": ["E"],  # Valid path
                "D": [],
                "E": []
            },
            "start": "A", "end": "E",
            "expected": True
        },

        # --- CATEGORY 2: DIRECTED EDGE & CYCLE TRAPS ---
        {
            "category": "Directed Trap",
            "desc": "Path exists in reverse only (B -> A, but checking A -> B)",
            "graph": {"A": [], "B": ["A"]},
            "start": "A", "end": "B",
            "expected": False
        },
        {
            "category": "Cycle Check",
            "desc": "Graph contains cycles (A -> B -> C -> A) — prevents infinite loop",
            "graph": {
                "A": ["B"],
                "B": ["C"],
                "C": ["A", "D"],  # Cycle back to A + path to D
                "D": []
            },
            "start": "A", "end": "D",
            "expected": True
        },
        {
            "category": "Cycle Check",
            "desc": "Trapped in an isolated cycle without reaching target",
            "graph": {
                "A": ["B"],
                "B": ["C"],
                "C": ["A"],  # Infinite loop with no exit to D
                "D": []
            },
            "start": "A", "end": "D",
            "expected": False
        },

        # --- CATEGORY 3: EDGE & BOUNDARY CASES ---
        {
            "category": "Boundary",
            "desc": "Trivial path: Start and End are the same node (A == A)",
            "graph": {"A": ["B"], "B": []},
            "start": "A", "end": "A",
            "expected": True
        },
        {
            "category": "Boundary",
            "desc": "Isolated graph with no edges",
            "graph": {"A": [], "B": []},
            "start": "A", "end": "B",
            "expected": False
        },

        # --- CATEGORY 4: EMPTY / MISSING NODE STATES ---
        {
            "category": "Empty/Missing",
            "desc": "Empty graph",
            "graph": {},
            "start": "A", "end": "B",
            "expected": False
        },
        {
            "category": "Empty/Missing",
            "desc": "Start or End node not present in graph keys",
            "graph": {"A": ["B"]},
            "start": "A", "end": "Z",
            "expected": False
        }
    ]

    all_passed = True
    passed_count = 0

    for idx, tc in enumerate(test_cases, 1):
        try:
            result = has_route_function(tc["graph"], tc["start"], tc["end"])
            
            # Convert result to boolean explicitly
            result_bool = bool(result)
            
            if result_bool == tc["expected"]:
                print(f"✓ Test {idx:02d} [{tc['category']}] PASSED: {tc['desc']}")
                passed_count += 1
            else:
                all_passed = False
                print(f"✗ Test {idx:02d} [{tc['category']}] FAILED: {tc['desc']}")
                print(f"   Query    : Path from '{tc['start']}' -> '{tc['end']}'")
                print(f"   Expected : {tc['expected']}")
                print(f"   Got      : {result}\n")
        except Exception as e:
            all_passed = False
            print(f"✗ Test {idx:02d} [{tc['category']}] ERROR: {tc['desc']}")
            print(f"   Raised Exception: {type(e).__name__}: {e}\n")

    print("\n" + "=" * 65)
    print(f" SUMMARY: {passed_count}/{len(test_cases)} Tests Passed")
    if all_passed:
        print(" RESULT:  ALL TESTS PASSED! 🎉 (Traversal & cycle tracking verified)")
    else:
        print(" RESULT:  SOME TESTS FAILED ❌ (Check visited tracking or edge cases)")
    print("=" * 65 + "\n")

    return all_passed

if __name__ == "__main__":
    run_tests(route_between_nodes)