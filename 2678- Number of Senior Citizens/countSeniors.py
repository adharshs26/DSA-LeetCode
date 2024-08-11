class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for detail in details:
            age_str = detail[11:13]
            age = int(age_str)
            if age > 60:
               count += 1
        return count  



details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
lst1 = Solution()
print(lst1.countSeniors(details))
        