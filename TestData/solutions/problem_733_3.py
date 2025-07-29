class Solution:
    def solution_733_3(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) # dimensions 
        score = [0]*m
        
        for j in range(1, n): 
            for i in range(m):
                score[i] *= 2
                if matrix[i][0] != matrix[i][j]: score[i] += 1
                    
        freq = {}
        for x in score: freq[x] = 1 + freq.get(x, 0)
        return max(freq.values())