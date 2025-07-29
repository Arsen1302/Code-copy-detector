class Solution:
    def solution_245_2_1(self, l1: ListNode, l2: ListNode) -> ListNode:

        def solution_245_2_2(node): 
            """Return number represented by linked list."""
            ans = 0
            while node:
                ans = 10*ans + node.val
                node = node.next
            return ans 
        
        dummy = node = ListNode()
        for x in str(solution_245_2_2(l1) + solution_245_2_2(l2)): 
            node.next = ListNode(int(x))
            node = node.next
        return dummy.next