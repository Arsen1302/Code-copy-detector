class Solution:
    def solution_54_3(self, head: Optional[ListNode]) -> bool:
        # Initialize two node slow and fast point to the hesd node...
        fastptr = head
        slowptr = head
        while fastptr is not None and fastptr.next is not None:
            # Move slow pointer by 1 node and fast at 2 at each step.
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            # If both the pointers meet at any point, then the cycle is present and return true...
            if slowptr == fastptr:
                return 1
        return 0