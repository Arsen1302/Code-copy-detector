class Solution:
    def solution_61_5_1(self, head: ListNode) -> ListNode:
        half = self.solution_61_5_2(head)
        if not half or head == half: return head 
        return self.solution_61_5_3(self.solution_61_5_1(head), self.solution_61_5_1(half))
    
    
    def solution_61_5_2(self, node: ListNode) -> ListNode: 
        """Break the list into two parts and return the head of 2nd half"""
        fast = prev = slow = node 
        while fast and fast.next:
            fast, prev, slow = fast.next.next, slow, slow.next
        if prev: prev.next = None #break linked list
        return slow
    
    
    def solution_61_5_3(self, list1: ListNode, list2: ListNode) -> ListNode: 
        """Merge two sorted lists into a sorted list"""
        dummy = node = ListNode()
        while list1 and list2: 
            if list1.val > list2.val: list1, list2 = list2, list1
            node.next = list1
            node, list1 = node.next, list1.next 
        node.next = list1 or list2
        return dummy.next