class Solution:
    def solution_1541_1(self, root: Optional[TreeNode]) -> bool:
        return root.left.val+root.right.val == root.val