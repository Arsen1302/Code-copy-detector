class Solution:
	def solution_394_1_1(self, root: TreeNode) -> int:
		def solution_394_1_2(root):
			if not root:
				return []
			else:
				return solution_394_1_2(root.left) + [root.val] + solution_394_1_2(root.right)
		r = set(solution_394_1_2(root))
		if len(r)>=2:
			return sorted(list(r))[1]
		else:
			return -1