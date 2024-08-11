class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1, n2)

        for i in range(n):
            result += word1[i] + word2[i]

        return result + word1[n:] + word2[n:]
        

        
word1 = "abc"
word2 = "pqr"
word = Solution()
print(word.mergeAlternately(word1,word2))