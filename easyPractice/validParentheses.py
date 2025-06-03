class Solution:
    def isValid(self, s: str) -> bool:
        input = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in s :
            if i in input:
               stack.append(input[i])
            elif not stack or i != stack.pop():
               return False 
        return not stack
if __name__ == "__main__":
    a = "([])"
    solution = Solution()
    rs = solution.isValid(a)
    print(rs)