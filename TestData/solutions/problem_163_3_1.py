class Solution:
    def solution_163_3_1(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) # dimensions 
        
        @cache
        def solution_163_3_2(i, j): 
            """Return max increasing path starting from (i, j)."""
            ans = 1
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and matrix[i][j] < matrix[ii][jj]: 
                    ans = max(ans, 1 + solution_163_3_2(ii, jj))
            return ans 
        
        return max(solution_163_3_2(i, j) for i in range(m) for j in range(n))