class Solution:
    def compress(self, chars: list[str]) -> int:
        
    
         write = 0  # Pointer for writing the compressed characters
         read = 0   # Pointer for reading characters

         while read < len(chars):
            # Start of a new group
            char = chars[read]
            count = 0
        
            # Count the number of consecutive repeating characters
            while read < len(chars) and chars[read] == char:
               read += 1
               count += 1
        
            # Write the character to the `write` position
            chars[write] = char
            write += 1
        
            # If count > 1, write the length of the count
            if count > 1:
               for digit in str(count):
                  chars[write] = digit
                  write += 1
    
         # The new length of the array after compression
         return write

chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))