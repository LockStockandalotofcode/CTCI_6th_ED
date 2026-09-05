import random
from typing import Optional
import unittest

def _get_random_index(lower_bound: int, upper_bound: int) -> int:
     #returns random nmber between lower and upper, both inclusive
    return random.randint(lower_bound, upper_bound)

# ITERATIVE
def shuffle_deck_i(cards: list[int]) -> list[int]:
    # Iterative In-place fisher yates shuffle
    #  Time: O(N)
    # Space: O(1)

    shuffled = cards.copy()
    for i in range(len(cards)):
        # traverseing forwards
        # swapping with elements from latter unshuffled section
        k = _get_random_index(0, i)
        # swap curr element with element at k
        # cards[i], cards[k] = cards[k], cards[i]
        shuffled[i], shuffled[k] = shuffled[k], shuffled[i]

    return shuffled

# RECURSIVE
def shuffle_deck(cards: list[int], n: Optional[int] = None) -> list[int]:
    # recursive process
    # Time: O(N)
    # Space: O(N) due to recursive call stack

    if n is None:
        n = len(cards)

    if n <= 1:
        # base case, going from executing top n-1 to top 1
        return cards

    shuffled = cards.copy()
    # inductively shuffle top n-1 elements
    shuffle_deck(shuffled, n-1)

    # pick random index from unshuffled window - (0 and n -1)
    k = _get_random_index(0, n-1)
    # swap with element at index n-1 
    shuffled[n-1], shuffled[k] = shuffled[k], shuffled[n-1],
    return shuffled




# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def shuffle_deck(cards: list[int]) -> list[int]:
#     """Shuffles an array of cards in-place using Fisher-Yates algorithm and returns it."""
#     shuffled = list(cards)
#     for i in range(len(shuffled) - 1, 0, -1):
#         j = random.randint(0, i)
#         shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
#     return shuffled


# =====================================================================
# TEST SUITE
# =====================================================================
class TestShuffle(unittest.TestCase):

    def test_01_empty_list(self):
        """Empty input list returns empty list."""
        self.assertEqual(shuffle_deck([]), [])

    def test_02_single_element(self):
        """Single element list remains unchanged."""
        self.assertEqual(shuffle_deck([42]), [42])

    def test_03_preserves_elements_multiset(self):
        """Shuffled list retains exact same elements and frequency as original."""
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffled = shuffle_deck(cards)
        self.assertEqual(sorted(cards), sorted(shuffled))

    def test_04_length_preservation(self):
        """Output length matches original input length."""
        cards = list(range(52))
        shuffled = shuffle_deck(cards)
        self.assertEqual(len(shuffled), 52)

    def test_05_non_mutating_original_input(self):
        """Original list remains unmodified when function returns new shuffled list."""
        original = [10, 20, 30, 40]
        original_copy = list(original)
        shuffle_deck(original)
        self.assertEqual(original, original_copy)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.2 - Shuffle\n{'='*75}")

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
    print(f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestShuffle)