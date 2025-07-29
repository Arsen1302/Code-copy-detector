class Solution:
	def solution_1210_3_1(self, n: int) -> bool:
		p = [3**i for i in range(16)]
		return self.solution_1210_3_2(0, 0, [], n, p[:(bisect.bisect_left(p, n)+1)])
    
	def solution_1210_3_2(self, idx, cur, cc, n, p):
		for i in range(idx, len(p)):
			cur += p[i]
			cc.append(p[i])
			if cur == n or (cur < n and self.solution_1210_3_2(i+1, cur, cc, n, p)):
				return True
			cur -= p[i]
			cc.pop()

		return False