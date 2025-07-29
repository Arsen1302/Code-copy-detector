class Solution:
    def solution_473_2_1(self,root,vals):
        if root is None:
            return
        
        self.solution_473_2_1(root.left,vals)
        vals.append(root.val)
        self.solution_473_2_1(root.right,vals)
        
    def solution_473_2_2(self, root: Optional[TreeNode]) -> int:
        vals =[]
        self.solution_473_2_1(root,vals)
        
        ans = [abs(vals[i+1]-vals[i]) for i in range(len(vals)-1)]
        return min(ans)