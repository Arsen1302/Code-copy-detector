class Solution:
    def solution_119_3_1(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # We use slow and fast pointer algorithm to get the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalfEnd = self.solution_119_3_2(slow)
        pointer1 = head
        pointer2 = secondHalfEnd
        
        validPalindrome = True
        
        while pointer1 and pointer2:
            if pointer1.val != pointer2.val:
                validPalindrome = False
                break
            
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        self.solution_119_3_2(secondHalfEnd) # Reverse the second half of the Linked List back to normal
        return validPalindrome
    
    def solution_119_3_2(self, head):
        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        return prev