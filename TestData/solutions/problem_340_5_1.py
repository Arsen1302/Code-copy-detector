class Solution:
    def solution_340_5_1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return
        def solution_340_5_2(r,s):
            if not s and not r:
                return True
            if not s or not r:
                return False
            if r.val == s.val and solution_340_5_2(r.left, s.left) and solution_340_5_2(r.right, s.right):
                return True
            else:
                return False
        if solution_340_5_2(root,subRoot) or self.solution_340_5_1(root.left, subRoot) or self.solution_340_5_1(root.right, subRoot):
            return True
        else:
            return False