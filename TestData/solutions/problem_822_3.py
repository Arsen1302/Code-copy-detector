class Solution:
    def solution_822_3(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(indices)):
            for k in range(2):
                if k == 0:
                    for j in range(n):
                        matrix[indices[i][0]][j] += 1
                else:
                    for j in range(m):
                        matrix[j][indices[i][1]] += 1
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 != 0:
                    count += 1
        return count