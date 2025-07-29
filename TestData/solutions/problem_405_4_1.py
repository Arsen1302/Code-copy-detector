class Solution:
    def solution_405_4_1(self, n: int, k: int, row: int, column: int) -> float:
        def solution_405_4_2(i, j):
            oox = i < 0 or i >= n
            ooy = j < 0 or j >= n
            return oox or ooy

        steps = [
            (2, 1),
            (-2, 1),
            (2, -1),
            (-2, -1),
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
        ]
        
        @cache
        def solution_405_4_3(i, j, k):
            if solution_405_4_2(i, j):
                return (0, 1)
            if k == 0:
                return (1, 0)
            
            total = [0, 0]
            for dx, dy in steps:
                x, y = i + dx, j + dy
                success, failure = solution_405_4_3(x, y, k - 1)
                total[0] += success
                total[1] += failure
            return total

        success, failure = solution_405_4_3(row, column, k)
        return success / float(8 ** k)