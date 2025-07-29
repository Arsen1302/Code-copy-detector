class Solution:
    def solution_162_4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        headOdd, headEven = head, head.next
        tailOdd, tailEven = headOdd, headEven
        
        i = 3
        cur = headEven.next
        while cur:
            if i%2:
                tailOdd.next = cur
                tailOdd = cur
            else:
                tailEven.next = cur
                tailEven = cur
                
            cur = cur.next
            i += 1
            
        tailEven.next = None # prevent cycle
        tailOdd.next = headEven
        
        return headOdd