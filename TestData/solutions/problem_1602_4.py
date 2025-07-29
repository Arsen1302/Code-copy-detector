class Solution:
    def solution_1602_4(self, grid: List[List[int]]) -> bool:
        r = len(grid)
        c = len(grid[0])
        for m in range(r):
            for n in range(c):
                if (m==n and grid[m][n]==0) or (m==((r-1)-n) and grid[m][n]==0):return False
                elif not(m==n or m==((r-1)-n)) and grid[m][n]!=0:return False
        return True