class Solution:
    def solution_170_5_1(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def solution_170_5_2(root, withRoot):
            if not root:
                return 0
            
            left, right = root.left, root.right
            
            res = 0
            if withRoot:
                res = root.val + solution_170_5_2(left, False) + solution_170_5_2(right, False)
            else:
                res = max(solution_170_5_2(left, False), solution_170_5_2(left, True)) +  max(solution_170_5_2(right, False), solution_170_5_2(right, True))
            
            return  res
 
        return max(solution_170_5_2(root, True), solution_170_5_2(root, False))