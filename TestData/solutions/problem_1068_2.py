class Solution:
    def solution_1068_2(self, mat: List[List[int]]) -> int:
        
        M, N, result = len(mat), len(mat[0]), 0
                
        mat_t = list(zip(*mat)) # transpose
        
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1 and \
                sum(mat[i]) == 1 and \
                sum(mat_t[j]) == 1:
                    result += 1
                            
        return result