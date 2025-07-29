class Solution:
    def solution_112_4(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.solution_112_4(root.right), self.solution_112_4(root.left)
        return root