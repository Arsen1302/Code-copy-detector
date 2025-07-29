class Solution:
	"""
	Time:   O(n*m)
	Memory: O(n*m)
	"""

	MOVES = [(-1, 0), (0, -1), (1, 0), (0, 1)]

	def solution_226_3_1(self, heights: List[List[int]]) -> Set[Tuple[int, int]]:
		def solution_226_3_2(i: int, j: int, visited: set):
			visited.add((i, j))
			for di, dj in self.MOVES:
				x, y = i + di, j + dj
				if 0 <= x < n and 0 <= y < m and (x, y) not in visited and heights[i][j] <= heights[x][y]:
					solution_226_3_2(x, y, visited)

		n, m = len(heights), len(heights[0])

		atl_visited = set()
		pas_visited = set()

		for i in range(n):
			solution_226_3_2(i,     0, pas_visited)
			solution_226_3_2(i, m - 1, atl_visited)

		for j in range(m):
			solution_226_3_2(    0, j, pas_visited)
			solution_226_3_2(n - 1, j, atl_visited)

		return atl_visited &amp; pas_visited