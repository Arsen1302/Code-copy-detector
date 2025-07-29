class Solution:
    def solution_335_5_1(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solution_335_5_2(root):
            if root is None:
                return 0
            
            left, right = solution_335_5_2(root.left), solution_335_5_2(root.right)
            self.res += abs(left - right)
            return root.val + left + right
        
        solution_335_5_2(root)
        return self.res