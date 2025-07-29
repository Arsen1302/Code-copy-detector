class Solution:
	"""
	Time:   O(n)
	Memory: O(n)
	"""

	@lru_cache(maxsize=None)
	def solution_764_4(self, n: int) -> int:
		if n < 1:
			return 0
		if n < 3:
			return 1
		return self.solution_764_4(n - 1) + self.solution_764_4(n - 2) + self.solution_764_4(n - 3)


class Solution:
	"""
	Time:   O(n)
	Memory: O(1)
	"""

	def solution_764_4(self, n: int) -> int:
		a, b, c = 0, 1, 1
		for _ in range(n):
			a, b, c = b, c, a + b + c
		return a