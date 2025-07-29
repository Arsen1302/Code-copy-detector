class Solution:
    def solution_1278_5_1(self, grid: List[List[int]]) -> List[int]:
        run = set()
        n = len(grid)
        m = len(grid[0])
        
        # Loop through every grid item
        for i in range(n):
            for j in range(m):
                # Calculate the max rhombus around the current grid item
                res = self.solution_1278_5_2(grid, i, j, len(grid), len(grid[0]))
                # Add to list of sums
                run.add(res)
        
        res = []
        # Stupid way of getting biggest 3,
        # a heap would work better but the problem
        # isn't here
        return sorted(run, reverse=True)[:3]
    
    # This function calculates the width of the largest
    # rhombus that can be made around the given grid row and col.
    
    # Then it calculates each rhombus that can be made up until that max width,
    # keeping track of what the largest sum is amongst all the created rhombuses,
    # and returns the max
    def solution_1278_5_2(self, grid, row, col, n, m):
        # Calculate how wide the largest rhombus can be.
        # it is the smaller number of how close are you to the 
        # nearest edge of row, or nearest edge of column
        distance = min(n - row, m - col)
        
        # set the max perimeter sum to the current number
        global_max = grid[row][col]
        
        # From 1 to the width of the biggest rhombus that can be made
        for i in range(1, distance):
            # check 4 corners, if not 4 corners, no rhombus can be made at current distance
            if row - i >= 0 and row + i < n and col - i >= 0 and col + i < m:
                top_point = row - i
                bottom_point = row + i
                
                # Add up the vertices (points)
                local_max = grid[row-i][col] + grid[row+i][col] + grid[row][col-i] + grid[row][col+i]
                
                # For 1 up to the width of the current rhombus,
                # add up the perimeter
                for j in range(1,i):
                    local_max += grid[top_point + j][col - j] + grid[top_point + j][col+j]
                    local_max += grid[bottom_point - j][col-j] + grid[bottom_point - j][col + j]
                
                # Save the bigger perimeter sum
                global_max = max(global_max, local_max)
            else:
                break
        return global_max