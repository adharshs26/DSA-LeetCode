import collections
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = collections.Counter(nums)
        operations = 0
    
        for num in list(count):
            complement = k - num
            if complement in count:
                if num == complement:
                    operations += count[num] // 2
                else:
                    pairs = min(count[num], count[complement])
                    operations += pairs
                    count[num] -= pairs
                    count[complement] -= pairs
    
        return operations
    
nums = [3,1,3,4,3] 
k = 6
print(Solution().maxOperations(nums,k))