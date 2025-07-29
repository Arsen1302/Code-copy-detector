class Solution:
    def solution_1610_2(self, root: Optional[TreeNode]) -> bool:
        if root.left == None:
            return root.val
        if root.val == 2:
            res = self.solution_1610_2(root.left)  or self.solution_1610_2(root.right)
        else:
            res = self.solution_1610_2(root.left)  and self.solution_1610_2(root.right)
        return res