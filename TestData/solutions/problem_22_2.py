class Solution:
    def solution_22_2(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        
        fast = slow = prev_of_slow = head
        # looking for median of list
        while fast and fast.next:
            prev_of_slow, slow, fast = slow, slow.next, fast.next.next
            
        # median = slow.val
        prev_of_slow.next = None
        return TreeNode(slow.val, left=self.solution_22_2(head), right=self.solution_22_2(slow.next))