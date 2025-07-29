class Solution:
    def solution_170_1_1(self, root: TreeNode) -> int:
        def solution_170_1_2(node):
            if not node: return 0, 0
            left, right = solution_170_1_2(node.left), solution_170_1_2(node.right)
            v_take = node.val + left[1] + right[1]
            v_not_take = max(left) + max(right)
            return v_take, v_not_take
        return max(solution_170_1_2(root))