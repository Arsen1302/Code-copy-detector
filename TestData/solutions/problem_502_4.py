class Solution:
    def solution_502_4(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        root .left=self.solution_502_4(root.left)
        root.right=self.solution_502_4(root.right)
        if root.val==0 and (root.left==None) and (root.right==None):
            return None
        return root