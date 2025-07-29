class Solution:
	def solution_1039_5(self, s: str) -> int:

		res = 0
		stack = []
		i = 0
		h = { '(' : "))"}

		# loop through string
		while i < len(s):
			curChar = s[i]

			# if the char is (, we can just append, update idx and continue
			if curChar == '(':
				stack.append(curChar)
				i += 1
				continue

			# if our char is closing, get next char
			nextChar = (s[i+1] if i+1 < len(s) else 'a')
			# if nextChar isn't closing, we need an insertion, if not we can skip next char so increment i
			if nextChar != ')':
				res += 1
			else:
				i += 1

			# if something in stack, pop it, else we need an insertion, increment
			if stack:
				stack.pop()
			else:
				res += 1

			i += 1

		# all remaining opening in stack will need two closing, return res + len(stack) *2
		return res + (len(stack) * 2)