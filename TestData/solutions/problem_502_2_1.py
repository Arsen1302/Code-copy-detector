class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	def solution_502_2_1(self, root: TreeNode) -> TreeNode:
		return self.solution_502_2_2(root)

	@classmethod
	def solution_502_2_2(cls, root: Optional[TreeNode]) -> Optional[TreeNode]:
		if not root:
			return None

		root.left = cls.solution_502_2_2(root.left)
		root.right = cls.solution_502_2_2(root.right)

		return root if (root.val or root.left or root.right) else None