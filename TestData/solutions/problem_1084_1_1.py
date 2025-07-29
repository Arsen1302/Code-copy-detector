class Solution:
    def solution_1084_1_1(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        def solution_1084_1_2(y, x):
            choice = min(rowSum[y], colSum[x])
            result[y][x] = choice
            rowSum[y] -= choice
            colSum[x] -= choice
            if y == 0 and x == 0:
                return

            elif not rowSum[y]:
                solution_1084_1_2(y - 1, x)
            elif not colSum[x]:
                solution_1084_1_2(y, x - 1)

        Y, X = len(rowSum), len(colSum)
        result = [[0 for _ in range(X)] for _ in range(Y)]
        solution_1084_1_2(Y-1, X-1)
        return result