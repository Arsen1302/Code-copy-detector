class Solution:
    def solution_162_5(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp2 = head
        c = 1
        while temp2.next:
            temp2 = temp2.next
            c += 1
        i = 0
        previous = head
        temp1 = head
        while i < c:
            if i % 2 != 0:
                temp2.next = ListNode(temp1.val)
                temp2 = temp2.next
                previous.next = previous.next.next
                previous = previous.next
            temp1 = temp1.next
            i += 1
        return head