class Solution:
    def solution_844_3(self, head: ListNode) -> int:
        res = 0
        while head:
            res = 2*res + head.val
            head = head.next
        return res