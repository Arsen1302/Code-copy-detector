class Solution:
    def solution_554_5(self, matrix: List[List[int]]) -> List[List[int]]:
        m= len(matrix)
        n = len(matrix[0])
        Transpose=[[0]*m for i in range(n)]
        for i in range(m):
            for j in range(n):
                Transpose[j][i]=matrix[i][j]
        return(Transpose)