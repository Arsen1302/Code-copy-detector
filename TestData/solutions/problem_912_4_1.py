class Solution:
    
    def solution_912_4_1(self, node):
        if node is None:
            return 0, 0, inf, -inf
        
        l_best, l_sum, l_min, l_max = self.solution_912_4_1(node.left)
        r_best, r_sum, r_min, r_max = self.solution_912_4_1(node.right)
        l_min, r_max = min(node.val, l_min), max(node.val, r_max)
        
        if l_sum != -inf and r_sum != -inf and l_max < node.val < r_min:
            return max(l_best, r_best, l_sum + r_sum + node.val), l_sum + r_sum + node.val, l_min, r_max
        else:
            return max(l_best, r_best), -inf, l_min, r_max
        
    def solution_912_4_2(self, root: Optional[TreeNode]) -> int:
        return self.solution_912_4_1(root)[0]