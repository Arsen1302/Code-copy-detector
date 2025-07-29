class Solution:
	def solution_467_2(self, start: str, end: str) -> bool:
		i=j=0
		n=len(start)
		while i<n or j<n:
			while i<n and start[i]=='X':
				i+=1
			while j<n and end[j]=='X':
				j+=1
			if i==n or j==n:
				return i==j
			if start[i]!=end[j]:
				return False
			if (start[i]=='L' and j>i) or (start[i]=='R' and i>j):
				return False
			i+=1
			j+=1
		return True