class Solution:
    def solution_1499_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        chunk = head
        while chunk: 
            chunk = chunk.next 
            sm = 0 
            while chunk and chunk.val: 
                sm += chunk.val 
                chunk = chunk.next 
            if sm: node.next = node = ListNode(sm)
        return dummy.next