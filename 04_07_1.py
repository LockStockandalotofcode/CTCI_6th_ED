from typing import List, Tuple, Optional
from collections import deque

class Node:
    def __init__(self, data:str="", children:list=[]):
        self.data = data
        self.children = children

def build_order(projects:list, dependencies:list[list]) -> list:
    if not projects and not dependencies: return []

    # build graph from dependencies
    # adjacency list - node, children
    # specifically dict in python
    graph_dict = {project: [] for project in projects}
    in_degree = {project: 0 for project in projects}
    # list tracks all the neighbor nodes
    # int tracks the in-degree of node

    for pair in dependencies:
        prerequisite = pair[0]
        course = pair[1]
        graph_dict[prerequisite].append(course) # append course as neighbor to prerequisite
        in_degree[course] += 1 # increment in-degree of course

    # queue-traversal through graph starts with all nodes having in-degree of 0
    # for this we need to track in-degree for all nodes in the graph
    # no_prereq_projects = []
    # for course in graph_dict:
    #     if in_degree[course] == 0:
    #         no_prereq_projects.append(course)

    no_prereq_projects = [p for p in projects if in_degree[p] == 0]
    

    # # traversal through the graph, for the building right order
    # if not no_prereq_projects:
    #     return 

    queue = deque(no_prereq_projects)
    right_order = []
    while queue:
        curr = queue.popleft()
        right_order.append(curr)
        for neighbor in graph_dict[curr]:
            # decrement in-degree of neighbors, 
            # a course gets added to queue only when its in-degree = 0, i.e., all its prerequisites have been already added to the queue
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(right_order) != len(projects):
        return [] # a cycle exists

    return right_order

def validate_topological_order(
    projects: List[str],
    dependencies: List[Tuple[str, str]],
    result: Optional[List[str]],
) -> bool:
    if result is None or (result == [] and len(projects) > 0):
        return False  # Represents invalid build order (cycle detected)

    if len(result) != len(projects) or set(result) != set(projects):
        return False  # Incomplete or mutated project set

    pos = {p: i for i, p in enumerate(result)}
    for dep, proj in dependencies:
        if pos[dep] >= pos[proj]:
            return False  # Dependency built after project!

    return True


def run_build_order_tests():
    # Format: (projects, dependencies, is_possible, description)
    test_cases = [
        ([], [], True, "Empty projects and dependencies"),
        (["a"], [], True, "Single project, no dependencies"),
        (["a", "b"], [("a", "b")], True, "Simple two-node linear dependency"),
        (
            ["a", "b", "c", "d", "e", "f"],
            [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")],
            True,
            "CTCI standard example DAG",
        ),
        (
            ["a", "b", "c"],
            [("a", "b"), ("b", "c"), ("c", "a")],
            False,
            "Simple 3-node cycle",
        ),
        (
            ["a", "b", "c", "d"],
            [("a", "b"), ("b", "c"), ("c", "d")],
            True,
            "Strict linear chain (a -> b -> c -> d)",
        ),
        (
            ["a", "b", "c", "d"],
            [("a", "b"), ("b", "c"), ("c", "b")],
            False,
            "Disconnected cycle in subgraph (b <-> c)",
        ),
        (
            ["a", "b", "c", "d", "e"],
            [],
            True,
            "Multiple independent projects, zero dependencies",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 4.7: BUILD ORDER TESTS")
    print("=" * 60)

    for i, (projects, deps, is_possible, desc) in enumerate(test_cases, 1):
        try:
            res = build_order(projects, deps)

            if not is_possible:
                assert res is None or res == [], (
                    f"Expected None/[] due to cycle, but got valid order:"
                    f" {res}"
                )
            else:
                is_valid = validate_topological_order(projects, deps, res)
                assert (
                    is_valid
                ), f"Invalid topological order generated: {res} for deps {deps}"

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.7 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_build_order_tests()