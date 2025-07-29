class Solution:
    def solution_874_5_1(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def solution_874_5_2(r):
            if r:
                r.left = solution_874_5_2(r.left)
                r.right = solution_874_5_2(r.right)
                
                if not r.left and not r.right and r.val == target:
                    return None
                
                return r
            else:
                return None

        return solution_874_5_2(root)