class Solution:
    def solution_1434_3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return

        fast = head.next
        slow = head        

        while slow and fast and fast.next:
            if fast.next.next is None:
                break
            else:
                fast= fast.next.next
            slow = slow.next

        slow.next = slow.next.next
        return head