class Solution:
	def solution_969_5(self, n):
		res = []
		seen = set()
		for z in range(1, n):
			for m in range(z+1, n+1):
				if z/m in seen:
					continue
				seen.add(z/m)
				res.append(str(z)+'/'+str(m))
		return res