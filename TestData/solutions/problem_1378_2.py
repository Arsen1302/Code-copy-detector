class Solution:
    def solution_1378_2(self, grid: List[List[int]]) -> int:
        ans = inf
        prefix = 0
        suffix = sum(grid[0])
        for i in range(len(grid[0])): 
            suffix -= grid[0][i]
            ans = min(ans, max(prefix, suffix))
            prefix += grid[1][i]
        return ans