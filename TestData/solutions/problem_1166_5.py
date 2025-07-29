class Solution:
    def solution_1166_5(self, head: ListNode, k: int) -> ListNode:
        node = n1 = n2 = head 
        while node: 
            if k == 1: n1 = node 
            if k <= 0: n2 = n2.next 
            node = node.next
            k -= 1
        n1.val, n2.val = n2.val, n1.val
        return head