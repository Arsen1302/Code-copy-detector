class Solution:
    def solution_866_1_1(self):
        self.summary = 0

    def solution_866_1_2(self, root: TreeNode) -> int:
        self.solution_866_1_3(root, False, False)
        return self.summary

    def solution_866_1_3(self, node: TreeNode, parent_even: bool, grand_parent_even: bool):
        if node is None:
            return
        if grand_parent_even:
            self.summary += node.val
        next_parent_even = True if node.val % 2 == 0 else False
        self.solution_866_1_3(node.left, next_parent_even, parent_even)
        self.solution_866_1_3(node.right, next_parent_even, parent_even)
        return