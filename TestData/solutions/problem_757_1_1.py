class Solution:
    def solution_757_1_1(self, node):
        if not node:
            return 0
        return max(self.solution_757_1_1(node.left), self.solution_757_1_1(node.right)) + 1
    
    def solution_757_1_2(self, node):
        if not node:
            return None
        left, right = self.solution_757_1_1(node.left), self.solution_757_1_1(node.right)
        if left == right:
            return node
        if left > right:
            return self.solution_757_1_2(node.left)
        if left < right:
            return self.solution_757_1_2(node.right)

    def solution_757_1_3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.solution_757_1_2(root)