class Solution:
	"""
	Time:   O(n)
	Memory: O(k)
	"""

	def solution_1643_2(self, blocks: str, k: int) -> int:
		min_cost = cost = blocks[:k].count('W')

		for i in range(k, len(blocks)):
			cost = cost - (blocks[i - k] == 'W') + (blocks[i] == 'W')
			min_cost = min(min_cost, cost)

		return min_cost