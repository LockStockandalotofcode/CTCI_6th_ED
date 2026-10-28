class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # bucket sort
        counts_dict = {}
        for num in nums:
            if num in counts_dict:
                counts_dict[num] += 1
            else:
                counts_dict[num] = 1

        freq = [[] for _ in range(len(nums) + 1)]

        # populate freq table, with all elements of i freq sitting at i index
        for num, i in counts_dict.items():
            freq[i].append(num)

        result = []
        for index in range(len(nums), 0, -1):
            for number in freq[index]:
                result.append(number)
                if len(result) == k:
                    return result
        
        return result

        