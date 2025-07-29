class Solution:
	def solution_1097_5(self, s: str) -> int:

		seen = {}
		maxLen = -1

		for idx, char in enumerate(s):
			if char in seen:
				maxLen = max(maxLen, idx - seen[char] - 1)
			else:
				seen[char] = idx

		return maxLen