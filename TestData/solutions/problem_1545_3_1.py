class Solution:
	def solution_1545_3_1(self, s: str, k: int) -> str:
		"""Iterative version"""
		while len(s) > k:
			s = self.solution_1545_3_2(s, k)
		return s

	def solution_1545_3_1(self, s: str, k: int) -> str:
		"""Recursive version"""
		if len(s) <= k:
			return s
		return self.solution_1545_3_1(self.solution_1545_3_2(s, k), k)

	@classmethod
	def solution_1545_3_2(cls, s: str, k: int) -> str:
		return ''.join(map(cls.solution_1545_3_3, cls.solution_1545_3_4(s, k)))

	@staticmethod
	def solution_1545_3_3(s: str) -> str:
		return str(sum(int(d) for d in s))

	@staticmethod
	def solution_1545_3_4(s: str, k: int):
		for i in range(0, len(s), k):
			yield s[i:i + k]