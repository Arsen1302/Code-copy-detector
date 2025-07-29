class Solution:
    def solution_1562_5_1(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def solution_1562_5_2(r):
            if r:
                vLeft, cLeft = solution_1562_5_2(r.left)
                vRight, cRight = solution_1562_5_2(r.right)
                
                value = vLeft + vRight + r.val
                nodes = cLeft + cRight + 1
                
                if r.val == value // nodes:
                    self.res += 1
                
                return value, nodes
            else:
                return 0, 0
        
        solution_1562_5_2(root)
        
        return self.res