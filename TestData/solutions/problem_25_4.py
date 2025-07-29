class Solution:
    def solution_25_4(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return (root.val == targetSum) if (root and not root.left and not root.right) else (root and (self.solution_25_4(root.right, targetSum - root.val) or self.solution_25_4(root.left, targetSum - root.val)))