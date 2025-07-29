class Solution:
    def solution_579_2_1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def solution_579_2_2(i, j):
            v = grid[i][j]
            if v == 0:
                return 0

            up = min(v, grid[i - 1][j]) if i else 0
            right = min(v, grid[i][j + 1]) if j < n - 1 else 0
            down = min(v, grid[i + 1][j]) if i < n - 1 else 0
            left = min(v, grid[i][j - 1]) if j else 0

            return 2 + 4*v - up - right - down - left
        
        return sum(solution_579_2_2(i, j) for i in range(n) for j in range(n))