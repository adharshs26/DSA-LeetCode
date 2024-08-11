class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
    
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return ones[n]
            elif n < 100:
                return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
            elif n < 1000:
                return ones[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + helper(n % 100))
            else:
                for i, chunk in enumerate(large_numbers):
                    if n < 1000 ** (i + 1):
                        return helper(n // (1000 ** i)) + ' ' + chunk + ('' if n % (1000 ** i) == 0 else ' ' + helper(n % (1000 ** i)))
    
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"]
    
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
        large_numbers = ["", "Thousand", "Million", "Billion"]
    
        return helper(num).strip()
    

num = 12345
print(Solution().numberToWords(num))