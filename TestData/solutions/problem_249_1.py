class Solution:
    def solution_249_1(self, root: TreeNode, key: int) -> TreeNode:
        
        if not root:
            return None
            
        if root.val > key:
		    # Target node is smaller than currnet node, search left subtree
			
            root.left = self.solution_249_1( root.left, key )

        elif root.val < key:
		    # Target node is larger than currnet node, search right subtree
			
            root.right = self.solution_249_1( root.right, key )

        else:
            # Current node is target node
			
            if (not root.left) or (not root.right):
                # At least one child is empty
                # Target node is replaced by either non-empty child or None
                root = root.left if root.left else root.right

            else:
                # Both two childs exist
                # Target node is replaced by smallest element of right subtree
                cur = root.right

                while cur.left:
                    cur = cur.left

                root.val = cur.val
                root.right = self.solution_249_1( root.right, cur.val )
                    
        return root