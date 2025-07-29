class Solution:
    def solution_322_2_1(self, root: TreeNode) -> int:
        def solution_322_2_2(root):
            nonlocal diameter
            if not root:
                return 0
            
            left = solution_322_2_2(root.left)
            right = solution_322_2_2(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        diameter = 0
        solution_322_2_2(root)
        return diameter