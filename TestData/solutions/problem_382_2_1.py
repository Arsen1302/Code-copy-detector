class Solution:
    def solution_382_2_1(self, root: Optional[TreeNode]) -> List[List[str]]:
        solution_382_2_3 = self.solution_382_2_3(root) - 1
        m, n = solution_382_2_3 + 1, 2 ** (solution_382_2_3 + 1) - 1
        res = [[''] * n for _ in range(m)]
        
        def solution_382_2_2(root, r, c):
            if root is None:
                return
            
            res[r][c] = str(root.val)
            x = 2 ** (solution_382_2_3 - r - 1)
            solution_382_2_2(root.left, r + 1, c - x)
            solution_382_2_2(root.right, r + 1, c + x)
        
        solution_382_2_2(root, 0, (n - 1) // 2)
        return res
    
    def solution_382_2_3(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.solution_382_2_3(root.left), self.solution_382_2_3(root.right))