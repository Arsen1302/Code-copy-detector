class Solution:
    def solution_970_2_1(self, root: TreeNode) -> int:
        # Our counter for the good nodes.
        count = 0
        
        def solution_970_2_2(node, m):
            nonlocal count
			# If we run out of nodes return.
            if not node:
                return
			# If the current node val is >= the largest observed in the path thus far.
            if node.val >= m:
			    # Add 1 to the count and update the max observed value.
                count += 1
                m = max(m, node.val)
			# Traverse l and r subtrees.
            solution_970_2_2(node.left, m)
            solution_970_2_2(node.right, m)
                
        solution_970_2_2(root, root.val)
        return count