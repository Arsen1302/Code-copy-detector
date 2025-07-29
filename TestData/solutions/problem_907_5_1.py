class Solution:
    def solution_907_5_1(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
		def solution_907_5_2(head, root):
            if not head:
                return True
            if root and head.val == root.val:
                return (solution_907_5_2(head.next, root.left) or
                        solution_907_5_2(head.next, root.right))
            return False

        row = {root}
        while row:
            nextrow = set()
            for root in row:
                if root.val == head.val and solution_907_5_2(head, root):
                    return True
                if root.left:
                    nextrow.add(root.left)
                if root.right:
                    nextrow.add(root.right)
            row = nextrow

        return False