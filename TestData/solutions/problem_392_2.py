class Solution:
    def solution_392_2(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val > high:
            return self.solution_392_2(root.left, low, high)
        if root.val < low:
            return self.solution_392_2(root.right, low, high)
        root.left = self.solution_392_2(root.left, low, root.val)
        root.right = self.solution_392_2(root.right, root.val, high)
        return root