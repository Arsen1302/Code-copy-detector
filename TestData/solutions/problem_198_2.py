class Solution:
	def solution_198_2(self, s: str) -> int:

		frequency = {}

		for char in s:

			if char not in frequency:
				frequency[char] = 1
			else:
				frequency[char] = frequency[char] + 1

		for index in range(len(s)):

			if frequency[s[index]] == 1:
				return index

		return -1