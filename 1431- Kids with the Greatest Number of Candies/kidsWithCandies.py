class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result

candies = [2,3,5,1,3]
extraCandies = 3
c1 = Solution()
print(c1.kidsWithCandies(candies,extraCandies))