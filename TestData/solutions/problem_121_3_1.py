class Solution:
    def solution_121_3_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def solution_121_3_2(node):
            """Return LCA of p and q in subtree rooted at node (if found)."""
            if not node or node in (p, q): return node
            left, right = solution_121_3_2(node.left), solution_121_3_2(node.right)
            return node if left and right else left or right
        
        return solution_121_3_2(root)