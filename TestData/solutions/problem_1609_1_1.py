class Solution:
    def solution_1609_1_1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = {}
        mod = (10 ** 9) + 7

        def solution_1609_1_2(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] <= prev:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            pathLength = 1
            pathLength += (solution_1609_1_2(r + 1, c, grid[r][c]) + solution_1609_1_2(r - 1, c, grid[r][c]) +
                solution_1609_1_2(r, c + 1, grid[r][c]) + solution_1609_1_2(r, c - 1, grid[r][c]))
            dp[(r, c)] = pathLength
            return pathLength
            
        count = 0
        for r in range(rows):
            for c in range(cols):
                count += solution_1609_1_2(r, c, 0)

        return count % mod