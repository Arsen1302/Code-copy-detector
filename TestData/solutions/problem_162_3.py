class Solution:
    def solution_162_3(self, head: ListNode) -> ListNode:
        odd = ListNode()
        even = ListNode()
        
        p1 = odd
        p2 = even
        t = head
            
        i = 1
        
        while t:
            if i % 2 != 0:
                p1.next = t
                p1 = p1.next
                
            else:
                p2.next = t
                p2 = p2.next
            
            i += 1
            t = t.next
        
        p2.next = None
        
    
        
        p1.next = even.next
        
        
        
        return odd.next