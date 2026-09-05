from collections import deque
import unittest

# queue strategy

def _get_min_head(q3: deque, q5: deque, q7: deque) -> tuple[int, int]:
    # finds minimum element from the 3 queues
    v3 = q3[0] if q3 else float("inf")
    v5 = q5[0] if q5 else float("inf")
    v7 = q7[0] if q7 else float("inf")

    min_val = min(v3, v5, v7)
    if min_val == v3:
        return min_val, 3
    elif min_val == v5:
        return min_val, 5
    elif min_val == v7:
        return min_val, 7

def get_kth_multiple(k: int) -> int:
    # time: O(k)
    # auxiliary space: O(k)
    if k < 1: 
        return 0

    q3, q5, q7 = deque([1]), deque(), deque()
    val = 0

    for _ in range(k):
        val, source_q = _get_min_head(q3, q5, q7)

        if source_q == 3:
            q3.popleft()
            q3.append(3 * val)
            q5.append(5 * val)
            q7.append(7 * val)
        
        elif source_q == 5:
            q5.popleft()
            q5.append(5 * val)
            q7.append(7 * val)
        
        if source_q == 7:
            q7.popleft()
            q7.append(7 * val)

    return val
        

# =====================================================================
# TEST SUITE
# =====================================================================
class TestKthMultiple(unittest.TestCase):

    def test_01_invalid_k_zero_or_negative(self):
        """Invalid k <= 0 returns 0."""
        self.assertEqual(get_kth_multiple(0), 0)
        self.assertEqual(get_kth_multiple(-5), 0)

    def test_02_first_element(self):
        """k = 1 returns the base element 1."""
        self.assertEqual(get_kth_multiple(1), 1)

    def test_03_first_few_multiples(self):
        """First 7 numbers in sequence: 1, 3, 5, 7, 9, 15, 21."""
        expected = [1, 3, 5, 7, 9, 15, 21]
        results = [get_kth_multiple(i) for i in range(1, 8)]
        self.assertEqual(results, expected)

    def test_04_thirteenth_multiple(self):
        """13th multiple in sequence should be 63."""
        self.assertEqual(get_kth_multiple(13), 63)

    def test_05_fifteenth_multiple(self):
        """15th multiple in sequence should be 81."""
        self.assertEqual(get_kth_multiple(15), 81)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.9 - Kth Multiple\n{'='*75}")

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
            fail_msg = result.failures[0][1].strip().split("\n")[-1]
            print(f"  ❌ [FAIL] {desc} | {fail_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().split("\n")[-1]
            print(f"  ⚠️  [ERROR] {desc} | {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(
        f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%"
    )
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestKthMultiple)