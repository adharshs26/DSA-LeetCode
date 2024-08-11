class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(s)
    
        # Initialize the count of vowels in the first window of length k
        current_vowel_count = sum(1 for char in s[:k] if char in vowels)
        max_vowel_count = current_vowel_count
    
        # Slide the window from start to end of the string
        for i in range(k, n):
            if s[i - k] in vowels:
                current_vowel_count -= 1
            if s[i] in vowels:
                current_vowel_count += 1
            max_vowel_count = max(max_vowel_count, current_vowel_count)
    
        return max_vowel_count
    
s = "leetcode"
k = 3

print(Solution().maxVowels(s,k))