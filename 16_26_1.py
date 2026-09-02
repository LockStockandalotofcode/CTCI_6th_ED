import unittest

def calculate(expression: str) -> float:
    if not expression or not expression.strip():
        raise ValueError("Expression cannot be empty.")
    s = expression.replace(" ", "")
    stack = []

    # read expression into respective stacks 
    # whilst computing all the higher precendce operations, negating whenever - comes across
    
    # while traversing the expression, we make numbers, more than single digit 
    # add their appropriate partially computed values in the stack

    curr_num = 0
    curr_op = '+'
    for i, char in enumerate(s):
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)

        # i == len(s) ensures the very last element is taken into account and added to stack
        # other wise it doesn;t get added to the stack
        if not char.isdigit() or i == len(s) - 1:
            if curr_op == '+':
                stack.append(curr_num)
            elif curr_op == '-':
                stack.append(-curr_num)
            elif curr_op == '*':
                prev = stack.pop()
                stack.append(prev * curr_num)
            elif curr_op == '/':
                prev = stack.pop()
                stack.append(prev / curr_num)

            curr_op = char
            curr_num = 0

    return float(sum(stack))
            
# =====================================================================
# TEST SUITE
# =====================================================================
class TestCalculator(unittest.TestCase):

    def test_01_empty_or_whitespace(self):
        """Empty or whitespace-only string raises ValueError."""
        with self.assertRaises(ValueError):
            calculate("")
        with self.assertRaises(ValueError):
            calculate("   ")

    def test_02_single_number(self):
        """Single number evaluates to its own value."""
        self.assertEqual(calculate("42"), 42.0)

    def test_03_simple_addition_subtraction(self):
        """Basic addition and subtraction."""
        self.assertEqual(calculate("2 + 3 - 1"), 4.0)

    def test_04_operator_precedence(self):
        """Multiplication takes precedence over addition."""
        self.assertEqual(calculate("2 + 3 * 4"), 14.0)

    def test_05_ctci_example(self):
        """CTCI example: 2*3 + 5/6*3 + 15."""
        self.assertAlmostEqual(calculate("2*3+5/6*3+15"), 23.5, places=4)

    def test_06_spaces_handling(self):
        """Expression with arbitrary spaces."""
        self.assertEqual(calculate("  10   - 3  * 2  "), 4.0)

    def test_07_left_to_right_division(self):
        """Consecutive division operations evaluated left-to-right (16 / 4 / 2 = 2.0)."""
        self.assertEqual(calculate("16 / 4 / 2"), 2.0)

    def test_08_zero_division(self):
        """Division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            calculate("10 / 0")


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.26 - Calculator\n{'='*75}")

    passed, failed, errors = 0, 0, 0

    for test in suite:
        test_name = test._testMethodName
        doc = (test._testMethodDoc or "").strip()
        desc = f"{test_name} -> {doc}" if doc else test_name

        result = unittest.TestResult()
        test.run(result)

        if result.wasSuccessful():
            print(f"  ✅ [PASS] {desc}")
            passed += 1
        elif result.failures:
            print(f"  ❌ [FAIL] {desc}")
            failed += 1
        elif result.errors:
            print(f"  ⚠️  [ERROR] {desc}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(f" EXECUTION SUMMARY:")
    print(f" Total Tests : {total}")
    print(f" Passed      : {passed} ✅")
    print(f" Failed      : {failed} ❌")
    print(f" Errors      : {errors} ⚠️")
    print(f" Success Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_informative_tests(TestCalculator)