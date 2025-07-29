class Solution:
    
    def solution_215_4_1(self, node: Optional[TreeNode]) -> float :
        if node :
            if not node.left and not node.right :
                return 1
        return 0
    
    def solution_215_4_2(self, root: Optional[TreeNode]) -> int:
        
        
        res = 0
        
        if root :
            if self.solution_215_4_1(root.left) :
                res += root.left.val
            
            res += self.solution_215_4_2(root.left) 
            res += self.solution_215_4_2(root.right)
            
        return res