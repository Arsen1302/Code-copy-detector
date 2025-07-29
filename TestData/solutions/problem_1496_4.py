class Solution:
	def solution_1496_4(self, f: int) -> List[int]:

		if f%2:
			return []

		res, i = [], 2
		while i<=f:
			res.append(i)
			f -= i
			i += 2

		res[-1]+=f
		return res