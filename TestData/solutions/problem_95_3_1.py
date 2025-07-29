class Solution:
    
    def solution_95_3_1(self, prev, cur):
        
        if cur:

            # locate next hopping node
            next_hop = cur.next
            
            # reverse direction
            cur.next = prev
        
            return self.solution_95_3_1( cur, next_hop)
        
        else:

            # new head of reverse linked list
            return prev    
            
    
    def solution_95_3_2(self, head: ListNode) -> ListNode:
        
        return self.solution_95_3_1( None, head)