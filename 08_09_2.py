# recursion & backtracking approach
def generate_parens(n: int) -> list[str]:
    if n <= 0: return []

    # BOTTOM-UP APPROACH
    # using set to avoid duplicates
    curr_level = {"()"}

    for _ in range(2, n+1):
        next_level = set()
        for item in curr_level:
            # inserting () at index 0
            next_level.add("()" + item)

            # inserting () after every opening parens (
            for i, char in enumerate(item): # looping through item's characters which is a string
                if char == "(":
                    next_level.add(item[: i+1] + "()" + item[i+1 :])

        curr_level = next_level
    return list(curr_level)









def is_valid_parens(s: str) -> bool:
    balance = 0
    for char in s:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


def run_parens_tests():
    # Catalan numbers C_n for n = 0..4
    test_cases = [
        (0, 1, "n = 0 pairs"),
        (1, 1, "n = 1 pair -> ['()']"),
        (2, 2, "n = 2 pairs -> ['(())', '()()']"),
        (3, 5, "n = 3 pairs (Catalan C_3 = 5)"),
        (4, 14, "n = 4 pairs (Catalan C_4 = 14)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.9: PARENS TESTS")
    print("=" * 60)

    for i, (n, expected_count, desc) in enumerate(test_cases, 1):
        try:
            res = generate_parens(n)
            if res is None:
                res = []

            if n == 0:
                assert res in ([], [""]), f"Expected [] or [''] for n=0, got {res}"
            else:
                assert len(res) == expected_count, (
                    f"Expected {expected_count} combinations for n={n}, got"
                    f" {len(res)}"
                )
                assert len(res) == len(
                    set(res)
                ), f"Duplicates found in output: {res}"
                for p_str in res:
                    assert (
                        len(p_str) == 2 * n
                    ), f"String '{p_str}' length != {2*n}"
                    assert is_valid_parens(
                        p_str
                    ), f"Invalid parentheses string: '{p_str}'"

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.9 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_parens_tests()