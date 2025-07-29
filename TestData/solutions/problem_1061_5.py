class Solution:
    def solution_1061_5(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result,primary,i,secondary = 0,0,0,n-1
        
        while i < n:
            x, y = mat[i][primary], mat[i][secondary]
            if primary!=secondary:
                result+= x + y
            else:
                result+=x
            
            primary,secondary,i = primary+1, secondary-1, i+1
        
        return result