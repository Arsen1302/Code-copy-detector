class Solution:
    def solution_460_3(self, matrix: List[List[int]]) -> bool:
        arr = matrix[0]
        
        for i in range(1 , len(matrix)):
            arr = [matrix[i][0]] + arr[:-1]
            
            if(matrix[i] != arr): return False
        
        return True