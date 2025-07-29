class Solution:
    def solution_843_1(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        min1 = min11 = float('inf')                     # min1 -> minimum , min11 -> second minimum in even indexed row
        min2 = min22 = float('inf')                     # min2 -> minimum , min22 -> second minimum in odd indexed row
        for i in range(rows):
            for j in range(cols):
                if i==0:
                    if grid[i][j]<=min1:                # Logic to find minimum and second minimum
                        min11 = min1
                        min1 = grid[i][j]
                    elif grid[i][j]<min11:
                        min11 = grid[i][j]    
                else:
                    if i%2:
                        if grid[i-1][j]==min1:          # If adjacent -> then add the second minimum value
                            grid[i][j] += min11
                        else:                           # Else -> add the minimum value
                            grid[i][j] += min1
                        if grid[i][j]<min2:             # Logic to find minimum and second minimum
                            min22 = min2
                            min2 = grid[i][j]
                        elif grid[i][j]<min22:
                            min22 = grid[i][j]
                    else:
                        if grid[i-1][j]==min2:
                            grid[i][j] += min22
                        else:
                            grid[i][j] += min2
                        if grid[i][j]<min1:             # Logic to find minimum and second minimum
                            min11 = min1
                            min1 = grid[i][j]
                        elif grid[i][j]<min11:
                            min11 = grid[i][j]    
            if i%2:                                     # Reset the minimum and second minimum values accordingly
                min1 = min11 = float('inf')
            else:
                min2 = min22 = float('inf')
        return min(grid[-1])                            # Return the minimum element in last row