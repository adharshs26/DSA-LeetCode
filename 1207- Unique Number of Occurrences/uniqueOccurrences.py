class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        nums = {}
        for num in arr:
            if num not in nums:
                nums[num] = 0
            nums[num] += 1
        occurences = set()
        for i in nums.values():
            if i in occurences:
                return False
            occurences.add(i)
        return True
        

arr = [1,2,2,1,1,3]
print(Solution().uniqueOccurrences(arr))        