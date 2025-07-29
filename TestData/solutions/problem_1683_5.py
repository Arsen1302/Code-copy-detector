class Solution:
    def solution_1683_5(self, grid: List[List[int]]) -> int:
        mx = 0
        i = 1
        j = 1
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                s = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] +  grid[i][j] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                mx = max(mx,s)
        return mx