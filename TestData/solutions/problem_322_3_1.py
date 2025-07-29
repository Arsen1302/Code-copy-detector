class Solution:
    def solution_322_3_1(self, root: TreeNode) -> int:
        def solution_322_3_2(root):
            nonlocal maxSum
            if not root:
                return 0
            
            left = solution_322_3_2(root.left)
            right = solution_322_3_2(root.right)
            maxSum = max(maxSum, left + right + root.val)
            return max(left + root.val, right + root.val, 0)
        
        maxSum = -math.inf  
        solution_322_3_2(root)
        return maxSum