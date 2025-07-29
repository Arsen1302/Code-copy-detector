class Solution:
def solution_170_3_1(self, root: Optional[TreeNode]) -> int:
    
    def solution_170_3_2(root):
        if root is None:
            return (0,0)
        
        left = solution_170_3_2(root.left)
        right = solution_170_3_2(root.right)
        return (root.val+left[1]+right[1], max(left)+max(right))
    
    return max(solution_170_3_2(root))