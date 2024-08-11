class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
    
        # Lengths of s and t
        len_s, len_t = len(s), len(t)
    
        # Traverse t
        while j < len_t:
             # Check if characters match
             if i < len_s and s[i] == t[j]:
                 i += 1
             # Move to the next character in t
             j += 1
    
        # If all characters of s were matched
        return i == len_s
    
s = "abc"
t = "ahbgdc"
print(Solution().isSubsequence(s,t))