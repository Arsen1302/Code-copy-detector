class Solution:
	def solution_968_5(self, s: str) -> int:
		max_count = 1
		count = 1
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				count+=1

			else:
				count = 1

			max_count = max(max_count, count)
		return max_count