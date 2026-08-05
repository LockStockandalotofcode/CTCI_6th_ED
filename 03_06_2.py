# Modified Queue based on LinkedList Data structure
# separate linked list for dog, and cat; with enqueueing timestamps for tracking the first out of both types of animals

# LinkedList Implementation
# class ListNode

class DogListNode:
    def __init__(self, data:str = "", serial_no: int = 0, next = None):
        self.data = data
        self.serial_no = serial_no
        self.next = next

class CatListNode:
    def __init__(self, data:str = "", serial_no: int = 0, next = None):
        self.data = data
        self.serial_no = serial_no
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.dog_dummy_head = DogListNode(data="Dog Dummy", serial_no=0)
        self.dog_tail = self.dog_dummy_head

        self.cat_dummy_head = CatListNode(data="Cat Dummy", serial_no=0)
        self.cat_tail = self.cat_dummy_head
        self.last_sr_no = 0

    def enqueue(self, animal_data: str, animal_type: str) -> None:
        if animal_type.lower() == "dog":
            self._enqueue_dog(animal_data)
        elif animal_type.lower() == "cat":
            self._enqueue_cat(animal_data)
        return

    def _enqueue_dog(self, animal_data: str) -> None:
        # we need the serial no of the last animal
        new_dog_sr_no = self.last_sr_no + 1

        # then create a dog node and append it to the linked list with the correct serial no
        new_dog = DogListNode(data=animal_data, serial_no=new_dog_sr_no)
        self.dog_tail.next = new_dog
        self.dog_tail = self.dog_tail.next
        self.last_sr_no += 1
        return

    def _enqueue_cat(self, animal_data: str) -> None:
        # we need the serial no of the last animal 
        new_cat_sr_no = self.last_sr_no + 1
        # then create a dog node and append it to the linked list with the correct serial no
        new_cat = CatListNode(data=animal_data, serial_no=new_cat_sr_no)
        self.cat_tail.next = new_cat
        self.cat_tail = self.cat_tail.next
        self.last_sr_no += 1
        return

    def dequeueAny(self) -> DogListNode | CatListNode | None:
        # compare the order of head nodes in Dog Linked List and Cat linked list
        # call the method for whichever's the least serial no
        top_dog = self.dog_dummy_head.next
        top_cat = self.cat_dummy_head.next

        # to attribute when a either shelter (queue) is empty

        if top_dog is None and top_cat is None:
            return ""
        if top_dog is None:
            return self.dequeueCat()
        if top_cat is None:
            return self.dequeueDog()
        
        if top_dog.serial_no < top_cat.serial_no:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self) -> DogListNode | None:
        # edge case 1: no dog in the shelter 
        if self.dog_dummy_head.next is None:
            return "" 

        # pop the first animal
        result = self.dog_dummy_head.next
        # unlink this node
        self.dog_dummy_head.next = self.dog_dummy_head.next.next

        # edge case 2: only 1 dog in the shelter, popped dog is the tail dog, so the tail node requires repair
        if result == self.dog_tail:
            self.dog_tail = self.dog_dummy_head

        return result.data

    def dequeueCat(self) -> CatListNode | None:
        # edge case 1: no dog in the shelter 
        if self.cat_dummy_head.next is None:
            return "" 

        # pop the first animal
        result = self.cat_dummy_head.next
        # unlink this node
        self.cat_dummy_head.next = self.cat_dummy_head.next.next

        # edge case 2: only 1 dog in the shelter, popped dog is the tail dog, so the tail node requires repair
        if result == self.cat_tail:
            self.cat_tail = self.cat_dummy_head

        return result.data

def run_animal_shelter_tests():
    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 3.6: ANIMAL SHELTER (TWO-QUEUE) TESTS")
    print("=" * 60)

    # Test 1: Interleaved Enqueue and O(1) DequeueAny FIFO Ordering
    try:
        shelter = AnimalShelter()
        shelter.enqueue("Rex", "dog")  # sr: 1
        shelter.enqueue("Whiskers", "cat")  # sr: 2
        shelter.enqueue("Buddy", "dog")  # sr: 3

        a1 = shelter.dequeueAny()
        a2 = shelter.dequeueAny()

        assert a1 == "Rex", f"Expected 'Rex', got '{a1}'"
        assert a2 == "Whiskers", f"Expected 'Whiskers', got '{a2}'"

        print("  [PASS] Test 01: Interleaved Enqueue & FIFO DequeueAny")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 01 -> ERROR: {e}")
        failed += 1

    # Test 2: Specific Species Dequeue (Bypassing Older Animals of Other Species)
    try:
        shelter = AnimalShelter()
        shelter.enqueue("Dog1", "dog")  # sr: 1
        shelter.enqueue("Cat1", "cat")  # sr: 2
        shelter.enqueue("Cat2", "cat")  # sr: 3
        shelter.enqueue("Dog2", "dog")  # sr: 4

        cat = shelter.dequeueCat()
        assert cat == "Cat1", f"Expected 'Cat1', got '{cat}'"

        dog = shelter.dequeueDog()
        assert dog == "Dog1", f"Expected 'Dog1', got '{dog}'"

        next_any = shelter.dequeueAny()
        assert (
            next_any == "Cat2"
        ), f"Expected 'Cat2' after specific dequeues, got '{next_any}'"

        print("  [PASS] Test 02: Species-Specific Filtering")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 02 -> ERROR: {e}")
        failed += 1

    # Test 3: DequeueAny When One Queue Is Completely Empty
    try:
        shelter = AnimalShelter()
        shelter.enqueue("Rover", "dog")  # Only dogs in shelter
        shelter.enqueue("Spot", "dog")

        # DequeueAny should fall back to dequeueDog safely without AttributeError
        a1 = shelter.dequeueAny()
        assert a1 == "Rover", f"Expected 'Rover', got '{a1}'"

        print(
            "  [PASS] Test 03: DequeueAny Safety When One Species Queue Is Empty"
        )
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 03 -> ERROR: {e}")
        failed += 1

    # Test 4: Tail Repair and Empty Shelter Boundaries
    try:
        shelter = AnimalShelter()
        shelter.enqueue("SoloCat", "cat")

        assert (
            shelter.dequeueDog() == ""
        ), "dequeueDog on cat-only shelter should return empty string!"
        assert (
            shelter.dequeueCat() == "SoloCat"
        ), "Failed to dequeue existing cat!"
        assert (
            shelter.dequeueAny() == ""
        ), "dequeueAny on empty shelter should return empty string!"

        # Ensure tail pointer was repaired and can take new items
        shelter.enqueue("NewDog", "dog")
        assert (
            shelter.dequeueAny() == "NewDog"
        ), "Failed to dequeue from repaired tail queue!"

        print("  [PASS] Test 04: Tail Repair and Empty Shelter Boundaries")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 04 -> ERROR: {e}")
        failed += 1

    print("-" * 60)
    print(f"3.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total: 4")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_animal_shelter_tests()