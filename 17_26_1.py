from collections import defaultdict
import unittest

def _build_inverted_indices_map(documents: dict[int, list[int]]) -> dict[int, list[int]]:
    # helper map each element to list of documents it is present inside
    inverted_map = defaultdict(list)
    for doc_id, words in documents.items():
        for word in words:
            inverted_map[word].append(doc_id)

    return inverted_map

def sparse_similarity(docs: dict[int, list[int]]) -> dict[tuple[int, int], float]:
    # inverted index intersection Counting
    # Time: O(P + E), P: matching document pairs, E: total elements
    # Space: O(P + E)

    if not docs:
        return {}

    inverted_map = _build_inverted_indices_map(docs)
    intersections: dict[tuple[int, int], int] = defaultdict(int)
    # value stores number of intersections between any two docs
    # docs doc_i, doc_j are stored in sorted fashion to avoid duplicates

    # accumulate pairwise intersections for docs
    for word, doc_ids in inverted_map.items():
        doc_ids.sort()
        for i in range(len(doc_ids)):
            for j in range(i + 1, len(doc_ids)):
                # i from start to end, j from i + 1 to end, in the subsequent section
                pair = (doc_ids[i], doc_ids[j])
                intersections[pair] += 1

    # Compute Jaccard Similarities
    similarities: dict[tuple[int, int], float] = {}
    for (d1, d2), intersection_count in intersections.items():
        size1 = len(docs[d1])
        size2 = len(docs[d2])
        union_count = size1 + size2 - intersection_count

        if intersection_count > 0:
            similarities[(d1, d2)] = round(intersection_count / union_count, 4)

    return similarities

# =====================================================================
# TEST SUITE
# =====================================================================
class TestSparseSimilarity(unittest.TestCase):

    def test_01_empty_documents(self):
        """Empty documents map returns empty similarity results."""
        self.assertEqual(sparse_similarity({}), {})

    def test_02_no_overlapping_words(self):
        """Documents with zero overlapping words produce no result entries."""
        docs = {1: [1, 2, 3], 2: [4, 5, 6]}
        self.assertEqual(sparse_similarity(docs), {})

    def test_03_identical_documents(self):
        """Identical document sets return similarity score 1.0."""
        docs = {1: [10, 20], 2: [10, 20]}
        self.assertEqual(sparse_similarity(docs), {(1, 2): 1.0})

    def test_04_partial_overlap_jaccard(self):
        """Calculates accurate Jaccard similarity for overlapping sets."""
        docs = {
            13: [14, 15, 100, 9, 3],
            16: [32, 1, 9, 3, 5],
            19: [15, 29, 2, 6, 8, 7],
            24: [7, 10]
        }
        res = sparse_similarity(docs)
        self.assertIn((13, 16), res)
        # Intersection = {9, 3} (2), Union = 8 -> 2/8 = 0.25
        self.assertEqual(res[(13, 16)], 0.25)
        # Intersection = {15} (1), Union = 10 -> 1/10 = 0.1
        self.assertEqual(res[(13, 19)], 0.1)

    def test_05_sparse_pair_filtering(self):
        """Filters out document pairs with zero similarity."""
        docs = {1: [1, 2], 2: [3, 4], 3: [2, 3]}
        res = sparse_similarity(docs)
        self.assertNotIn((1, 2), res)
        self.assertIn((1, 3), res)
        self.assertIn((2, 3), res)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.26 - Sparse Similarity\n{'='*75}")

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
    run_tests(TestSparseSimilarity)