class Solution:
    def solution_1461_5(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # slow == n / 2 - 1, fast == n - 1
        
        # reverse nodes from n / 2 to n - 1
        prev, cur = None, slow.next
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        
        twin1, twin2 = head, prev  # 0, n - 1
        res = 0
        while twin2:
            res = max(res, twin1.val + twin2.val)
            twin1, twin2 = twin1.next, twin2.next
        
        return res