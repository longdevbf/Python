from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        bit = 0
        while l1 or l2 or bit:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + bit
            bit = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            if l1: l1 = l1.next 
            if l2: l2.next 
        return dummy.next

if __name__ == "__main__":  
  
    l1 = ListNode(0, ListNode(8, ListNode(6, ListNode(5, ListNode(6, ListNode(8, ListNode(3, ListNode(5, ListNode(7)))))))))
    l2 = ListNode(6, ListNode(7, ListNode(8, ListNode(0, ListNode(8, ListNode(5, ListNode(8, ListNode(9, ListNode(7)))))))))
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")  # Output: 7 -> 0 -> 8 -> None