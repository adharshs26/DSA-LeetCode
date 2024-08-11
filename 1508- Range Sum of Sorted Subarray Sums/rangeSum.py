class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        subarray_sums = []
    
        # Generate all subarray sums
        for start in range(n):
           current_sum = 0
           for end in range(start, n):
             current_sum += nums[end]
             subarray_sums.append(current_sum)
    
        # Sort the subarray sums
        subarray_sums.sort()
    
        # Compute the sum of the range
        result_sum = 0
        for i in range(left - 1, right):
          result_sum = (result_sum + subarray_sums[i]) % MOD
    
        return result_sum
    
nums = [1,2,3,4] 
n = 4 
left = 3 
right = 4

print(Solution().rangeSum(nums,n,left,right))