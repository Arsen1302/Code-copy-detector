class Solution:
    def solution_673_1(self, root: Optional[TreeNode], x: int, y: int) -> bool:
		# Check if root node is x or y
        if root.val == x or root.val == y:
            return False
		# Prepare for BFS, initialise variables
        curr, flag = [root.left, root.right], False
		
        while curr:
            tmp = []
			# Check nodes two-by-two
            for i in range(0, len(curr), 2):
				# Case 1: x and y are both found
				# This indicates that they have the same parent
                if curr[i] and curr[i+1] and \
                       ((curr[i].val == x and curr[i+1].val == y) or \
                       (curr[i+1].val == x and curr[i].val == y)):
                    return False
				# Case 2: Either one of x or y is found
                elif (curr[i] and (curr[i].val == x or curr[i].val == y)) or \
                        (curr[i+1] and (curr[i+1].val == x or curr[i+1].val == y)):
                    if flag:
						# Previously, the other node has been found in the same depth
						# This is our success condition, return True
                        return True
					# Otherwise, this is the first node in the current depth to be found
                    flag = True
				
				# Simultaneously, we can prepare the nodes for the subsequent depth
				# Note to append both left and right regardless of existence
                if curr[i]:
                    tmp.append(curr[i].left)
                    tmp.append(curr[i].right)
                if curr[i+1]:
                    tmp.append(curr[i+1].left)
                    tmp.append(curr[i+1].right)
			
			# Before we proceed to the next depth, check:
            if flag:
				# One of the nodes has already been found
				# This means that the other node cannot be of the same depth
				# By definition, this means that the two nodes are not cousins
                return False
            curr = tmp  # Assign the new nodes as the current ones
		
		# The program will never reach here since x and y are guaranteed to be found
		# But you can return False if you want