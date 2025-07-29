class Solution:
    def solution_722_5(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for i in range(n+1)]
        for i in range(1, n + 1):
            current_max = 0
            for j in range(1, min(i, k) + 1):
                current_max = max(current_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + current_max * j)
        return dp[n]