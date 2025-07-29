class Solution:
    def solution_613_3_1(self, matrix: List[List[int]]) -> int:
        
        h, w = len(matrix), len(matrix[0])
        INF = sys.maxsize
        
        @cache
        def solution_613_3_2(row, col):
            
            ## Base case: top row
            if row == 0 and 0 <= col < w:
                return matrix[0][col]
            
            ## Base case: out-of boundary
            if col < 0 or col >= w:
                return INF
            
            ## General case: current cost + minimal cost of neighbor on previous row
            return matrix[row][col] + min( solution_613_3_2(row-1,col+offset) for offset in (-1, 0, 1) )
        
        # ------------------------------------------------
        return min( solution_613_3_2(h-1, col) for col in range(w) )