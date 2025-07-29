class Solution:
    def solution_1689_5(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        dp[(0,0)][grid[0][0]%k] = 1
        for i in range(R):
            for j in range(C):
                if i > 0:
                    for n, val in dp[(i-1, j)].items(): dp[(i, j)][(n+grid[i][j])%k] += val
                if j > 0:
                    for n, val in dp[(i, j-1)].items(): dp[(i, j)][(n+grid[i][j])%k] += val
        return dp[(R-1, C-1)][0] % (10**9 + 7)