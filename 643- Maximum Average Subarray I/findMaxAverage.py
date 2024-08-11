class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
    
        # Initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
    
        # Slide the window from start to end
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
    
        # Return the maximum average
        return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums,k))