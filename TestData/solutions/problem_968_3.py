class Solution:
	def solution_968_3(self, s: str) -> int:
		maxi = 0
		for i, j in itertools.groupby(s):
			temp = len(list(j))
			if temp > maxi:
				maxi = temp
		return maxi