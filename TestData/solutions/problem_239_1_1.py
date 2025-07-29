class Solution:
    def solution_239_1_1(self, root: TreeNode, sum: int) -> int:
        
        global result
        result = 0
        
        def solution_239_1_2(node, target):
            if node is None: return
            solution_239_1_3(node, target)
            solution_239_1_2(node.left, target)
            solution_239_1_2(node.right, target)
                
        def solution_239_1_3(node, target):
            global result
            if node is None: return
            if node.val == target: result += 1
            solution_239_1_3(node.left, target-node.val)
            solution_239_1_3(node.right, target-node.val)
            
        solution_239_1_2(root, sum)
        
        return result