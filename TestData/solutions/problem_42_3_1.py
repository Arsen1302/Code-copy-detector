class Solution:
    def solution_42_3_1(self, root: TreeNode) -> int:
        
        def solution_42_3_2(node, val):
            """Return sum of node-to-leaf numbers"""
            if not node: return 0
            val = 10*val + node.val
            if not node.left and not node.right: return val 
            return solution_42_3_2(node.left, val) + solution_42_3_2(node.right, val)
            
        return solution_42_3_2(root, 0)