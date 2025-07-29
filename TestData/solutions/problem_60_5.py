class Solution:
    def solution_60_5(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, next=head)
        cur = head
        
        while cur.next:
            # beginning of the list
            begin = dummy 
            
            #traverse every element from begin of the list while not found element large or equal cur.next.val
            while cur.next.val > begin.next.val:
                begin = begin.next
            
            # transferring an element. If all the elements are smaller, then we change the element to ourselves
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = begin.next
            begin.next = tmp
            
            # if you did not move during the permutation, then move the pointer
            if cur.next == tmp:
                cur = cur.next

        return dummy.next