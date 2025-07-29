class Solution:
    def solution_738_3_1(self, root: TreeNode, limit: int) -> TreeNode:
        
        def solution_738_3_2(node, prefix): 
            """Return updated node (possibly None) and max sum passing it."""
            if not node: return None, -inf # boundary condition 
            prefix += node.val # prefix sum 
            suffix = 0 
            if node.left or node.right: # non-leaf
                node.left, lsuf= solution_738_3_2(node.left, prefix)
                node.right, rsuf = solution_738_3_2(node.right, prefix)
                suffix = max(lsuf, rsuf) # max suffix sum
            return None if prefix + suffix < limit else node, node.val + suffix
        
        return solution_738_3_2(root, 0)[0]