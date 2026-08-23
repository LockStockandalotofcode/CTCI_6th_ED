import random

def simulate_one_family() -> tuple[int, int]:
    # gives out numver of boys and girls born in a family 
    girls, boys = 0, 0
    while girls == 0:
        if random.random() < 0.5:
            girls += 1
        else:
            boys += 1

    return (girls, boys)

def simulate_apocalypse_ratio(num_families: int) -> float:
    """CTCI 6.7: Simulates family policy (stop after 1st girl) and returns expected ratio of girls to total children."""
    if num_families <= 0:
        return 0.0

    total_girls, total_boys = 0, 0
    for _ in range(num_families):
        girls, boys = simulate_one_family()
        total_girls += girls
        total_boys += boys
    
    return total_girls / (total_girls + total_boys)

def run_apocalypse_tests():
    test_cases = [
        (10000, 0.50, "Large population simulation (10,000 families)"),
        (100000, 0.50, "Extremely large population simulation (100,000 families)"),
        (0, 0.0, "Zero families boundary check"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.7: THE APOCALYPSE TESTS")
    print("=" * 60)

    for i, (num_families, expected_ratio, desc) in enumerate(test_cases, 1):
        try:
            res = simulate_apocalypse_ratio(num_families)
            if num_families == 0:
                assert res == 0.0 or res is None, f"Expected 0.0/None for 0 families, got {res}"
            else:
                assert 0.48 <= res <= 0.52, f"Expected girl proportion ~0.50, got {res:.4f}"
            print(f"  [PASS] Test {i:02d}: {desc} (Ratio: {res})")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"6.7 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_apocalypse_tests()