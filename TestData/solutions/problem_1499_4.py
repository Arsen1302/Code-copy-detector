class Solution:
    def solution_1499_4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        sm=0
        temp=temp.next
        curr=head
        while temp:
            if temp.val==0:
                curr=curr.next
                curr.val=sm
                sm=0
            else:
                sm+=temp.val
            temp=temp.next
        curr.next=None
        return head.next