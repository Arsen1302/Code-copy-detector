class Solution:
	def solution_1027_4(self, s: str) -> int:
		prefix = [0]*len(s)
		suffix = [0]*len(s)
		unique = set()
		ans = 0

		for index in range(len(s)):
			unique.add(s[index])
			prefix[index] = len(unique)

		unique.clear()
		for index in range(len(s)-1, -1, -1):
			unique.add(s[index])
			suffix[index] = len(unique)

		for index in range(len(s)-1):
			if prefix[index] == suffix[index+1]:
				ans += 1

		return ans