class Solution:
    def solution_706_3_1(self, root: Optional[TreeNode]) -> int:
        
        
        self.ans=0
        def solution_706_3_2(root,mn,mx):
            if root==None:
                self.ans=max(self.ans,abs(mx-mn))
                return
            
            solution_706_3_2(root.left,min(mn,root.val),max(mx,root.val))
            solution_706_3_2(root.right,min(mn,root.val),max(mx,root.val))
        
        solution_706_3_2(root,root.val,root.val)
        return self.ans