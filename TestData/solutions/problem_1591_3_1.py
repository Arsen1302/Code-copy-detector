class Solution:
    def solution_1591_3_1(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache()
        def solution_1591_3_2(i, j):
            if i == 0:
                return grid[i][j]
            else:
                return grid[i][j] + min(moveCost[grid[i - 1][k]][j] + solution_1591_3_2(i - 1, k) for k in range(n))
        
        return min(solution_1591_3_2(m - 1, j) for j in range(n))