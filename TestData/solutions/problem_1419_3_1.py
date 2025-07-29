class Solution:
    def solution_1419_3_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        groupCount = 0
        ptr1 = None
        ptr2 = head
        
        while ptr2:
            count = 0
            ptr3 = ptr2
            ptr4 = None
            while ptr3 and count<groupCount+1:
                ptr4 = ptr3
                ptr3 = ptr3.next
                count += 1
            
            if count%2:
                ptr1 = ptr4
            else:
                ptr1.next = self.solution_1419_3_2(ptr2, ptr3)
                ptr1 = ptr2
            ptr2 = ptr3
            groupCount += 1
        
        return head
            
    def solution_1419_3_2(self, curr, until):
        prev = until
        next = curr.next
        
        while next!=until:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        
        curr.next = prev
        return curr