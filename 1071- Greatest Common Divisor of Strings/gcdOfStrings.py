import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        elif str1+str2 != str2+str1:
            return ""
        else:
             result = math.gcd(len(str1), len(str2))
             return  str1[:result]
 

s = "ABCABC"
t = "ABC"
str3 = Solution()
print(str3.gcdOfStrings(s,t))