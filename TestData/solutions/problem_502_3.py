class Solution:
    def solution_502_3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if self.solution_502_3(root.left) is None:
            root.left = None
        if self.solution_502_3(root.right) is None:
            root.right = None
        
        if root.val != 1 and root.left is None and root.right is None:
            root = None
        
        return root