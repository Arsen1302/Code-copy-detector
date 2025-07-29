class Solution:
	def solution_863_4(self, s: str) -> int:
		w1 = s
		m = len(s)
		w2 = s[::-1]
		n = len(s)

		t = [[-1 for i in range(n + 1)] for j in range(m + 1)]

		for i in range(m + 1):
			for j in range(n + 1):
				if i ==0 or j ==0:
					t[i][j] = 0 

		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if w1[i - 1] == w2[j - 1]:
					t[i][j] = 1 + t[i - 1][j - 1]
				else:
					t[i][j] = max(t[i - 1][j], t[i][j - 1])
		res = (m - t[m][n] )
		return res