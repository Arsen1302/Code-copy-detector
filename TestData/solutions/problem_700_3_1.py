class Solution:
	"""
	Time:   O(n^2)
	Memory: O(n^2)
	"""

	WATER = 0
	LAND = 1

	def solution_700_3_1(self, grid: List[List[int]]) -> int:
		n, m = len(grid), len(grid[0])

		for i in range(n):
			self.solution_700_3_2(i, 0, grid)
			self.solution_700_3_2(i, m - 1, grid)

		for j in range(m):
			self.solution_700_3_2(0, j, grid)
			self.solution_700_3_2(n - 1, j, grid)

		return sum(map(sum, grid))

	@classmethod
	def solution_700_3_2(cls, row: int, col: int, grid: List[List[int]]):
		if grid[row][col] == cls.LAND:
			grid[row][col] = cls.WATER
			if row > 0:
				cls.solution_700_3_2(row - 1, col, grid)
			if row < len(grid) - 1:
				cls.solution_700_3_2(row + 1, col, grid)
			if col < len(grid[0]) - 1:
				cls.solution_700_3_2(row, col + 1, grid)
			if col > 0:
				cls.solution_700_3_2(row, col - 1, grid)