class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
         # Step 1: Count occurrences of each string
        count = {}
        for s in arr:
           if s in count:
             count[s] += 1
           else:
             count[s] = 1
    
        # Step 2: Collect distinct strings
        distinct_strings = []
        for s in arr:
           if count[s] == 1:
              distinct_strings.append(s)
    
        # Step 3: Return the k-th distinct string, or "" if not enough distinct strings
        if k <= len(distinct_strings):
           return distinct_strings[k - 1]
        else:
           return ""
        

arr = ["d","b","c","b","c","a"]
k= 2

print(Solution().kthDistinct(arr,k))