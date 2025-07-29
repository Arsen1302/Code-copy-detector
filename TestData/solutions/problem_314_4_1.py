class Solution:
    def solution_314_4_1(self, root: TreeNode) -> int:
        
        res = []
        
        def solution_314_4_2(node, vals, minn):
		    # If we find a min diff of 1 we can return (given properties of BST + abs diff)
			# we know this is the lowest result we can find.
            if minn == 1:
                return True
            if not node:
			    # If we run out of nodes append the min diff we found on this path 
				# and return False because we didn't find 1.
                res.append(minn)
                return False
			# Otherwise we see if theres a smaller difference with the current node and what we've seen so far.
            if vals:
                for i in vals:
                    if abs(node.val - i) < minn:
                        minn = abs(node.val - i)
			# Recurse subtrees and return if we found 1 in either subtree.
            return solution_314_4_2(node.left, vals + [node.val], minn) or \
            solution_314_4_2(node.right, vals + [node.val], minn)
         
		# We know we found 1 if our func. returns True else we'll take the min of the mins we found.
        return 1 if solution_314_4_2(root, [], float('inf')) else min(res)