def print_binary(num: float) -> str:
    # APPROACH 1: multiply by 2, compare with 1, gets next digit 0 or 1, then we append it to the result
    # APPROACH 2: directly compare with (decreasing powers of 1/2) 0.5 (1/2)^1, 0.25 (1/2)^2, 0.125 (1/2)^3, 0.625 (1/2)^4, gets next digit 0 or 1, then we append it to the result
    if num >= 1 or num <= 0:
        return "ERROR"

    result = ["."] # creating the required string, as a list of characters and then return it as string
    while num > 0:
        if len(result) >= 32: return "ERROR"
        # get the digit
        num *= 2
        # compare with 1
        if num >= 1:
            result.append("1")
            num -= 1
        # append the next digit to result 0 or 1
        else:
            result.append("0")


    return "".join(result)

def run_binary_to_string_tests():
    test_cases = [
        (0.5, "0.1", "0.5 (1/2)"),
        (0.25, "0.01", "0.25 (1/4)"),
        (0.75, "0.11", "0.75 (3/4)"),
        (0.625, "0.101", "0.625 (5/8)"),
        (0.8125, "0.1101", "0.8125 (13/16)"),
        (0.1, "ERROR", "0.1 (Non-terminating binary representation)"),
        (0.3, "ERROR", "0.3 (Non-terminating binary representation)"),
        (0.0, "ERROR", "Out-of-bounds lower limit (num <= 0)"),
        (1.0, "ERROR", "Out-of-bounds upper limit (num >= 1)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 5.2: BINARY TO STRING TESTS")
    print("=" * 60)

    for i, (num, expected, desc) in enumerate(test_cases, 1):
        try:
            res = print_binary(num)
            if expected != "ERROR" and res.startswith("."):
                res = "0" + res

            assert (
                res == expected
            ), f"For input {num}: Expected '{expected}', got '{res}'"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"5.2 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_binary_to_string_tests()