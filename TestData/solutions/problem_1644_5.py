class Solution:
	def solution_1644_5(self, s: str) -> int:
		count = 0
		while "01" in s:
			"""
			While we are getting "01" in the string
			we will replace them into "10"
			and count the number of occurrence
			"""
			s = s.replace("01", "10")
			count += 1
		return count