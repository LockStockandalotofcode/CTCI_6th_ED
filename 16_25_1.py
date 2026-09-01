import unittest

class Node:
    def __init__(self, key = 0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Size must be greater than 0.")
        self.size = 0
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        # breakpoint()
        # instead of single element hashmap at each node, use one hashmap for entire LRUCache

    def _remove_lru(self):
        lru = self.head.next
        self.head.next = lru.next
        lru.next.prev = self.head

        del self.cache[lru.key]
        return
    
    def _update_mru(self, new_node):
        # unlink from previous position
        new_node.next.prev = new_node.prev
        new_node.prev.next = new_node.next
        # append at the very tail

        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node

        self.tail.prev = new_node
        new_node.next = self.tail
        return

    def put(self, key, val):
        if self.size == self.cap:
            self._remove_lru()
        new_addition = Node(key, val)
        last_node = self.tail.prev
        last_node.next = new_addition
        new_addition.prev = last_node
        new_addition.next = self.tail
        self.tail.prev = new_addition

        self.size += 1

        self.cache[key] = val
        return

    def get(self, key):
        ptr_node = self.head.next
        if self.size == 0 or key not in self.cache:
            return -1
        while ptr_node != self.tail:
            if ptr_node.key == key:
                break
            ptr_node = ptr_node.next
        self._update_mru(ptr_node)
        return self.cache[key]


# =====================================================================
# TEST SUITE
# =====================================================================
class TestLRUCache(unittest.TestCase):

    def test_01_invalid_capacity(self):
        """Constructing cache with capacity <= 0 raises ValueError."""
        with self.assertRaises(ValueError):
            LRUCache(0)
        with self.assertRaises(ValueError):
            LRUCache(-5)

    def test_02_get_non_existent_key(self):
        """Querying missing key returns -1."""
        cache = LRUCache(2)
        self.assertEqual(cache.get(1), -1)

    def test_03_basic_put_and_get(self):
        """Basic put and retrieval operations."""
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 20)

    def test_04_eviction_policy(self):
        """Exceeding capacity evicts the least recently used key."""
        cache = LRUCache(2)
        cache.put(1, 100)
        cache.put(2, 200)
        cache.put(3, 300)  # Evicts key 1

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 200)
        self.assertEqual(cache.get(3), 300)

    def test_05_get_updates_recently_used(self):
        """Reading a key marks it as MRU, preventing its eviction."""
        cache = LRUCache(2)
        cache.put(1, 100)
        cache.put(2, 200)

        # Touch key 1 so 1 becomes MRU and 2 becomes LRU
        self.assertEqual(cache.get(1), 100)

        cache.put(3, 300)  # Should evict key 2

        self.assertEqual(cache.get(1), 100)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 300)

    def test_06_update_existing_key(self):
        """Updating existing key updates value without triggering eviction."""
        cache = LRUCache(2)
        cache.put(1, 100)
        cache.put(2, 200)
        cache.put(1, 150)  # Update key 1

        self.assertEqual(cache.get(1), 150)
        self.assertEqual(cache.get(2), 200)

    def test_07_capacity_one(self):
        """Cache of capacity 1 works correctly."""
        cache = LRUCache(1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)

        cache.put(2, 20)  # Evicts key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 20)


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.25 - LRU Cache\n{'='*75}")

    passed, failed, errors = 0, 0, 0
    failures_details = []

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
            for _, err in result.failures:
                failures_details.append((test_name, doc, err))
        elif result.errors:
            print(f"  ⚠️  [ERROR] {desc}")
            errors += 1
            for _, err in result.errors:
                failures_details.append((test_name, doc, err))

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

    if failures_details:
        print(f"{'!'*75}\n DETAILED FAILURE / ERROR REPORT:\n{'!'*75}")
        for name, doc, err in failures_details:
            print(f"• Test: {name}\n  Description: {doc}\n  Traceback:\n{err}\n{'-'*75}")


if __name__ == "__main__":
    run_informative_tests(TestLRUCache)