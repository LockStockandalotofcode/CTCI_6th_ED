class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if not nums:
            return None
        max_freq_element = nums[0]
        freq = 1

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr == max_freq_element:
                freq += 1
            else:
                freq -= 1
                if freq == 0:
                    max_freq_element = curr
                    freq = 1

        return max_freq_element