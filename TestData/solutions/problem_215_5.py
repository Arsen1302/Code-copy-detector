class Solution:
    def solution_215_5(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left and not root.left.left and not root.left.right:
            return root.left.val+self.solution_215_5(root.right)
        else:
            return self.solution_215_5(root.left)+self.solution_215_5(root.right)