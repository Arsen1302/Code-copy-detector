class Solution:
    def solution_192_1_1(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        def solution_192_1_2(m):
            c = 0                   # solution_192_1_2 of element less than equals to 'm'
            i = n-1
            j = 0
            
            while i >= 0 and j < n:
                if matrix[i][j] > m:
                    i -= 1
                else:
                    c += i+1
                    j += 1
            return c
           
        
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        while low <= high:
            m = (low+high)//2
            cnt = solution_192_1_2(m)
            if cnt < k:
                low = m + 1
            else:
                cnt1 = solution_192_1_2(m-1)
                if cnt1 < k:
                    return m
                high = m-1
        return 0