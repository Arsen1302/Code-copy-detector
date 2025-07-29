class Solution:
	def solution_392_3_1(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

		def solution_392_3_2(node):

			if node == None:
				return None

			elif node.val > high : 
				return solution_392_3_2(node.left)

			elif node.val < low : 
				return solution_392_3_2(node.right)

			else:
				node.left = solution_392_3_2(node.left)
				node.right = solution_392_3_2(node.right)

				return node

		return solution_392_3_2(root)