class Solution:
    def solution_215_2(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        queue = collections.deque([root])
        res = 0
        
        while queue:
            node = queue.popleft()
            if node:
			    # check if the current node has a left child
				# and that left child is a leaf, if yes, consider it
                if node.left and not node.left.left and not node.left.right:
                    res += node.left.val
				
				# irrespectively, add the children
				# of the current node to continue
				# your bfs exploration further
                queue.append(node.left)
                queue.append(node.right)
                
        return res