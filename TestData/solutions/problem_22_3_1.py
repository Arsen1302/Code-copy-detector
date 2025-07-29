class Solution:
    def solution_22_3_1(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head: return None

        def solution_22_3_2(node):

            if not node:
                return None
            slow = node
            fast = node
            prev = None
            while fast and fast.next:
                slow_next = slow.next
                fast_next = fast.next.next
                slow.next = prev
                prev = slow
                # print(slow_next.val if slow_next else None, fast_next.val if slow_next else None )
                slow = slow_next
                fast = fast_next
    
            right = slow.next
            slow.next = None

            left = None
            while prev:
                temp = prev.next
                prev.next = left
                left = prev
                prev = temp


            new_node = TreeNode(slow.val)
            new_node.left = solution_22_3_2(left)
            new_node.right = solution_22_3_2(right)

            return new_node
            

        return solution_22_3_2(head)