class Solution:
	def solution_317_1_1(self, root: TreeNode) -> TreeNode:
		sum = 0
		
		def solution_317_1_2(root: TreeNode) -> TreeNode:
			nonlocal sum
			if root:
				solution_317_1_2(root.right)
				root.val += sum
				sum = root.val
				solution_317_1_2(root.left)
			return root
		
		return solution_317_1_2(root)