
# implement the towers as stacks
class Tower:
    # its a stack at its core
    # with an identity, to let us distinguish between the source, destination, buffer
    # with a set of disks it holds
    def __init__(self, id:int=0):
        self.id = id
        self.elements = []

    def push(self, val) -> None:
        top = self._get_top()
        if top is not None and val > top:
            raise ValueError(f"Cannot a larger disk over a smaller disk")
        self.elements.append(val)
        return
    
    def _get_top(self) -> int | None:
        return self.elements[-1] if self.elements else None
    
    def pop(self) -> int | None:
        popped_element = self._get_top()
        self.elements.pop(-1)
        return popped_element

def towers_of_hanoi(n:int) -> tuple[Tower, Tower, Tower]:
    # initialise towers 
    source = Tower(id=1)
    for disk in range(n, 0, -1):
        source.push(disk)

    buffer = Tower(id=2)
    destination = Tower(id=3)

    # recursive solution
    def move_disks(count:int, source_tower:Tower, destination_tower:Tower, buffer_tower:Tower):
        # base case
        if count <= 0:
            return 

        # move top (n-1) disks from source to buffer
        move_disks(count-1, source_tower=source_tower, destination_tower=buffer_tower, buffer_tower=destination_tower)
        # move n th disk from source to destination
        destination_tower.push(source_tower.pop())
        # move the (n-1) disks from buffer to destination
        move_disks(count-1, source_tower=buffer_tower, destination_tower=destination_tower, buffer_tower=source_tower)
        return

    move_disks(n, source, destination, buffer)
    return source, buffer, destination

def run_towers_of_hanoi_tests():
    test_disks = [1, 3, 5, 8, 9, 20]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.6: TOWERS OF HANOI TESTS")
    print("=" * 60)

    for i, n in enumerate(test_disks, 1):
        expected_destination = list(range(n, 0, -1))

        try:
            source, buffer, destination = towers_of_hanoi(n)

            # 1. Destination must contain all disks in descending order (bottom to top)
            assert destination.elements == expected_destination, (
                f"Destination tower corrupted!\nExpected:"
                f" {expected_destination}\nGot:      {destination.elements}"
            )

            # 2. Source and buffer must end up empty
            assert (
                len(source.elements) == 0
            ), f"Source not empty! Leftover: {source.elements}"
            assert (
                len(buffer.elements) == 0
            ), f"Buffer not empty! Leftover: {buffer.elements}"

            print(
                f"  [PASS] Test {i:02d}: N={n} Disks Successfully Transferred"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: N={n} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_disks)}"
    )
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_towers_of_hanoi_tests()