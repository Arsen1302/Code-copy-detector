class Solution:
    def solution_857_1(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        h = lambda r:  h(r.left) + [r.val] + h(r.right) if r else []
        return sorted( h(root1) + h(root2) )