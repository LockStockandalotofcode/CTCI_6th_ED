import unittest

# STATICMETHODS
# dont require
    #  creating class instance before calling functions
    #  recieve an implicit first argument, cls or self


# most algos uses exponential doubling
# with overshoot resetting, whenever not dealing with exact powers of 2

class Operations:
    
    @staticmethod
    def _negate(a: int) -> int:
        # helper to negate a number
        # time: O(log_2 N)
        if a == 0:
            return 0

        direction = -1 if a > 0 else 1
        delta = direction
        neg = 0

        while a != 0:
            # Check if doubling delta exceeds remaining amount (overshoots)
            # if adding delta overshoots 0, delta resets back to direction (base amount 1 or -1)
            different_signs = (a + delta > 0) if a < 0 else (a + delta < 0)
            # holds true if delta overshoot the sum
            if a + delta != 0 and different_signs:
                delta = direction

            neg += delta
            a += delta
            delta += delta 

        return neg

    @staticmethod
    def _abs(a: int) -> int:
        return Operations._negate(a) if a < 0 else a

    @staticmethod
    def subtract(a: int, b: int) -> int:
        # time: O(log_2 b)
        # b is the smaller of the two
        # space: O(1)
        return a +  Operations._negate(b)

    @staticmethod
    def multiply(a: int, b: int) -> int:
        # using exponential doubling addition
        # adding doubling the numbers till the nearest 2-power
        # time : O(log b)
        # auxiliary space: O(1)

        if a == 0 or b == 0:
            return 0
            
        if abs(a) < abs(b):
            return  Operations.multiply(b,a) # Optimise by iterating for smaller number(number of times)

        abs_a, abs_b =  Operations._abs(a),  Operations._abs(b)
        result = 0
        current_sum = abs_a
        count = 1

        while count <= abs_b:
            result = result + current_sum
            abs_b =  Operations.subtract(abs_b, count)

            # Exponential doubling of step sum
            current_sum += current_sum
            count += count

            if count > abs_b:
                # reset step pointer for remaining fraction, in case of overshoot
                current_sum = abs_a
                count = 1

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return  Operations._negate(result)

        return result

    @staticmethod
    def divide(a: int, b: int) -> int:
        # double shift addition
        # time: O(log_2 (a/b))
        # space: O(1)

        if b == 0:
            raise ZeroDivisionError("Division by zero")

        abs_a, abs_b =  Operations._abs(a),  Operations._abs(b)
        if abs_a < abs_b:
            return 0

        quotient = 0
        product = abs_b
        count = 1

        # Find largest power of 2 chunk
        while (product + product) <= abs_a:
            product += product
            count += count

        quotient += count
        quotient +=  Operations.divide( Operations.subtract(abs_a, product), abs_b)

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return  Operations._negate(quotient)

        return quotient


# =====================================================================
# TEST SUITE
# =====================================================================
class TestOperations(unittest.TestCase):

    def test_01_subtract_positive_and_negative(self):
        """Subtraction across positive, negative, and zero values."""
        self.assertEqual(Operations.subtract(10, 4), 6)
        self.assertEqual(Operations.subtract(4, 10), -6)
        self.assertEqual(Operations.subtract(0, 5), -5)
        self.assertEqual(Operations.subtract(-5, -3), -2)

    def test_02_multiply_variations(self):
        """Multiplication with positive, negative, and zero operands."""
        self.assertEqual(Operations.multiply(3, 4), 12)
        self.assertEqual(Operations.multiply(-3, 4), -12)
        self.assertEqual(Operations.multiply(-3, -4), 12)
        self.assertEqual(Operations.multiply(0, 99), 0)

    def test_03_divide_exact_and_truncating(self):
        """Division with exact and non-exact quotients."""
        self.assertEqual(Operations.divide(12, 3), 4)
        self.assertEqual(Operations.divide(10, 3), 3)
        self.assertEqual(Operations.divide(-10, 3), -3)
        self.assertEqual(Operations.divide(5, 10), 0)

    def test_04_divide_by_zero_exception(self):
        """Division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            Operations.divide(10, 0)


# =====================================================================
# CONCISE SINGLE-LINE TEST RUNNER
# =====================================================================
def run_tests(test_class, title: str):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: {title}\n{'='*75}")

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
            err_msg = result.failures[0][1].strip().splitlines()[-1]
            print(f"  ❌ [FAIL] {desc} | Details: {err_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().splitlines()[-1]
            print(f"  ⚠️  [ERROR] {desc} | Details: {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"{'-'*75}")
    print(f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestOperations, "CTCI 16.9 - Operations")