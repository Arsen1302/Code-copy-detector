class Solution:
    def solution_632_5(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        return not r1 and not r2 if not r1 or not r2 else (self.solution_632_5(r1.right, r2.right) and self.solution_632_5(r1.left, r2.left)) or (self.solution_632_5(r1.left, r2.right) and self.solution_632_5(r1.right, r2.left)) if r1.val == r2.val else False