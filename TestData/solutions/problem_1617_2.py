class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	def solution_1617_2(self, nums: List[int]) -> List[int]:
		pairs = 0
		single = set()

		for num in nums:
			if num in single:
				single.remove(num)
				pairs += 1
			else:
				single.add(num)

		return [pairs, len(single)]