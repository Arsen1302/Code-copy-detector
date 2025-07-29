class Solution:
	def solution_909_5(self, s: str) -> str:
		string, memo = sorted(set(s)), Counter(s)
		result = ""
		count = 0

		while len(result) < len(s):
			if count == 0:
				for char in string:
					if memo[char] == 0: continue
					result += char
					memo[char] -= 1

				count += 1

			if count == 1:
				for char in string[::-1]:
					if memo[char] == 0: continue
					result += char
					memo[char] -= 1

				count -=1

		return result