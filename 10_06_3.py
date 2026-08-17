import heapq
import tempfile
import os

def mergesort(arr: list[str]) -> list[str]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    return merge(left, right)

def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    i = j = 0
    final_list = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            final_list.append(arr1[i])
            i += 1
        else:
            final_list.append(arr2[j])
            j += 1

    # append any leftover portion from i and j
    final_list.extend(arr1[i:])
    final_list.extend(arr2[j:])

    return final_list

def sort_big_file(input_file_path: str, output_file_path: str, chunk_file_size: int = 1_000_000) -> None:
    temp_files = []
    # PHASE 1 - split into chunks and in-memory sort for the chunks
    with open(input_file_path, 'r') as infile:
        while True:
            # read limited number of lines into RAM
            lines = [infile.readline().strip() for _ in range(chunk_file_size)]
            lines = [line for line in lines if line] # filter EOF end of file character
            if not lines:
                break

            lines = mergesort(lines) # quicksort implementation above - in-memory using RAM as auxilliary space

            # save this as a temporary sorted chunk on the hard drive
            temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
            temp_file.write('\n'.join(lines) + '\n')
            temp_file.flush()
            temp_file.seek(0) # reset pointer to beginning for reading later
            temp_files.append(temp_file)

    # PHASE 2 - K-way Merge using Min-Heap
    min_heap = []

    # starting at 1st line across all chunks, appending into the heap
    for file_idx, temp_file in enumerate(temp_files):
        line = temp_file.readline().strip()
        if line:
            heapq.heappush(min_heap, (line, file_idx))

    # stream sorted output to disk
    with open(output_file_path, 'w') as outfile:
        while min_heap:
            smallest_str, file_idx = heapq.heappop(min_heap)
            outfile.write(smallest_str + '\n')

            # replenish heap from the file that supplied the popped string
            next_line = temp_files[file_idx].readline().strip()
            if next_line:
                heapq.heappush(min_heap, (next_line, file_idx))

    # Close and remove temp files
    for temp_file in temp_files:
        temp_file.close()
    return

def run_sort_big_file_tests():
    test_datasets = [
        ([], "Empty input file"),
        (["single_entry"], "Single line file"),
        (["banana", "apple", "cherry", "date"], "Unsorted words"),
        (["b", "a", "b", "a", "c", "b"], "File with heavy duplicates"),
        ([f"line_{i:04d}" for i in range(200, 0, -1)], "Reverse sorted large dataset"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.6: SORT BIG FILE TESTS")
    print("=" * 60)

    for i, (lines, desc) in enumerate(test_datasets, 1):
        with tempfile.NamedTemporaryFile("w+", delete=False) as in_f, \
             tempfile.NamedTemporaryFile("w+", delete=False) as out_f:

            in_path, out_path = in_f.name, out_f.name

            try:
                for l in lines:
                    in_f.write(l + "\n")
                in_f.flush()

                sort_big_file(in_path, out_path)

                with open(out_path, "r") as f:
                    output_lines = [line.rstrip("\r\n") for line in f.readlines()]

                expected = sorted(lines)
                assert output_lines == expected, (
                    f"Sorting mismatch.\nExpected first 5: {expected[:5]}\nGot first 5: {output_lines[:5]}"
                )
                print(f"  [PASS] Test {i:02d}: {desc}")
                passed += 1
            except Exception as e:
                print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
                failed += 1
            finally:
                if os.path.exists(in_path):
                    os.remove(in_path)
                if os.path.exists(out_path):
                    os.remove(out_path)

    print("-" * 60)
    print(f"10.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_datasets)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_sort_big_file_tests()