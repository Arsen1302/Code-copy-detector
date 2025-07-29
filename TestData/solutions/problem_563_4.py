class Solution:
    def solution_563_4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next # Move by one node ahead
            fast = fast.next.next # Move by two nodes ahead
        
        return slow