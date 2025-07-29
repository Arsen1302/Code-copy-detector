class Solution:
    def solution_1721_1_1(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(k, n + 1):
            dp[i] = dp[i - 1]
            for length in range(k, k + 2):
                j = i - length
                if j < 0:
                    break
                if self.solution_1721_1_2(s, j, i):
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[-1]
    
    
    def solution_1721_1_2(self, s, j, i):
        left, right = j, i - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True