class Solution:
    def solution_559_1_1(self):
        self.n = []
        
    def solution_559_1_2(self, root):
        if root:
			# checking if the node is leaf
            if not root.left and not root.right:  
				# appends the leaf nodes to the list - self.n 
                self.n.append(root.val)  
				
            self.solution_559_1_2(root.left)
            self.solution_559_1_2(root.right)
            
    def solution_559_1_3(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.solution_559_1_2(root1)
        a = self.n
        self.n = []
        self.solution_559_1_2(root2)
        
        if a == self.n:
            return True
        else:
            return False