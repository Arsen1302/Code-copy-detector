class Solution:
    def solution_912_1_1(self, root: TreeNode) -> int:
        tot = -math.inf

        def solution_912_1_2(node):
            nonlocal tot
            if not node:
                return 0, math.inf, -math.inf 
            l_res, l_min, l_max = solution_912_1_2(node.left)
            r_res, r_min, r_max = solution_912_1_2(node.right)
			# if maintains BST property
            if l_max<node.val<r_min:
                res = node.val + l_res + r_res
                tot = max(tot, res)
				# keep track the min and max values of the subtree
                return res, min(l_min,node.val), max(r_max, node.val)
            else:
                return 0, -math.inf, math.inf
        
        return max(solution_912_1_2(root)[0], tot)