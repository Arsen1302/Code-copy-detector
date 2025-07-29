class Solution:
    def solution_1564_3_1(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def solution_1564_3_2(i, j, score):
            if i == m or j == n:
                return False
            if i == m - 1 and j == n - 1:
                return score == 1 and grid[i][j] == ')'
            
            if grid[i][j] == '(':
                return solution_1564_3_2(i + 1, j, score + 1) or solution_1564_3_2(i, j + 1, score + 1)
            if score == 0:
                return False
            return solution_1564_3_2(i + 1, j, score - 1) or solution_1564_3_2(i, j + 1, score - 1)
        
        return solution_1564_3_2(0, 0, 0)