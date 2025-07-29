class Solution:
    def solution_1499_3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        ans = ListNode()
        dummy = ans
        while current is not None and current.next is not None:
            if current.val == 0:
                count = 0
                current = current.next
                while current.val != 0 and current is not None:
                    count += current.val
                    current = current.next
                dummy.next = ListNode(count)
                dummy = dummy.next
        return ans.next