from typing import List 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        a = str(x)
        b = a[::-1]
        if a == b:
            return True
        else:
            return False
if __name__ == "__main__":
    x = 121
    solution = Solution()
    result = solution.isPalindrome(x)
    print(result)  # Output: True