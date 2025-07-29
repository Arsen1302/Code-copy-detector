class Solution:
    def solution_92_5(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        
        prev = dummyNode
        current = head
        
        while current:
            if current.val == val:
                prev.next = current.next
            else:  
                prev = current
            current = current.next
        
        return dummyNode.next