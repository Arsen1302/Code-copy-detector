class Solution:
    def solution_706_1_1(self, root: Optional[TreeNode]) -> int:
        def solution_706_1_2(root, mn, mx):
            # Base Case: If we reach None, just return 0 in order not to affect the result
            if not root: return 0
            
			# The best difference we can do using the current node can be found:
            res = max(abs(root.val - mn), abs(root.val - mx))
			
			# Recompute the new minimum and maximum taking into account the current node
            mn, mx = min(mn, root.val), max(mx, root.val)
			
			# Recurse left and right using the newly computated minimum and maximum
            return max(res, solution_706_1_2(root.left, mn, mx), solution_706_1_2(root.right, mn, mx))
        
        # Initialize minimum `mn` and maximum `mx` equals value of given root
        return solution_706_1_2(root, root.val, root.val)