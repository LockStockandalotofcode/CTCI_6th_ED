# recursion & backtracking approach
def generate_parens(n: int) -> list[str]:
    if not n: return []

    # BOTTOM-UP APPROACH
    def helper(n:int) -> list:
    # def helper(n:int, curr_list: list) -> list:
        if n == 1: 
            return ["()"]

        prev_list = helper(n-1)
        # prev_list = helper(n-1, curr_list)
        new_list = []
        for item in prev_list: # item is str data type
            # .insert() cannot append at the very last position
            # .insert(-1, item) appends right before the very last position
            # use .append() to do so

            # AROUND
            item1 = list(item)
            item1.insert(0, "(")
            item1.append(")")
            item1 = "".join(item1)
            if item1 not in new_list:
                new_list.append(item1)

            # AFTER
            item2 = list(item)
            item2.append( "(")
            item2.append( ")")
            item2 = "".join(item2)
            if item2 not in new_list:
                new_list.append(item2)

            # BEFORE
            item3 = list(item)
            item3.insert(0, ")")
            item3.insert(0, "(")
            item3 = "".join(item3)
            if item3 not in new_list:
                new_list.append(item3)

        return new_list

    return helper(n)

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