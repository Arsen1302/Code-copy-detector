class Solution:
    def solution_54_5(self, head: Optional[ListNode]) -> bool:
        D={}
        while head:
            if head in D: return True
            D[head]=True
            head=head.next
        return False