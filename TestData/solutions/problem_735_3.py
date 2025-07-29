class Solution:
    def solution_735_3(self, matrix: List[List[int]], target: int) -> int:
        ans = 0 
        m, n = len(matrix), len(matrix[0]) # dimensions 
        prefix = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m): 
            for j in range(n): 
                prefix[i+1][j+1] = matrix[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
                
            for ii in range(i+1):
                freq = {0: 1}
                for j in range(n): 
                    diff = prefix[i+1][j+1] - prefix[ii][j+1] 
                    ans += freq.get(diff - target, 0)
                    freq[diff] = 1 + freq.get(diff, 0)
        return ans