class Solution:
	"""
	Time:   O(n^2)
	Memory: O(n)
	"""

	def solution_324_4(self, isConnected: List[List[int]]) -> int:
		n = len(isConnected)
		dsu = DSU(n)

		for i in range(n):
			for j in range(n):
				if isConnected[i][j]:
					dsu.union(i, j)

		return len({dsu.find(i) for i in range(n)})