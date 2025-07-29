class Solution:
    def solution_619_5_1(self, root: TreeNode, L: int, R: int) -> int:
        valid_vals = []
        def solution_619_5_2(root):
            if root.val >= L and root.val<=R:
                valid_vals.append(root.val)
            if root.left:
                solution_619_5_2(root.left)
            if root.right:
                solution_619_5_2(root.right)
        solution_619_5_2(root)
        return sum(valid_vals)