class Solution:
    MOD = 1000000007
    
    def solution_1689_3(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prev = [[0] * k for _ in range(n + 1)]
        
        for i in range(m - 1, -1, -1):
            cur = [[0] * k for _ in range(n + 1)]
            for j in range(n - 1, -1, -1):
                for s in range(k):
                    new = (s + grid[i][j]) % k
                    if i == m - 1 and j == n - 1:
                        cur[j][s] = int(new == 0)
                    else:
                        cur[j][s] = (prev[j][new] +
                                     cur[j + 1][new]) % Solution.MOD
            prev = cur
        
        return prev[0][0]