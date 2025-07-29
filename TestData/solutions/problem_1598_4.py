class Solution:
	def solution_1598_4(self, s: str) -> int:
		if '*' not in s:
			return 0
		else:
			c=0
			bars=0
			for i in range(0,len(s)):
				if s[i]=="|":
					bars=bars+1
				if bars%2==0 and s[i]=="*":
					c=c+1
			return c