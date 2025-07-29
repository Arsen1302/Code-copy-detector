class Solution:
    def solution_361_1(self, root: TreeNode, v: int, d: int, side = "left") -> TreeNode:
        if d == 1:
            res = TreeNode(v)
            setattr(res, side, root)
            return res
        if root:
            root.left = self.solution_361_1(root.left, v, d - 1)
            root.right = self.solution_361_1(root.right, v, d - 1, 'right')
        return root