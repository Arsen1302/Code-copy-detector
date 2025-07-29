class Solution:
	def solution_154_5(self, s: str) -> str:

		LastIndex = {}

		for i in range(len(s)):
			LastIndex[s[i]] = i

		stack = []
		AlreadySeen = set()

		for i in range(len(s)):

			if s[i] in AlreadySeen:
				continue
			else:
				while stack and stack[-1] > s[i] and LastIndex[stack[-1]] > i:

					AlreadySeen.remove(stack[-1])
					stack.pop()

			stack.append(s[i])
			AlreadySeen.add(s[i])

		return ''.join(stack)