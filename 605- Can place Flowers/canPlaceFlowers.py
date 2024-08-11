class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length=len(flowerbed)
        if n==0:
            return True
        for i in range(length):
            if flowerbed[i] == 0:
                cond1 = (i==0 or flowerbed[i-1]==0)
                cond2 = (i==length-1 or flowerbed[i+1]==0)
                if cond1 and cond2:
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                        return True
        return False        


flowerbed = [1,0,0,0,1]
n=1
f1 = Solution()
print(f1.canPlaceFlowers(flowerbed,n))