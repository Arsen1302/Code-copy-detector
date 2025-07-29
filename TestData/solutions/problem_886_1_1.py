class Solution:
    def solution_886_1_1(self, root: Optional[TreeNode]) -> int:
        vals = []
        
        def solution_886_1_2(node): 
            """Return sum of sub-tree."""
            if not node: return 0 
            ans = node.val + solution_886_1_2(node.left) + solution_886_1_2(node.right)
            vals.append(ans)
            return ans
        
        total = solution_886_1_2(root)
        return max((total-x)*x for x in vals) % 1_000_000_007