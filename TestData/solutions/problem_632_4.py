class Solution:
	def solution_632_4(self, root1: TreeNode, root2: TreeNode) -> bool:

		if not root1: return root2 is None
		if not root2: return False

		return root1.val == root2.val \
			and (self.solution_632_4(root1.left, root2.left) \
			and self.solution_632_4(root1.right, root2.right) \
			or self.solution_632_4(root1.right, root2.left) \
			and self.solution_632_4(root1.left, root2.right))