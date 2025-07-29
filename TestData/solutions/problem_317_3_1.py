class Solution:
    def solution_317_3_1(self, root, sumSoFar):
        if root == None:
            return sumSoFar
        
        newSum = self.solution_317_3_1(root.right, sumSoFar)
        root.val = root.val + newSum
        return self.solution_317_3_1(root.left, root.val)
        
    
    def solution_317_3_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.solution_317_3_1(root,0)
        return root