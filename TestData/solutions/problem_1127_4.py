class Solution:
    def solution_1127_4(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        x = None
        while a > 0:
            x = temp
            temp = temp.next
            a -= 1
        
        temp1 = list1
        while b > 0:
            temp1 = temp1.next
            b -= 1
        
        temp2 = list2
        while temp2.next != None:
            temp2 = temp2.next
        
        if x is not None:
            x.next = list2
        else:
            list1 = list2
        
        temp2.next = temp1.next
        
        return list1