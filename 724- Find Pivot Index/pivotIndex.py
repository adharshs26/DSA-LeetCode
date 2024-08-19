class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total - nums[i]

            if right_total == left_total:
                return i
            
            left_total += nums[i]
        
        return -1
        

nums = [1,7,3,6,5,6]
print(Solution().pivotIndex(nums))