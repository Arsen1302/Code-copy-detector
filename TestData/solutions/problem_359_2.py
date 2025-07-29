class Solution:
    def solution_359_2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1: return root2
        if not root2: return root1
        root1.val += root2.val
        root1.left = self.solution_359_2(root1.left, root2.left)
        root1.right = self.solution_359_2(root1.right, root2.right)
        return root1