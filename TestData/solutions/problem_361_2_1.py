class Solution:
    def solution_361_2_1(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1: return TreeNode(v, left=root) # edge case 
        
        def solution_361_2_2(node, d): 
            if d == 1: 
                node.left = TreeNode(v, left=node.left)
                node.right = TreeNode(v, right=node.right)
            if node.left: node.left = solution_361_2_2(node.left, d-1)
            if node.right: node.right = solution_361_2_2(node.right, d-1)
            return node 
        
        return solution_361_2_2(root, d-1)