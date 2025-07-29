class Solution:
    def solution_26_4_1(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Simple dfs solution
        # we have to check both left call, and right call and
        # insert path into the final result i.e. res
        
        def solution_26_4_2(root,targetsum,path,res,csum):
            if root is None:
                return
            if root.left == None and root.right==None:
                if targetSum==csum+root.val:
                    path+=[root.val]
                    return res.append(path[:])
            solution_26_4_2(root.left,targetSum,path+[root.val],res,csum+root.val)
            solution_26_4_2(root.right,targetSum,path+[root.val],res,csum+root.val)
            
        path=[]
        res=[]
        solution_26_4_2(root,targetSum,path,res,0)
        return res