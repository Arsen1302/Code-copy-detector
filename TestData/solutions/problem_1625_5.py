class Solution:
    def solution_1625_5(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        ans = 0
        for i in range(n):
            res = []
            for j in range(n):
                res = []
                for k in range(n):
                    res.append(grid[k][j])
                if res == grid[i]:
                    ans += 1
        
        return ans