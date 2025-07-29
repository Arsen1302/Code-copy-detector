class Solution:
    def solution_552_5_1(self, root: TreeNode) -> TreeNode:
        def solution_552_5_2(n, level = 0):
            if not n:
                return 0, None
            l, r = solution_552_5_2(n.left, level + 1), solution_552_5_2(n.right, level + 1)
            if l[0] == r[0]:
                return max(level, l[0]), n
            return max((l, r), key = lambda x: x[0])
        return solution_552_5_2(root)[1]