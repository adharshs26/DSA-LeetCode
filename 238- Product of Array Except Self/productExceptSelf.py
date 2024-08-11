class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        answer = [1] * n

        for i in range (1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = 1
        for i in range(n-1,-1,-1):
            answer[i] = prefix[i] * suffix
            suffix *= nums[i]
        return answer            


nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))