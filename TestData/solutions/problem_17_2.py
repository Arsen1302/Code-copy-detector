class Solution:
    def solution_17_2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.solution_17_2(root.left), self.solution_17_2(root.right)) + 1