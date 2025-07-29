class Solution:
    def solution_61_1_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the list into two halfs
        left = head
        right = self.solution_61_1_2(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.solution_61_1_1(left)
        right = self.solution_61_1_1(right)
        
        return self.solution_61_1_3(left, right)
    
    def solution_61_1_2(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # Merge the list
    def solution_61_1_3(self, list1, list2):
        newHead = tail = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return newHead.next