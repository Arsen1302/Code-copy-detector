class Solution:
    def solution_632_1(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val: return False
        return (self.solution_632_1(root1.left, root2.left) and self.solution_632_1(root1.right, root2.right)) or (self.solution_632_1(root1.left, root2.right) and self.solution_632_1(root1.right, root2.left))