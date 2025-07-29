class Solution:
    def solution_1285_4_1(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # check if matrix is already equal
        if mat == target:
            return True
        
        
        # 90 degree rotation clockwise can be achieved by transposing and reflecting
        # do this 3 times for degrees 90,180 and 270 and compare with original
        for i in range(3):
            self.solution_1285_4_2(mat)
            self.solution_1285_4_3(mat)
            if mat == target:
                return True
        
        return False
    
    
    def solution_1285_4_2(self, matrix):
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
    def solution_1285_4_3(self, matrix):
        for i in range(len(matrix)):
            matrix[i].reverse()