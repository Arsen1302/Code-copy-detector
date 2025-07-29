class Solution:
    def solution_109_5(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftNodes = self.solution_109_5(root.left)
        rightNodes = self.solution_109_5(root.right)
        return leftNodes + rightNodes + 1