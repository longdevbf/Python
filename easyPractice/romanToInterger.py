class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
           if(i > 0 and roman_nums[s[i]] > roman_nums[s[i - 1]]):
                total += roman_nums[s[i]] - 2 * roman_nums[s[i - 1]]
           else:
               total += roman_nums[s[i]]
        return total
    
if __name__ == "__main__":
    str = "MCMXCIV"
    solution = Solution()
    rls = solution.romanToInt(str)
    print(rls)  