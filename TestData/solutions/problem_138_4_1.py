class Solution:
	"""
	Time:   O(n*√n)
	Memory: O(log(n))
	"""

	def solution_138_4_1(self, n: int) -> int:
		return self.solution_138_4_2(n)

	@classmethod
	@lru_cache(None)
	def solution_138_4_2(cls, n: int) -> int:
		if n < 2:
			return n
		return 1 + min(cls.solution_138_4_2(n - i * i) for i in range(1, isqrt(n) + 1))