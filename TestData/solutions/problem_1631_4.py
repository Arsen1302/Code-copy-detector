class Solution:
	"""
	Time:   O((n+m)*log(n+m))
	Memory: O(n+m)
	"""

	def solution_1631_4(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
		merged = defaultdict(int)

		for value, weight in first + second:
			merged[value] += weight

		return sorted(merged.items())