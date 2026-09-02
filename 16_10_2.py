import unittest

# Prefix Sum Sweep
# O(P + Y) Optimal time complexity
# O(Y) auxilliary space complexity

def max_alive_year(people: list[tuple[int, int]], min_year: int = 1900, max_year: int = 2000) -> int:
    if not people:
        return min_year

    num_years = (max_year - min_year + 1)
    # one extraslot handles deaths in max_year
    deltas = [0] * (num_years + 1)
    # breakpoint()
    for b_year, d_year in people:
        # ignore people outside the given window 
        if d_year < min_year or b_year > max_year:
            continue

        b = max(min_year, b_year)
        d = min(d_year, max_year)

        deltas[b - min_year] += 1
        deltas[d - min_year + 1] -= 1
        
    max_alive = 0
    max_alive_yr = min_year
    currently_alive = 0
    
    # PREFIX SUM SWEEP
    for i in range(num_years):
        currently_alive += deltas[i]
        if currently_alive > max_alive:
            max_alive = currently_alive
            max_alive_yr = min_year + i

    return max_alive_yr


# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def max_alive_year(people: list[tuple[int, int]], min_year: int = 1900, max_year: int = 2000) -> int:
#     """Finds the earliest year with the maximum number of living people.
#     People are alive in all years between birth and death, inclusive.
#     """
#     if not people:
#         return min_year

#     year_deltas = [0] * (max_year - min_year + 2)

#     for birth, death in people:
#         if birth > max_year or death < min_year:
#             continue
#         b = max(birth, min_year)
#         d = min(death, max_year)
#         year_deltas[b - min_year] += 1
#         year_deltas[d - min_year + 1] -= 1

#     max_alive = 0
#     max_year_result = min_year
#     currently_alive = 0

#     for yr in range(max_year - min_year + 1):
#         currently_alive += year_deltas[yr]
#         if currently_alive > max_alive:
#             max_alive = currently_alive
#             max_year_result = min_year + yr

#     return max_year_result


# =====================================================================
# TEST SUITE
# =====================================================================
class TestLivingPeople(unittest.TestCase):

    def test_01_empty_people_list(self):
        """Empty list should default to start of range (min_year)."""
        self.assertEqual(max_alive_year([], 1900, 2000), 1900)

    def test_02_single_person(self):
        """Single person returns their birth year."""
        self.assertEqual(max_alive_year([(1920, 1980)], 1900, 2000), 1920)

    def test_03_same_birth_and_death_year(self):
        """Person born and died in the exact same year."""
        self.assertEqual(max_alive_year([(1950, 1950)], 1900, 2000), 1950)

    def test_04_no_overlapping_lifespans(self):
        """Non-overlapping lifespans should return the birth year of the earliest person."""
        people = [(1905, 1910), (1920, 1930), (1940, 1950)]
        self.assertEqual(max_alive_year(people, 1900, 2000), 1905)

    def test_05_clear_population_peak(self):
        """Clear peak where multiple people overlap in 1940."""
        people = [
            (1900, 1950),
            (1920, 1945),
            (1935, 1940),
            (1940, 1970)
        ]
        self.assertEqual(max_alive_year(people, 1900, 2000), 1940)

    def test_06_tie_in_max_population(self):
        """Tie in maximum living count should return the earliest year."""
        # 1910 has 2 people (1900-1910, 1910-1920)
        # 1930 has 2 people (1925-1935, 1930-1940)
        people = [(1900, 1910), (1910, 1920), (1925, 1935), (1930, 1940)]
        self.assertEqual(max_alive_year(people, 1900, 2000), 1910)

    def test_07_boundary_years(self):
        """Lifespans on exact min and max boundaries (1900 and 2000)."""
        people = [(1900, 1900), (2000, 2000), (2000, 2000)]
        self.assertEqual(max_alive_year(people, 1900, 2000), 2000)

    def test_08_out_of_bounds_lifespans(self):
        """Lifespans completely outside 1900-2000 window should be ignored."""
        people = [(1800, 1850), (2050, 2100)]
        self.assertEqual(max_alive_year(people, 1900, 2000), 1900)


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.10 - Living People\n{'='*75}")

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
    run_informative_tests(TestLivingPeople)