from typing import Tuple
import math
def optimal_basketball_game(p: float) -> Tuple[float, float, int]:
    # CTCI 6.2: Calculates winning probabilities for Game 1 (1 shot) and Game 2 (3 shots, make >= 2).

    # Given single-shot probability p (0 <= p <= 1), returns:
    # (prob_game1, prob_game2, best_game_choice)
    # where best_game_choice is 1 or 2 (or 1 if equal).

    game1 = p
    game2 = 3* p * p * (1-p) + p*p*p # if winning game2 requires atleast 2 shots
    best_game_choice = 1 if game1 > game2 else 2
    return (game1, game2, best_game_choice)

def run_basketball_tests():
    # Format: (p, expected_p1, expected_p2, valid_choices, description)
    test_cases = [
        (0.0, 0.0, 0.0, {1, 2}, "p = 0.0 boundary (0 probability for both)"),
        (0.25, 0.25, 0.15625, {1}, "p = 0.25 (Game 1 strictly better)"),
        (0.5, 0.5, 0.5, {1, 2}, "p = 0.5 break-even point (Equal probability)"),
        (0.75, 0.75, 0.84375, {2}, "p = 0.75 (Game 2 strictly better)"),
        (1.0, 1.0, 1.0, {1, 2}, "p = 1.0 boundary (100% probability for both)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.2: BASKETBALL PROBABILITY TESTS")
    print("=" * 60)

    for i, (p, exp_p1, exp_p2, valid_choices, desc) in enumerate(test_cases, 1):
        try:
            p1, p2, choice = optimal_basketball_game(p)

            assert math.isclose(p1, exp_p1, abs_tol=1e-5), (
                f"Game 1 prob for p={p}: Expected {exp_p1}, got {p1}"
            )
            assert math.isclose(p2, exp_p2, abs_tol=1e-5), (
                f"Game 2 prob for p={p}: Expected {exp_p2}, got {p2}"
            )
            assert choice in valid_choices, (
                f"Optimal game choice for p={p}: Expected one of {valid_choices}, got {choice}"
            )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"6.2 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_basketball_tests()