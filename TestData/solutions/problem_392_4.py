class Solution:
    def solution_392_4(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if low <= root.val <= high:
            root.left = self.solution_392_4(root.left, low, high)
            root.right = self.solution_392_4(root.right, low, high)
        elif root.val < low:
            root = self.solution_392_4(root.right, low, high)
        else:
            root = self.solution_392_4(root.left, low, high)
            
        return root