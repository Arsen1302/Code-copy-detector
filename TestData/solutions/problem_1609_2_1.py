class Solution:
    def solution_1609_2_1(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dir = [[1,0],[0,1],[-1,0],[0,-1]]

        dp = {}

        def solution_1609_2_2(r,c):
            
            if (r,c) in dp:
                return dp[(r,c)]
                
            ans = 1
            for dr,dc in dir:
                if 0<=r+dr<ROWS and 0<=c+dc<COLS and grid[r+dr][c+dc]>grid[r][c]:
                    ans += solution_1609_2_2(r+dr,c+dc)
            
            dp[(r,c)] = ans%1000000007

            return ans%1000000007

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += solution_1609_2_2(r,c)

        return res%1000000007