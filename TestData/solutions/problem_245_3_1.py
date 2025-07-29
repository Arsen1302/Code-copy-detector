class Solution:
    def solution_245_3_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def solution_245_3_2(node): 
            """Reverse a linked list."""
            prev = None
            while node: prev, node.next, node = node, prev, node.next
            return prev 
        
        l1, l2 = solution_245_3_2(l1), solution_245_3_2(l2) # reverse l1 &amp; l2
        carry = 0
        dummy = node = ListNode()
        while carry or l1 or l2:
            if l1: 
                carry += l1.val
                l1 = l1.next
            if l2: 
                carry += l2.val
                l2 = l2.next
            carry, x = divmod(carry, 10)
            node.next = node = ListNode(x)
        return solution_245_3_2(dummy.next)