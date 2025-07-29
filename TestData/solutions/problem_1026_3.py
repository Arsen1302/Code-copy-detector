class Solution:
    MOD = pow(10, 9) + 7
    def solution_1026_3(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [0] * N

        if arr[0] % 2:
            dp[0] = 1
        else:
            dp[0] = 0
        
        for i in range(1, N):
            if arr[i] % 2:
                dp[i] = (i + 1 - dp[i - 1]) % self.MOD
            else:
                dp[i] = dp[i - 1]
        
        return sum(dp) % self.MOD