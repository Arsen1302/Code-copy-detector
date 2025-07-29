class Solution:
	"""
	Time:   O(n^2)
	Memory: O(1)
	"""

	def solution_1639_3_1(self, grid: List[List[int]]) -> List[List[int]]:
		n = len(grid)
		return [[self.solution_1639_3_2(grid, r, c, 1) for c in range(1, n - 1)] for r in range(1, n - 1)]

	@staticmethod
	def solution_1639_3_2(grid: List[List[int]], row: int, col: int, radius: int) -> int:
		return max(
			grid[r][c]
			for r in range(row - radius, row + radius + 1)
			for c in range(col - radius, col + radius + 1)
		)