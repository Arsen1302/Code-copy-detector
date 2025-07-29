class Solution:
	def solution_1227_5(self, word: str) -> int:
		parsed = []

		for c in word: 
			if c.isalpha():
				parsed.append(" ")
			else:
				parsed.append(c)
		parsed = ("".join(parsed)).split(" ")
		parsed = [int(c) for c in parsed if c]
		return len(set(parsed))
		
		''' Time: O(n)
			Space: O(n)
		'''