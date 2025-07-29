class Solution:
	def solution_1609_5_1(self, grid: List[List[int]]) -> int:

		dp = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

		def solution_1609_5_2 (r,c):

			if dp[r][c] != 1:

				return dp[r][c]

			adjacent_points = [[r-1,c],[r,c-1],[r+1,c],[r,c+1]]

			for point in adjacent_points:

				x , y = point 

				if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] < grid[r][c]:

					dp[r][c] = dp[r][c] + solution_1609_5_2(x,y)

			return dp[r][c]

		result = 0

		for row in range(len(grid)):

			for col in range(len(grid[0])):

				result = result + solution_1609_5_2(row,col)

		return result % (10 **9 + 7)