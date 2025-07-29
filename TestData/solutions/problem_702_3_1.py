class Solution:
    def solution_702_3_1(self, root: TreeNode) -> int:
        
        def solution_702_3_2(node, temp):
            if not node:
                return 0
            
            temp = temp*2 + node.val
            if (node.left is None) and (node.right is None):
                return temp
            
            return (solution_702_3_2(node.left, temp) + solution_702_3_2(node.right, temp))
        
        return solution_702_3_2(root, 0)