class Solution:                 # The plan is to iterate through grid, a 2D array, and if we find
                                # a cell in grid has value 1, then we recognize this cell as the
                                # first cell on an unexplored island, start an area count (res) and
                                # mark this first cell as visited (with a -1) in grid.

                                # A cell in the grid is connected to the first cell if there is a path of 1s from
								# the first cell to the this cell. We solution_411_4_2 recursively in each connected
								# cell to this cell looking for values of 1. If a connected cell is in the grid 
								# and its value  is 1, we add it to the area for this island, mark it as visited,
								# and keep exploring. If we get a 0 or -1, we consider that the base case 
                                # for the recursion. Once the island is completely explored, we deteremine
                                # whether the area of this island is greater than the those explored before.

                                # We continue the iteration thoughout the grid to determine the the max.

    def solution_411_4_1(self, grid: list[list[int]]) -> int:
        ans, R, C = 0, range(len(grid)), range(len(grid[0]))  # <-- initialize some stuff for solution_411_4_1
        
        def solution_411_4_2(r: int, c: int)->int:                     # <-- The recursive function
            grid[r][c], res, dr, dc = -1, 0, 1, 0             # <-- dr, dc = 1,0 sets the initial direction as south

            for _ in range(4):
                row, col = r+dr, c+dc
                if row in R and col in C and grid[row][col] == 1:
                    res+= solution_411_4_2(row, col)
				dr, dc = dc, -dr                              # <--- this transformation rotates the direction though the 
                                                              # sequence south, west, north, east
            return 1+res        
        
        for r in R:                                           # <--- the iteration through the grid
            for c in C:
                if grid[r][c] >= 1:
                    ans = max(solution_411_4_2(r,c), ans)       
        return ans
		
		# My thanks to fouad399 for catching an error in the original post