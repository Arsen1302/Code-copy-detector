class Solution:
    def solution_24_4_1(self, root: Optional[TreeNode]) -> int:
        def solution_24_4_2(root):
            if root.left is None and root.right is None:
                return 1
            if root.left is None and root.right:
                return 1+solution_24_4_2(root.right)
            if root.left and root.right is  None:
                return 1+solution_24_4_2(root.left)
            if root.left and root.right:
                return min(1+solution_24_4_2(root.right),1+solution_24_4_2(root.left))
        return solution_24_4_2(root) if root else 0