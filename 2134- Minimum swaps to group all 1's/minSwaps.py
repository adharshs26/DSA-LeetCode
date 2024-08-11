
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        l = 0
        window_ones = max_window_ones = 0
        for r in range (2 * n):
            if nums[r % n]:
                window_ones += 1
            if r - l + 1 > total_ones:
                window_ones -= nums[l % n]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)
        return total_ones - max_window_ones


nums = [0,1,0,1,1,0,0]
n1 = Solution()
print(n1.minSwaps(nums))

        
