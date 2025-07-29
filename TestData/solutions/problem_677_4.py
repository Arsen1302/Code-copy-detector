class Solution(object):
	def solution_677_4(self, N, trust):
		if trust==[] and N==1:
			return 1
		x1 = [x[1] for x in trust]
		x0 = [x[0] for x in trust]
		for i in range(1, N+1):
			if i in x1:
				if x1.count(i)==(N-1):
					if i not in x0:
						return i
		return -1