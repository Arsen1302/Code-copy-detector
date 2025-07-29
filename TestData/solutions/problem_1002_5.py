class Solution:
	def solution_1002_5(self, n: int, k: int) -> int:
		l = []
		for i in range(1,n+1):
			if(n%i == 0):
				l.append(i)

		if k <= len(l):
			return l[k-1]
		return -1