class Solution:
    def solution_17_5(self, root: TreeNode) -> int:
        if root==None:
            return 0
        left = self.solution_17_5(root.left)
        right = self.solution_17_5(root.right)
        return max(left,right)+1