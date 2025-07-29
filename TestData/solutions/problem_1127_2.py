class Solution:
    def solution_1127_2(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        point1 = list1
        point2 = list1
        for _ in range(b - a):
            point2 = point2.next
        prev = None
        for _ in range(a):
            prev = point1
            point1 = point1.next
            point2 = point2.next
        
        prev.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = point2.next
        
        return list1