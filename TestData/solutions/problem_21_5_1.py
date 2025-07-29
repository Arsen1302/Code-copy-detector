class Solution:
	"""
	Time:   O(n)
	Memory: O(log(n))
	"""

	def solution_21_5_1(self, nums: List[int]) -> Optional[TreeNode]:
		return self.solution_21_5_2(0, len(nums) - 1, nums)

	@classmethod
	def solution_21_5_2(cls, left: int, right: int, nums: List[int]) -> Optional[TreeNode]:
		if left <= right:
			mid = (left + right) // 2
			return TreeNode(
				val=nums[mid],
				left=cls.solution_21_5_2(left, mid - 1, nums),
				right=cls.solution_21_5_2(mid + 1, right, nums),
			)