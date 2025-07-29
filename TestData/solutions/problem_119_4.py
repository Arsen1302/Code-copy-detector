class Solution:
    def solution_119_4(self, head: ListNode) -> bool:
        prev = None
        fast = head
        slow = head
    
        # Reverse half the list while trying to find the end
        while fast and fast.next:
            fast = fast.next.next
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # left side 
        left = prev
        
		# right side
        if fast:
            '''
            if fast is not None, then the length of the list is odd
            and we can ignore the middle value
            '''
            right = slow.next
        else:
            right = slow
            
        # Just need to traverse each side and check if the values equal or not.
        while left is not None and right is not None:
            if left.val !=  right.val:
                return False
            left = left.next
            right = right.next
        
        return True