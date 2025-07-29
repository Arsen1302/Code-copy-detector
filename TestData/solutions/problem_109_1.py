class Solution:
    def solution_109_1(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + self.solution_109_1(root.left) + self.solution_109_1(root.right)