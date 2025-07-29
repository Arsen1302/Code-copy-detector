class Solution:
    def solution_473_4(self, root: Optional[TreeNode]) -> int:
        inOrder = lambda n: inOrder(n.left) + [n.val] + inOrder(n.right) if n else []
        vals = inOrder(root)
        return min(a - b for a, b in zip(vals[1:], vals))