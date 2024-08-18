class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        l=[0]
        sum=0
        for i in gain:
            sum+=i
            l.append(sum)
        return max(l)
    
gain = [-5,1,5,0,-7]
print(Solution().largestAltitude(gain))