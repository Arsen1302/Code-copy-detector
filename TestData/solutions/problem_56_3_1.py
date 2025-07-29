class Solution:
    def solution_56_3_1(self , head):
        prev = None
        after = None
        curr = head
        while(curr):
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        return prev
            
    def solution_56_3_2(self , head):
        slow = head
        fast = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow
        
    def solution_56_3_3(self, head: Optional[ListNode]) -> None:
        mid = self.solution_56_3_2(head)
        rev = self.solution_56_3_1(mid)
        first = head
        second = rev
        
        while(second.next):
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp