class Solution:
    def solution_911_4_1(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solution_911_4_2(root):
            if root is None:
                return -1, -1
            
            leftRight = solution_911_4_2(root.left)[1] + 1
            rightLeft = solution_911_4_2(root.right)[0] + 1
            self.res = max(self.res, leftRight, rightLeft)
            return leftRight, rightLeft
        
        solution_911_4_2(root)
        return self.res