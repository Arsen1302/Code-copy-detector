class Solution:
	@staticmethod
	def solution_249_5_1(node):    '''Finds inorder successor'''
		if node.left:
			return Solution.solution_249_5_1(node.left)
		return node.val

	def solution_249_5_2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
		if not root:
			return root
		if root.val == key:
			if not root.left:
				return root.right
			if not root.right:
				return root.left
			root.val = Solution.solution_249_5_1(root.right)     '''Copying inorder successor value'''
			root.right = self.solution_249_5_2(root.right,root.val)  
			return root
		if root.val > key:
			root.left = self.solution_249_5_2(root.left,key)
		else:
			root.right = self.solution_249_5_2(root.right,key)
		return root
		
		'''If any doubt regarding solution please ask in comment section 
		  if you like it please upvote '''