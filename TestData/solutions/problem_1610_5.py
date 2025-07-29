class Solution:
    def solution_1610_5(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        l=self.solution_1610_5(root.left)
        r=self.solution_1610_5(root.right)
        
        if root.val == 2:
            return l | r
        elif root.val == 3:
            return l &amp; r