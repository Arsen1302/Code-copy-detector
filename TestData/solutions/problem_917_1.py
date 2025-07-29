class Solution:    
    def solution_917_1(self, node1: TreeNode, node2: TreeNode, target: TreeNode) -> TreeNode:        
        if not node1 or target == node1:  # if node1 is null, node2 will also be null
            return node2
        
        return self.solution_917_1(node1.left, node2.left, target) or self.solution_917_1(node1.right, node2.right, target)