class Solution:
    def solution_1127_3(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummynode = ListNode(-1, list1)
        curr = dummynode
        idx = 0
        while curr.next:            
            if idx == a:
                head = curr
                curr = curr.next
                head.next = list2
                while list2.next:
                    list2 = list2.next
            if idx == b:
                list2.next = curr.next
                break
            curr = curr.next
            idx += 1
        return dummynode.next