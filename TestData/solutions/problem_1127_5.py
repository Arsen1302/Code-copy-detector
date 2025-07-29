class Solution:
    def solution_1127_5(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev, first, second = None, list1, list1
        
        #Moves the second pointer forward
        while b - a > 0:
            second = second.next
            b -= 1
        
        #Moves all pointers forward
        while a > 0:
            prev = first
            first = first.next
            second = second.next
            a -= 1
        
        #prev is the tail in the first part of list1, link the next pointer to list2 head
        prev.next = list2
        
        #Iterates through the second list
        curr = list2
        while curr.next:
            curr = curr.next
        
        #Attaches to the tail of list2 the second part of list1 (second is the last node to be removed)
        curr.next = second.next
        
        return list1