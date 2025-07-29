class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	def solution_1617_1(self, nums: List[int]) -> List[int]:
		pairs = sum(cnt // 2 for cnt in Counter(nums).values())
		return [pairs, len(nums) - 2 * pairs]