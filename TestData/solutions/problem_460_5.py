class Solution:
    def solution_460_5(self, matrix: List[List[int]]) -> bool:
        r= len(matrix)
        for i in range(1,r):
            for j in range(1,len(matrix[0])):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True