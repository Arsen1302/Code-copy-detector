class Solution:
	def solution_121_5_1(self):
		self.ans = None

	def solution_121_5_2(self, root, p, q):

		def solution_121_5_3(node):
			if not node:
				return False

			left = solution_121_5_3(node.left)
			right = solution_121_5_3(node.right)

			mid = node == p or node == q

			if mid + left + right >= 2:
				self.ans = node

			return mid or left or right

		solution_121_5_3(root)
		return self.ans