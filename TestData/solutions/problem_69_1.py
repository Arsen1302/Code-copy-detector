class Solution:
    def solution_69_1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first_set=set()
        curr=headA
        
        while curr:
            first_set.add(curr)
            curr=curr.next
        
        curr = headB
        while curr:
            if curr in first_set:
                return curr
            curr=curr.next

        return None