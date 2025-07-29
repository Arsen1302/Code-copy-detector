class Solution:
    def solution_1499_5(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, cur = head, head.next
        
        while cur.next:
            if cur.val:
                res.val += cur.val
            else:
                res.next = res = cur
            cur = cur.next
        
        res.next = None
        return head