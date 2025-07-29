class Solution:
    def solution_335_3_1(self):
        self.ans = 0
        
    def solution_335_3_2(self, root):
        if not root:
            return 0
        
        left = self.solution_335_3_2(root.left)
        right = self.solution_335_3_2(root.right)
        self.ans += abs(left - right)
        return left + right + root.val
    
    def solution_335_3_3(self, root: Optional[TreeNode]) -> int:
        self.solution_335_3_2(root)
        return self.ans