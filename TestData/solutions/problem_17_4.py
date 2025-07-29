class Solution:
    def solution_17_4(self, node: TreeNode) -> int:
        if node is None:
            return 0

        return max(self.solution_17_4(node.left) + 1, self.solution_17_4(node.right) + 1)