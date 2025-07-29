class Solution:
    def solution_735_2(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0]) # dimensions 
        
        ans = 0 
        freq = defaultdict(int)
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m): 
            for j in range(n): 
                prefix[i+1][j+1] = matrix[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
                for jj in range(-1, j): 
                    diff = prefix[i+1][j+1] - prefix[i+1][jj+1] 
                    ans += freq[jj, j, diff - target]
                    if diff == target: ans += 1
                    freq[jj, j, diff] += 1
        return ans