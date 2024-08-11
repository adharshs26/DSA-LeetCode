class Solution:
    def reverseWords(self, s: str) -> str:
        #splits the strings into list of words
        lstr = s.split() 
        #reverse the list
        revlst = lstr[::-1]
        #joins the reversed list of words into single string with a single space in between
        return " ".join(revlst) 
    
s = "the sky is blue"
print(Solution().reverseWords(s))