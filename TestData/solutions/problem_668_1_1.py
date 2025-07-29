class Solution:
    res = 'z' * 13           # init max result, tree depth,  12< log2(8000) < 13
    
    def solution_668_1_1(self, root: TreeNode) -> str:
        
        def solution_668_1_2(node: TreeNode, prev):
            prev = chr(97 + node.val) + prev
            
            if not node.left and not node.right:
                self.res = min(self.res, prev)
                return
            
            if node.left:
                solution_668_1_2(node.left, prev)
            if node.right:
                solution_668_1_2(node.right, prev)
        
        solution_668_1_2(root, "")
        return self.res