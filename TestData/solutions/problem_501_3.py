class Solution:
    def solution_501_3(self, nums: List[int], k: int) -> float:
        pre_sum = [0]
        for num in nums: pre_sum.append(pre_sum[-1] + num)
        avg = lambda i, j: (pre_sum[i+1]-pre_sum[j+1])/(i-j)
            
        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        for i in range(n): dp[i][0] = pre_sum[i+1] / (i+1)
            
        for i in range(1, n):
            for kk in range(1, k):
                for j in range(kk-1, i):
                    dp[i][kk] = max(dp[i][kk], dp[j][kk-1] + avg(i, j))
        return dp[n-1][k-1]