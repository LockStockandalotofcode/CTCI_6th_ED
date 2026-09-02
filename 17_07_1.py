import unittest

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i: str) -> str:
        if i not in self.parent:
            self.parent[i] = i
            return i
        # Path compression, flattening the tree, on each lookup
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: str, j: str) -> None:
        # union the two, if not already
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # keep lexicographically smaller name as root
            if root_i < root_j:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j

        return
 
def popular_names_dsu(names: dict[str, int], synonyms: list[tuple[str, str]]) -> dict[str, int]:
    uf = UnionFind()

    # process all synonyms and make edges
    for name1, name2 in synonyms:
        uf.union(name1, name2)

    # aggregate counts under canonical root
    result = {}
    # key: canonical root, value: number of babies with that name
    for name, count in names.items():
        root_name = uf.find(name)
        result[root_name] = result.get(root_name, 0) + count

    return result

# =====================================================================
# TEST SUITE
# =====================================================================
class TestBabyNames(unittest.TestCase):

    def test_01_empty_inputs(self):
        """Empty names dictionary and empty synonyms return empty result."""
        self.assertEqual(popular_names_dsu({}, []), {})

    def test_02_no_synonyms(self):
        """Names with no synonyms remain unchanged."""
        names = {"John": 15, "Chris": 10}
        self.assertEqual(popular_names_dsu(names, []), {"John": 15, "Chris": 10})

    def test_03_simple_synonym_pair(self):
        """Two names merged into one canonical root."""
        names = {"John": 15, "Jon": 10}
        synonyms = [("John", "Jon")]
        res = popular_names_dsu(names, synonyms)
        self.assertEqual(sum(res.values()), 25)
        self.assertEqual(len(res), 1)

    def test_04_transitive_synonym_chain(self):
        """Chain of synonyms: A=B and B=C merges A, B, C into total count."""
        names = {"Dan": 10, "Daniel": 20, "Danny": 5}
        synonyms = [("Dan", "Daniel"), ("Daniel", "Danny")]
        res = popular_names_dsu(names, synonyms)
        self.assertEqual(sum(res.values()), 35)
        self.assertEqual(len(res), 1)

    def test_05_cycle_in_synonyms(self):
        """Cycles in synonym pairings (A=B, B=C, C=A)."""
        names = {"A": 5, "B": 10, "C": 15}
        synonyms = [("A", "B"), ("B", "C"), ("C", "A")]
        res = popular_names_dsu(names, synonyms)
        self.assertEqual(sum(res.values()), 30)
        self.assertEqual(len(res), 1)

    def test_06_multiple_disconnected_components(self):
        """Multiple independent synonym clusters."""
        names = {"John": 10, "Jon": 5, "Mary": 20, "Mari": 8}
        synonyms = [("John", "Jon"), ("Mary", "Mari")]
        res = popular_names_dsu(names, synonyms)
        self.assertEqual(len(res), 2)
        self.assertEqual(sum(res.values()), 43)

    def test_07_synonym_name_missing_from_frequency_map(self):
        """Synonym list contains a name not present in the initial frequencies map."""
        names = {"John": 10}
        synonyms = [("John", "Johnny")]
        res = popular_names_dsu(names, synonyms)
        self.assertEqual(sum(res.values()), 10)
        self.assertEqual(len(res), 1)


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.7 - Baby Names\n{'='*75}")

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
    run_informative_tests(TestBabyNames)