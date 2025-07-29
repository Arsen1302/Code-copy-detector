class Solution:
	def solution_416_4(self, root: TreeNode, val: int) -> TreeNode:
		while root:
			if val < root.val: root = root.left
			elif val > root.val: root = root.right
			else: return root
		return root