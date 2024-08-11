import collections
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        freq = collections.Counter(word)
    
        # Get the frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)
    
        # We have 8 keys (2-9), and each key can have multiple letters
        num_keys = 8
        total_pushes = 0
    
        # Assign letters to keys
        for i, frequency in enumerate(frequencies):
            # Determine the number of presses for this letter
            presses = (i // num_keys) + 1
            total_pushes += presses * frequency
    
        return total_pushes
    
word = "xyzxyzxyzxyz"
print(Solution().minimumPushes(word))