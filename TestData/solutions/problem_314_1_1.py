class Solution:
    def solution_314_1_1(self, root: Optional[TreeNode]) -> int:
        d = float('inf')
        s = []
        if root == None:
            return 
        d = self.solution_314_1_2(root,d,s)
        return d
    def solution_314_1_2(self,root,d,s):
        if root.left != None:
            d = self.solution_314_1_2(root.left,d,s)
        s.append(root.val)
        if len(s)>1:
            diff = s[-1]-s[-2]
            if diff < d:
                d = diff
        if root.right != None:
            d = self.solution_314_1_2(root.right,d,s) 
        return d