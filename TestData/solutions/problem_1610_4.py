class Solution:
    def solution_1610_4(self, root: Optional[TreeNode]) -> bool:
        
        if root.val < 2:
            return root.val
        if root.val == 2:
            return self.solution_1610_4(root.left) or self.solution_1610_4(root.right)
        if root.val == 3:
            return self.solution_1610_4(root.left) and self.solution_1610_4(root.right)