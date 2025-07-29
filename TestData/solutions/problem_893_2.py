class Solution:
	def solution_893_2(self, s: str, t: str) -> int:

		common = Counter(s) &amp; Counter(t)
		count = sum(common.values())

		return len(s) - count