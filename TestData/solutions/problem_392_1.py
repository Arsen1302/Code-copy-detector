class Solution:
	def solution_392_1(self, root: TreeNode, low: int, high: int) -> TreeNode:
		if not root: return root
		if root.val < low: return self.solution_392_1(root.right, low, high)
		if root.val > high: return self.solution_392_1(root.left, low, high)
		root.left = self.solution_392_1(root.left, low, high)
		root.right = self.solution_392_1(root.right, low, high)
		return root