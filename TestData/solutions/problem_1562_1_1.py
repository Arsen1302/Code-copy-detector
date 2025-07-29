class Solution:
    def solution_1562_1_1(self, root: Optional[TreeNode]) -> int:
        
        def solution_1562_1_2(node): 
            nonlocal ans
            if not node: return 0, 0 
            ls, ln = solution_1562_1_2(node.left)
            rs, rn = solution_1562_1_2(node.right)
            s = node.val + ls + rs
            n = 1 + ln + rn
            if s//n == node.val: ans += 1
            return s, n
        
        ans = 0 
        solution_1562_1_2(root)
        return ans