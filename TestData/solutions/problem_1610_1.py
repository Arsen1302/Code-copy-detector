class Solution:
    def solution_1610_1(self, root: Optional[TreeNode]) -> bool:
            if root.val==0 or root.val==1:
                return root.val
            if root.val==2:
                return self.solution_1610_1(root.left) or self.solution_1610_1(root.right)
            if root.val==3:
                return self.solution_1610_1(root.left) and self.solution_1610_1(root.right)