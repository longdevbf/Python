class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    solution = Solution()
    result = solution.strStr(haystack, needle)
    print(result)  