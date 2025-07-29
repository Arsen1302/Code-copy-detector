class Solution:
    def solution_112_2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root==None):return
        root.left,root.right=root.right,root.left
        self.solution_112_2(root.left)
        self.solution_112_2(root.right)
        return root