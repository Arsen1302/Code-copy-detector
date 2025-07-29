class Solution:
    def solution_359_3(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
		if root1 is None and root2 is None:
            return None
        
        # catching the values of root nodes, if root absert, assign 0
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        
        # creating a new node off of these values
        new_node = TreeNode(v1+v2)
        
        # Fetching the Left Subtree Nodes
        root1_left = root1.left if root1 else None
        root2_left = root2.left if root2 else None
        # merging the Left Subtree
        new_node.left = self.solution_359_3(root1_left, root2_left)
        
        # Fetching the Right Subtree Nodes
        root1_right = root1.right if root1 else None
        root2_right = root2.right if root2 else None
        # merging the Left Subtree
        new_node.right = self.solution_359_3(root1_right, root2_right)
        
        # return the Node created
        return new_node