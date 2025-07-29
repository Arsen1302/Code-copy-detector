class Solution:
    def solution_738_4_1(self, root: TreeNode, limit: int) -> TreeNode:
        
        def solution_738_4_2(node, x): 
            """Return updated node."""
            if not node: return 
            x -= node.val
            if node.left is node.right: return None if x > 0 else node # leaf 
            node.left = solution_738_4_2(node.left, x)
            node.right = solution_738_4_2(node.right, x)
            return node if node.left or node.right else None
        
        return solution_738_4_2(root, limit)