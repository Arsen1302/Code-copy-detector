class Solution:
    def solution_706_5_1(self, root: Optional[TreeNode]) -> int:
        def solution_706_5_2(root, min_so_far, max_so_far):
            if not root: return
            nonlocal res
            min_so_far, max_so_far = min(min_so_far, root.val), max(max_so_far, root.val)
            res = max(res, root.val - min_so_far, max_so_far - root.val)
            solution_706_5_2(root.left, min_so_far, max_so_far); solution_706_5_2(root.right, min_so_far, max_so_far);
            
        res = 0
        solution_706_5_2(root, math.inf, -math.inf)
        return res