class Solution:
    def solution_342_2_1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7

        @lru_cache(None)
        def solution_342_2_2(move, row, col):
            if row == m or row < 0 or col == n or col < 0:
                return 1
            if move == 0:
                return 0
            move -= 1
            return (
                solution_342_2_2(move, row, col + 1)
                + solution_342_2_2(move, row, col - 1)
                + solution_342_2_2(move, row - 1, col)
                + solution_342_2_2(move, row + 1, col)
            ) % modulo
        return solution_342_2_2(maxMove, startRow, startColumn)