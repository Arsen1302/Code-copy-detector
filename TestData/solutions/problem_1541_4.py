class Solution:
    def solution_1541_4(self, root: Optional[TreeNode]) -> bool:
        if (root.left.val + root.right.val) == root.val:
            return True
        return False