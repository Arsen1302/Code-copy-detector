class Solution:
    def solution_170_2_1(self, root: TreeNode) -> int:
        def solution_170_2_2(node):
            return (node.val + (left:=solution_170_2_2(node.left))[1] + (right:=solution_170_2_2(node.right))[1], max(left) + max(right)) if node else (0, 0)
        return max(solution_170_2_2(root))