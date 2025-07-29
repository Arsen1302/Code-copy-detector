class Solution:
    def solution_61_3_1(self, head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev: prev.next = None
        return slow
    
    def solution_61_3_2(self, l1, l2):
        dummy = tail = ListNode()
        while l1 or l2:
            v1 = l1.val if l1 else inf
            v2 = l2.val if l2 else inf
            if v1 <= v2:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return dummy.next
            
    
    def solution_61_3_3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        head2 = self.solution_61_3_1(head)
        
        head1 = self.solution_61_3_3(head)
        head2 = self.solution_61_3_3(head2)
        
        return self.solution_61_3_2(head1, head2)