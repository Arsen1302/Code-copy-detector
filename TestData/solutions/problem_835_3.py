class Solution:
def solution_835_3(self, matrix: List[List[int]]) -> int:
    
    m=len(matrix)
    n=len(matrix[0])
    
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j]:
                matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
    res=0
    for p in range(m):
        res+=sum(matrix[p])
    
    return res