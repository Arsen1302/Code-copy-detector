class Solution:
	def solution_174_3(self, s: List[str]) -> None:
		N = len(s)
		for i in range(N // 2):
			s[i], s[-i-1] == s[-i-1], s[i]