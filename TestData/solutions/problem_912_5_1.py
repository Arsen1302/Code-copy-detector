class Solution:
    def solution_912_5_1(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def solution_912_5_2(root):
            nonlocal max_sum
            if root is None:
                return 1, inf, -inf, 0      
            
            is_l, min_l, max_l, sum_l = solution_912_5_2(root.left)
            is_r, min_r, max_r, sum_r = solution_912_5_2(root.right)
            
            if is_l and is_r and max_l < root.val < min_r:
                cur = sum_l + sum_r + root.val
                max_sum = max(cur, max_sum)
                min_l = min(min_l, root.val)
                max_r = max(max_r, root.val)
                return 1, min_l, max_r, cur
            else:
                return 0, 0, 0, 0
                
        solution_912_5_2(root)
        return max_sum