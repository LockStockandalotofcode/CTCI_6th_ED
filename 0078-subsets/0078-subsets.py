class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # recursive top down DP
        # base case
        if not nums:
            return [[]]
        subsets = self.subsets(nums[: -1])
        last_element = nums[-1]
        # update the prev state, adding the last element
        results = subsets.copy()
        for subset in subsets:
            new_addition = subset.copy()
            new_addition.append(last_element)
            results.append(new_addition)

        return results