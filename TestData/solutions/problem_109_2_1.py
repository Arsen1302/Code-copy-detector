class Solution:
	def solution_109_2_1(self, root: Optional[TreeNode]) -> int:

		self.result = 0

		def solution_109_2_2(node):

			if node == None:
				return None

			self.result = self.result + 1

			solution_109_2_2(node.left)
			solution_109_2_2(node.right)

		solution_109_2_2(root)
		return self.result