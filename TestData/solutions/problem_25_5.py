class Solution:
    def solution_25_5(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and not  root.left and not root.right:
            return True
        return self.solution_25_5(root.left, sum-root.val) or self.solution_25_5(root.right, sum-root.val)