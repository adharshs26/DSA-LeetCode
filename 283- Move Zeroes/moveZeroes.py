class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0  # Pointer for the position of the next non-zero element
    
            # Traverse the array with the `current` pointer
        for current in range(len(nums)):
            if nums[current] != 0:
                # Swap the current element with the element at the `non_zero` position
                nums[non_zero], nums[current] = nums[current], nums[non_zero]
                non_zero += 1


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)