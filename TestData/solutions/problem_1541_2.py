class Solution:
    def solution_1541_2(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val