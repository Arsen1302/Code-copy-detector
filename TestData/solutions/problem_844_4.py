class Solution:
    def solution_844_4(self, head: ListNode) -> int:
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next
        return res