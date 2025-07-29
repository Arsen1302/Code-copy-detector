class Solution:
    res = 0
    def solution_649_3_1(self, root: TreeNode) -> int:

        def solution_649_3_2(node: TreeNode) -> int:
        
            if not node: return 0
            val = solution_649_3_2(node.left) + solution_649_3_2(node.right)
        
            if val == 0: return 3
            if val < 3: return 0
        
            self.res += 1
        
            return 1
        
        return self.res + 1 if solution_649_3_2(root) > 2 else self.res