class Solution:
    def solution_918_1 (self, matrix: List[List[int]]) -> List[int]:
        rmin = [min(x) for x in matrix]
        cmax = [max(x) for x in zip(*matrix)]
        return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if rmin[i] == cmax[j]]