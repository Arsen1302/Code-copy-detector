class Solution:
    def solution_215_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # does this node have a left child which is a leaf?
        if root.left and not root.left.left and not root.left.right:
			# gotcha
            return root.left.val + self.solution_215_1(root.right)

        # no it does not have a left child or it's not a leaf
        else:
			# bummer
            return self.solution_215_1(root.left) + self.solution_215_1(root.right)