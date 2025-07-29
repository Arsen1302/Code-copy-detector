class Solution:
    def solution_846_2(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        presum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = mat[i-1][j-1] + presum[i][j-1] + presum[i-1][j] - presum[i-1][j-1] 
        ans = 0            
        for i in range(m+1):
            for j in range(n+1):
                length = ans + 1
                while (i + length <= m and j + length <= n and
                       presum[i+length][j+length] - presum[i+length][j] - presum[i][j+length] + presum[i][j] <= threshold):
                    ans = length
                    length += 1
        return ans