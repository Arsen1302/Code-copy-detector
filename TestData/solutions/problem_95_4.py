class Solution:
    def solution_95_4(self, head: ListNode) -> ListNode:
        
        prev, cur = None, head
        
        while cur:
            
            # locate next hoppoing node
            next_hop = cur.next
            
            # reverse direction
            cur.next = prev
                
            prev = cur
            cur = next_hop

        # new head of reverse linked list    
        return prev