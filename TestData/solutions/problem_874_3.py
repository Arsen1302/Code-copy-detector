class Solution:
    def solution_874_3(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return root
        root.left = self.solution_874_3(root.left, target)
        root.right = self.solution_874_3(root.right, target)
        if root.val == target and not root.left and not root.right:
            return
        return root