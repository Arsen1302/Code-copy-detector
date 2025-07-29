class Solution:
    def solution_835_1(self, matrix: List[List[int]]) -> int:
        
        count=matrix.count(1)
        count=0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==1:
                    count+=1
                if r==0 or c==0: continue
                
                old_val=matrix[r][c]
                matrix[r][c]=min(matrix[r-1][c-1], matrix[r][c-1],matrix[r-1][c]) + 1 if matrix[r][c]==1 else 0
                count= count+ matrix[r][c]- old_val  
        return count