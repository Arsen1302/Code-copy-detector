class Solution:
	def solution_1113_5(self, s: str) -> int:

		d = {}
		result = 0
		visted = []

		for char in s:
		
			if char not in d:
				d[char] = 1
			else:
				d[char] = d[char] + 1

		d = dict(sorted(d.items(), key = lambda x : x[1]))

		for i in d:
		
			if d[i] not in visted:
				visted.append(d[i])
			else:
				while d[i] != 0:

					if d[i] not in visted:
						visted.append(d[i])
						break

					d[i] = d[i] - 1
					
					result = result + 1

		return result