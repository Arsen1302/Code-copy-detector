class Solution:
    def solution_335_1_1(self, root: Optional[TreeNode]) -> int:
        def solution_335_1_2(node):
            nonlocal res
            if not node:
                return 0
            left_sum = solution_335_1_2(node.left)
            right_sum = solution_335_1_2(node.right)
            res += abs(left_sum - right_sum)
            
            return left_sum + node.val + right_sum
        
        res = 0
        solution_335_1_2(root)
        return res