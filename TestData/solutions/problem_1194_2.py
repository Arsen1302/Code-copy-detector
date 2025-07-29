class Solution:
	def solution_1194_2(self, s: str) -> int:
		count = 0
		for i, j in itertools.groupby(s):
			temp = len(list(j))
			count += (temp * (temp + 1)) // 2

		return count % (10 ** 9 + 7)