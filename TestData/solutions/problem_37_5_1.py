class Solution:
    def solution_37_5_1(self, root: TreeNode) -> int:
        max_path = -inf

        def solution_37_5_2(node: TreeNode):
            nonlocal max_path
            left = solution_37_5_2(node.left) if node.left else 0
            right = solution_37_5_2(node.right) if node.right else 0
            max_path = max(max_path, node.val, node.val + left,
                           node.val + right, node.val + left + right)
            return node.val + max(left, right, 0)

        if root:
            solution_37_5_2(root)
        return max_path