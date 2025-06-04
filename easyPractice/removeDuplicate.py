from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Two pointers approach
        write_index = 1  # Vị trí để ghi phần tử unique tiếp theo
        
        for read_index in range(1, len(nums)):
            # Nếu phần tử hiện tại khác phần tử trước đó
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
        
        return write_index
