class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch flag algo, only the working palette keeps shrinking towards the centre
        low, curr = 0, 0
        high = len(nums) - 1

        while curr <= high:
            if nums[curr] == 0:
                nums[low], nums[curr] = nums[curr], nums[low]
                low += 1
                curr += 1
            
            elif nums[curr] == 1:
                curr += 1
            
            else:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1
        
        return 