def count_eval(expression: str, result: bool, memo=None) -> int:
    """CTCI 8.14: Counts ways to parenthesize expression to yield target result."""
    # TOP DOWN RECURSIVE W/ MEMOIZATION
    if memo is None:
        memo = {}
    key = (expression, result)
    if key in memo:
        return memo[key]
    # Base case
    if len(expression) == 0:
        return 0
    if len(expression) == 1:
        # breakpoint()
        return 1 if bool(int(expression)) == result else 0
    
    ways = 0
    i = 1
    while i < len(expression):
        left_exp = expression[:i]
        right_exp = expression[i + 1 :]
        # count all the possible possibilities
        left_t = count_eval(left_exp, True, memo)
        left_f = count_eval(left_exp, False, memo)
        right_t = count_eval(right_exp, True, memo)
        right_f = count_eval(right_exp, False, memo)
        
        total_true = 0
        if expression[i] == '^':
            total_true = (left_t * right_f) + (left_f * right_t)
        elif expression[i] == '|':
            total_true = (left_t * right_f) + (left_f * right_t) + (left_t * right_t)
        elif expression[i] == '&':
            total_true = (left_t * right_t)
        total_ways = (left_t * right_f) + (left_f * right_t) + (left_t * right_t) + (left_f * right_f)
        
        subproblem_ways = total_true if result == True else (total_ways - total_true)
        ways += subproblem_ways

        i += 2
    memo[(expression, result)] = ways
    return memo[(expression, result)]

def run_boolean_evaluation_tests():
    test_cases = [
        ("1", True, 1, "Single literal '1' evaluating True"),
        ("1", False, 0, "Single literal '1' evaluating False"),
        ("0", True, 0, "Single literal '0' evaluating True"),
        ("0", False, 1, "Single literal '0' evaluating False"),
        ("1^0|0|1", False, 2, "CTCI Example 1 ('1^0|0|1', result=False)"),
        ("0&0&0&1^1|0", True, 10, "CTCI Example 2 ('0&0&0&1^1|0', result=True)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.14: BOOLEAN EVALUATION TESTS")
    print("=" * 60)

    for i, (expr, target, expected, desc) in enumerate(test_cases, 1):
        try:
            res = count_eval(expr, target)
            assert res == expected, (
                f"Expression '{expr}' for target={target}: Expected {expected},"
                f" got {res}"
            )
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.14 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_boolean_evaluation_tests()