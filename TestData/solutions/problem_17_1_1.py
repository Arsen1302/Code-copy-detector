class Solution:
    def solution_17_1_1(self, root: Optional[TreeNode]) -> int:
        def solution_17_1_2(root, depth):
            if not root: return depth
            return max(solution_17_1_2(root.left, depth + 1), solution_17_1_2(root.right, depth + 1))
                       
        return solution_17_1_2(root, 0)