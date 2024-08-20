class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1, s2 = set(nums1), set(nums2)
        ans = [[], []]

        for i in s1:
            if i not in s2:
                ans[0].append(i)
        
        for i in s2:
            if i not in s1:
                ans[1].append(i)
        
        return ans

nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference(nums1,nums2))