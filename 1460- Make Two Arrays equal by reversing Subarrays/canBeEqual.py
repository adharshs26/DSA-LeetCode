import collections
class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:

        if len(target) != len(arr):
            return False
        
        # Compare element frequencies in both arrays
        return collections.Counter(target) == collections.Counter(arr)
    

target = [1,2,3,4]
arr = [2,4,1,3]
print(Solution().canBeEqual(target,arr))