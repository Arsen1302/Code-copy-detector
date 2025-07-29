class Solution:
    def solution_1278_3_1(self, grid: List[List[int]]) -> List[int]:
        first = second = third = 0

        def solution_1278_3_2(val):
            nonlocal first, second, third
            if val > first:
                third = second
                second = first
                first = val
            elif first > val > second:
                third = second
                second = val
            elif second > val > third:
                third = val

        rows, cols = len(grid), len(grid[0])
        max_size = max(rows // 2, cols // 2) + 1
        for r in range(rows):
            for c in range(cols):
                solution_1278_3_2(grid[r][c])
                for n in range(1, max_size):
                    if c + 2 * n < cols and r - n >= 0 and r + n < rows:
                        sum_rhombus = (grid[r][c] + grid[r][c + 2 * n] +
                                       grid[r - n][c + n] + grid[r + n][c + n])
                        end_c = c + 2 * n
                        for i in range(1, n):
                            sum_rhombus += (grid[r + i][c + i] +
                                            grid[r - i][c + i] +
                                            grid[r + i][end_c - i] +
                                            grid[r - i][end_c - i])
                        solution_1278_3_2(sum_rhombus)
                    else:
                        break
        biggest = {first, second, third} - {0}
        return sorted(biggest, reverse=True)