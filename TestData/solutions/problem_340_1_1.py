class Solution:
    def solution_340_1_1(self, s: TreeNode, t: TreeNode) -> bool:
        if not s: 
            return False
        if self.solution_340_1_2(s, t): 
            return True
        return self.solution_340_1_1(s.left, t) or self.solution_340_1_1(s.right, t)

    def solution_340_1_2(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.solution_340_1_2(p.left, q.left) and self.solution_340_1_2(p.right, q.right)
        return p is q