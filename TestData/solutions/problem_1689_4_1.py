class Solution:
    def solution_1689_4_1(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        P = 10**9 + 7

        if k == 1:
            return self.solution_1689_4_2(n + m - 2, n - 1, P)

        dp = [[[0 for r in range(k)] for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0] % k] = 1
        for j in range(1,n):
            for r in range(k):
                r_p = (r - grid[0][j] % k) % k
                dp[0][j][r] = dp[0][j-1][r_p]

        for i in range(1,m):
            for r in range(k):
                r_p = (r - grid[i][0] % k) % k
                dp[i][0][r] = dp[i-1][0][r_p]


        for i in range(1,m):
            for j in range(1,n):
                for r in range(k):
                    r_p = (r - grid[i][j] % k) % k
                    dp[i][j][r] = (dp[i-1][j][r_p] + dp[i][j-1][r_p]) % P

        return dp[m-1][n-1][0]

    # Compute the binomial coefficient n C r modulo p, where
    # p is prime.
    def solution_1689_4_2(self, n, r, p):
        prod = 1
        for i in range(r):
            prod = (prod * (n - i) * self.solution_1689_4_3(i + 1, p)) % p

        return prod

    # Use the Euclidean algorithm to find the inverse of x (mod p).
    def solution_1689_4_3(self, x, p):
        return self.solution_1689_4_4(x, p)[0] % p

    def solution_1689_4_4(self, a, b):
        if b == 0:
            return (1, 0)
        
        u, v = self.solution_1689_4_4 (b, a % b)
        return (v, u - (a // b) * v)