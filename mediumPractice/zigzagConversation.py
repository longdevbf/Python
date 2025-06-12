class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if len(s) == 1 or numRows == 1:
            return s  
        rs = ''*numRows
        for i in range(numRows):
            j = i
            while j < len(s):
                rs += s[j]
                if i != 0 and i != numRows - 1 and j + (numRows - i - 1) * 2 < len(s):
                    rs += s[j + (numRows - i - 1) * 2]
                j += (numRows - 1) * 2
        return rs
if __name__ == "__main__":
    solution = Solution()
    test_string = "PAYPALISHIRING"
    num_rows = 3
    result = solution.convert(test_string, num_rows)
    print(f"The zigzag conversion of '{test_string}' with {num_rows} rows is: {result}")  # Output: "PAHNAPLSIIGYIR" for numRows = 3