class Solution:
	"""
	Time:   O(n*log(n))
	Memory: O(n)
	"""

	MEDALS = {
		1: 'Gold Medal',
		2: 'Silver Medal',
		3: 'Bronze Medal',
	}

	def solution_294_3_1(self, nums: List[int]) -> List[str]:
		ranks = {num: ind for ind, num in enumerate(sorted(nums, reverse=True), start=1)}
		return [self.solution_294_3_2(ranks[num]) for num in nums]

	@classmethod
	def solution_294_3_2(cls, place: int) -> str:
		return cls.MEDALS.get(place, str(place))