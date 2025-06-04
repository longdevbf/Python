from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Modify nums trực tiếp
            k += 1
    return k
if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    solution = Solution()
    result = solution.removeElement(nums, val)
    print(result)  # Output: [2, 2]
    
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = solution.removeElement(nums, val)
    print(result)  # Output: [0, 1, 3, 0, 4]