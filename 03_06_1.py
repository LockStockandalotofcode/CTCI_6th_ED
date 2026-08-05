# Modified Queue based on LinkedList Data structure

# enqueue operation: changes the tail
# dequeue operation: either affects the top (dequeueAny)
# dequeue cat or dog removes the first node of that kind

# LinkedList Implementation
class ListNode:
    def __init__(
            self, 
            animal_data: str = "", 
            animal_type: str = "", 
            next = None
            ):
        self.animal_data = animal_data
        self.animal_type = animal_type
        self.next = next

class AnimalShelter:
    def __init__(self):
        # Sentinel dummy node simplifies edge cases (like empty list, popping first element)
        self.dummy_head = ListNode(animal_data="DUMMY", animal_type="dummy")
        self.tail = self.dummy_head
        # its not like the user would send an input of these nodes, the time this class is created/initialised
        # head node is one before actual head
        # tail node is the actual tail node, which is modified with every enqueue an dequeue operation

    def enqueue(self, animal_data:str, animal_type:str) -> None:
        new_node = ListNode(animal_data=str(animal_data), animal_type=animal_type)
        self.tail.next = new_node
        self.tail = self.tail.next

    def dequeueAny(self) -> str:
        if self.dummy_head.next is None:
            return "" # shelter is empty

        target = self.dummy_head.next
        self.dummy_head.next = target.next
        # we keep the dummy_head where it is, since it points to the actual head
        # we change its next pointer

        # if we popped the very last element, for the edge case of tail node
        if target == self.tail:
            self.tail = self.dummy_head

        return target.animal_data

    def _dequeue_by_type(self, target_type: str) -> str:
        # find the first dog from start
        prev = self.dummy_head
        curr = self.dummy_head.next

        while curr and curr.animal_type != target_type :
            prev = curr
            curr = curr.next

        if curr is None: 
            return "" # no animal in the shelter of this type

        # if head_node exists after having survived above loop, that means there's a dog in the animal shelter
        # unlink this node, i.e. remove this node
        prev.next = curr.next
        # if its the tail node, repair the tail node
        if curr == self.tail:
            self.tail = prev

        return curr.animal_data

    def dequeueDog(self) -> str:
        return self._dequeue_by_type(target_type="dog")
    def dequeueCat(self) -> str:
        return self._dequeue_by_type(target_type="cat")

def run_animal_shelter_tests():
    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 3.6: ANIMAL SHELTER TESTS")
    print("=" * 60)

    # Test 1: Basic Enqueue and DequeueAny (FIFO Order)
    try:
        shelter = AnimalShelter()
        shelter.enqueue("Rex", "dog")
        shelter.enqueue("Whiskers", "cat")
        shelter.enqueue("Buddy", "dog")

        a1 = shelter.dequeueAny()
        a2 = shelter.dequeueAny()

        assert a1 == "Rex", f"Expected 'Rex', got '{a1}'"
        assert a2 == "Whiskers", f"Expected 'Whiskers', got '{a2}'"

        print("  [PASS] Test 01: Basic FIFO DequeueAny")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 01 -> ERROR: {e}")
        failed += 1

    # Test 2: Specific Species Dequeue (Filter Dogs / Cats)
    try:
        shelter = AnimalShelter()
        shelter.enqueue("Dog1", "dog")
        shelter.enqueue("Cat1", "cat")
        shelter.enqueue("Cat2", "cat")
        shelter.enqueue("Dog2", "dog")

        cat = shelter.dequeueCat()
        assert cat == "Cat1", f"Expected 'Cat1', got '{cat}'"

        dog = shelter.dequeueDog()
        assert dog == "Dog1", f"Expected 'Dog1', got '{dog}'"

        next_any = shelter.dequeueAny()
        assert (
            next_any == "Cat2"
        ), f"Expected 'Cat2' after specific dequeues, got '{next_any}'"

        print("  [PASS] Test 02: Species-Specific Dequeue (dequeueDog / dequeueCat)")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 02 -> ERROR: {e}")
        failed += 1

    # Test 3: Dequeuing Tail Node (Tail Pointer Synchronization)
    try:
        shelter = AnimalShelter()
        shelter.enqueue("Cat1", "cat")
        shelter.enqueue("Dog1", "dog")  # Tail node is Dog1

        # Dequeue the tail node specifically
        d = shelter.dequeueDog()
        assert d == "Dog1", f"Expected 'Dog1', got '{d}'"

        # Now enqueue another animal to ensure tail pointer isn't corrupt
        shelter.enqueue("Cat2", "cat")
        remaining = shelter.dequeueAny()
        assert (
            remaining == "Cat1"
        ), f"Expected 'Cat1' from front, got '{remaining}'"

        last = shelter.dequeueAny()
        assert (
            last == "Cat2"
        ), f"Expected 'Cat2' appended to repaired tail, got '{last}'"

        print("  [PASS] Test 03: Tail Node Removal & Tail Pointer Synchronization")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 03 -> ERROR: {e}")
        failed += 1

    # Test 4: Empty Shelter & Missing Species Edge Cases
    try:
        shelter = AnimalShelter()
        shelter.enqueue("SoloCat", "cat")

        assert (
            shelter.dequeueDog() == ""
        ), "dequeueDog on cat-only shelter should return empty string/None!"
        assert (
            shelter.dequeueCat() == "SoloCat"
        ), "Failed to dequeue existing cat!"
        assert (
            shelter.dequeueAny() == ""
        ), "dequeueAny on empty shelter should return empty string/None!"

        print("  [PASS] Test 04: Empty Shelter & Missing Species Safety")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 04 -> ERROR: {e}")
        failed += 1

    print("-" * 60)
    print(f"3.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total: 4")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_animal_shelter_tests()