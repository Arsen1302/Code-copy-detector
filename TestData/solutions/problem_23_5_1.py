class Solution:
    def solution_23_5_1(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        hleft=self.solution_23_5_2(root.left)
        hright=self.solution_23_5_2(root.right)
        
        if abs(hleft-hright)>1:
            return False
        
        if self.solution_23_5_1(root.left) and self.solution_23_5_1(root.right):
            return True
        else:
            return False
          
    def solution_23_5_2(self,root):
        
        if root is None:
            return 0
        
        return max(self.solution_23_5_2(root.left)+1,self.solution_23_5_2(root.right)+1)