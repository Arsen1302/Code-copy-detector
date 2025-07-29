class Solution:
    def solution_322_1_1(self):
	    self.diameter = 0  # stores the maximum diameter calculated
	
    def solution_322_1_2(self, node: Optional[TreeNode]) -> int:
        """
        This function needs to do the following:
            1. Calculate the maximum solution_322_1_2 of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        # Calculate maximum solution_322_1_2
        left = self.solution_322_1_2(node.left) if node.left else 0
        right = self.solution_322_1_2(node.right) if node.right else 0
        # Calculate diameter
        if left + right > self.diameter:
            self.diameter = left + right
        # Make sure the parent node(s) get the correct solution_322_1_2 from this node
        return 1 + (left if left > right else right)
    
    def solution_322_1_3(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        self.solution_322_1_2(root)  # root is guaranteed to be a TreeNode object
        return self.diameter