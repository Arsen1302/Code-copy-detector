class Solution:
    def solution_1541_3(self, root: Optional[TreeNode]) -> bool:
        if root.right.val + root.left.val == root.val:
            return True
        else:
            return False