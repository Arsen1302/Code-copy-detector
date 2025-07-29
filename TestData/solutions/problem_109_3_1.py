class Solution:
	def solution_109_3_1(self, root: Optional[TreeNode]) -> int:

		def solution_109_3_2(node):

			if node == None:
				return 0

			queue = [node]
			self.result = 0

			while queue:

				current_node = queue.pop()
				self.result = self.result + 1

				if current_node.left != None:
					queue.append(current_node.left)
				if current_node.right != None:
					queue.append(current_node.right)

			return self.result

		return solution_109_3_2(root)