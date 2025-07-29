class Solution:
	def solution_723_2_1(self, s: str) -> str:

		def solution_723_2_2(window):
			visit = set()
			for i in range(0, len(s) - window):
				substring = s[i : i + window + 1]
				if substring in visit:
					return substring
				visit.add(substring)

			return None

		l, r = 0, len(s) - 1
		res = ""

		while l < r:
			mid = l + (r - l) // 2
			duplicate = solution_723_2_2(mid)

			if duplicate:
				res = duplicate
				l = mid + 1
			else:
				r = mid

		return res