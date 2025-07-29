class Solution:
    def solution_1127_1(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr=list1
        for count in range(b):
            if count==a-1:      # travel to a node and   --> step 1
                start=curr      # then save pointer in start
            curr=curr.next   # continue travel to b node  --> step 2
        start.next=list2     # point start to list2   --> step3
        while list2.next:    # travel list2   --> step 4
            list2=list2.next
        list2.next=curr.next  # map end of list2 to b
        return list1