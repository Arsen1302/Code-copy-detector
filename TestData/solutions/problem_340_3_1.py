class Solution:
    def solution_340_3_1(self, root, subroot):
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        return root.val == subroot.val and self.solution_340_3_1(root.left, subroot.left) and self.solution_340_3_1(root.right, subroot.right)
    
    def solution_340_3_2(self, cur, subRoot) -> bool:
        if not cur:
            return False
        if self.solution_340_3_1(cur, subRoot):
            return True
        else:
            return self.solution_340_3_2(cur.left, subRoot) or self.solution_340_3_3(cur.right, subRoot)
              
        
    def solution_340_3_3(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.solution_340_3_2(root, subRoot)