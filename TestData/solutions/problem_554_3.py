class Solution:
    def solution_554_3(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]