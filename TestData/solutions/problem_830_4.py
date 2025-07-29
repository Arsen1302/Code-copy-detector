class Solution:
	def solution_830_4(self, grid: List[List[int]]) -> int:

		ROWS, COLS = len(grid), len(grid[0])
		# store num servers seen in row
		rows = {}
		# store num servers seen in col
		cols = {}
		res = 0   

		# loop through grid and if server in cell, increment the current row and column server count by 1 
		for row in range(ROWS):
			for col in range(COLS):
				if grid[row][col] == 1:
					rows[row] = rows.get(row, 0) + 1
					cols[col] = cols.get(col, 0) + 1

		# loop through grid and if cell is a server and count of servers in row or col is greater than 1, increment res 
		for row in range(ROWS):
			for col in range(COLS):
				if grid[row][col] == 1 and (rows.get(row, 0) > 1 or cols.get(col, 0) > 1):
					res += 1

		return res