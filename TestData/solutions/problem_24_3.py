class Solution:
    def solution_24_3(self, root: TreeNode) -> int:
        
        if not root:
			# base case for empty node or empty tree
            return 0
        
        if not root.left and not root.right:
			# leaf node
            return 1
        
        elif not root.right:
			# only has left sub-tree
            return self.solution_24_3(root.left) + 1
        
        elif not root.left:
			# only has right sub-tree
            return self.solution_24_3(root.right) + 1
        
        else:
			# has left sub-tree and right sub-tree
            return min( map(self.solution_24_3, (root.left, root.right) ) ) + 1