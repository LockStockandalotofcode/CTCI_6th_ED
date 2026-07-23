# CODE / LOGIC
# major learning: combinatorics 0! = 1
# no. of ways of reaching stairs of 0-length = 1 (mathematically and physically true), though not so intuitive
# no._of_ways(0) = no._of_ways(3 - 3) = no. of ways going from stair 3 to ground(0) after 3-step jump = 1,
# just stay there; doing nothing (0) is a decision. counts as 1
# DP problem
# 2 ways going forward - top-down (memoization helps avoid repeating subproblems) - downside: recursive stack overflow
# bottom-up approach (creating array of result of subproblems) - downside: less space efficient 

# recursive formula : n = (n-1) + (n-2) + (n-3)

def triple_step_top_down(n: int):
    # negative case: incorrect input
    if n < 0:
        return 0
    # absolute base cases;
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return triple_step_top_down(n - 1) + triple_step_top_down(n - 2) + triple_step_top_down(n - 3)

# =====================================================================
# UNIVERSAL TEST SUITE: CTCI 8.1 TRIPLE STEP (DECOUPLED)
# =====================================================================

def run_tests(triple_step_function):
    """
    Executes universal tests against any solution function with signature:
    triple_step_function(n: int) -> int
    """
    print("=" * 65)
    print(" RUNNING UNIVERSAL TEST SUITE FOR 8.1: TRIPLE STEP")
    print("=" * 65 + "\n")

    test_cases = [
        # --- CATEGORY 1: STANDARD CASES ---
        {"category": "Standard", "desc": "3 steps (1+1+1, 1+2, 2+1, 3)", "n": 3, "expected": 4},
        {"category": "Standard", "desc": "4 steps", "n": 4, "expected": 7},
        {"category": "Standard", "desc": "5 steps", "n": 5, "expected": 13},
        {"category": "Standard", "desc": "10 steps", "n": 10, "expected": 274},

        # --- CATEGORY 2: BASE & BOUNDARY CASES ---
        {"category": "Boundary", "desc": "1 step", "n": 1, "expected": 1},
        {"category": "Boundary", "desc": "2 steps (1+1, 2)", "n": 2, "expected": 2},

        # --- CATEGORY 3: EMPTY / ZERO / INVALID STATES ---
        {"category": "Empty/Zero", "desc": "0 steps (Base case: 1 path - doing nothing)", "n": 0, "expected": 1},
        {"category": "Invalid", "desc": "Negative stair count (Impossible path)", "n": -5, "expected": 0},

        # # --- CATEGORY 4: LARGE INPUT (PERFORMANCE TEST) ---
        # {"category": "Performance", "desc": "35 steps (Verifies O(N) DP / Memoization efficiency)", "n": 35, "expected": 11324368657}
    ]

    all_passed = True
    passed_count = 0

    for idx, tc in enumerate(test_cases, 1):
        if idx == 9:
            break
        try:
            result = triple_step_function(tc["n"])
            if result == tc["expected"]:
                print(f"✓ Test {idx:02d} [{tc['category']}] PASSED: {tc['desc']}")
                passed_count += 1
            else:
                all_passed = False
                print(f"✗ Test {idx:02d} [{tc['category']}] FAILED: {tc['desc']}")
                print(f"   Input N  : {tc['n']}")
                print(f"   Expected : {tc['expected']}")
                print(f"   Got      : {result}\n")
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
    run_tests(triple_step_top_down)