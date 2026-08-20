import math

def probability_of_collision(n_vertices: int = 3) -> float:
    """CTCI 6.4: Returns collision probability of ants walking on an n-vertex polygon."""
    total_possibilities = 2 ** n_vertices # n_vertices = no. of ants
    no_collision_prob = 2 # clockwise and anticlockwise
    return (total_possibilities - no_collision_prob) / total_possibilities

def run_ants_on_triangle_tests():
    test_cases = [
        (3, 0.75, "Triangle (n=3): Collision prob = 1 - (1/2)^2 = 0.75"),
        (4, 0.875, "Square (n=4): Collision prob = 1 - (1/2)^3 = 0.875"),
        (5, 0.9375, "Pentagon (n=5): Collision prob = 0.9375"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.4: ANTS ON A TRIANGLE TESTS")
    print("=" * 60)

    for i, (n, expected_prob, desc) in enumerate(test_cases, 1):
        try:
            res = probability_of_collision(n)
            assert math.isclose(
                res, expected_prob, rel_tol=1e-5
            ), f"For n={n}: Expected {expected_prob}, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"6.4 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_ants_on_triangle_tests()