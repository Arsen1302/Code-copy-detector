class Solution:
    def solution_322_4_1(self, root: TreeNode) -> int:
        
        def solution_322_4_2(node):
            """Return length+1 and diameter rooted at node"""
            if not node: return (0, 0)
            l1, d1 = solution_322_4_2(node.left)
            l2, d2 = solution_322_4_2(node.right)
            return 1 + max(l1, l2), max(d1, d2, l1+l2)
        
        return solution_322_4_2(root)[1]