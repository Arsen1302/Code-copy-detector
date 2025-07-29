class Solution:
	def solution_417_5(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		new, origin = TreeNode(val), root
		if not root: return new

		while root:
			prev = root
			if val > root.val: root = root.right
			else: root = root.left

		if val > prev.val: prev.right = new
		else: prev.left = new

		return origin