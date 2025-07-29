class Solution:
    def solution_1591_2_1(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:

        @lru_cache()
        def solution_1591_2_2(i, j):
            if i >= len(grid) - 1:
                return grid[i][j]
            
            m_cost = 9999999999
            cost = 0

            for k in range(len(grid[0])):
                cost = grid[i][j] + moveCost[grid[i][j]][k] + solution_1591_2_2(i + 1, k)
                m_cost = min(cost, m_cost)

            return m_cost

        cost, min_cost = 0, 999999999999
        n = len(grid[0])
        for j in range(n):
            cost = solution_1591_2_2(0, j)
            min_cost = min(cost, min_cost)

        return min_cost