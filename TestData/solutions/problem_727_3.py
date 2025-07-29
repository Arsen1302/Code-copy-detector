class Solution:
    def solution_727_3(self, stones):
        total = sum(stones)

        max_weight = int(total/2)

        dp = [0]*(max_weight+1)

        for stone in stones:
            for weight in range(max_weight,-1,-1):
                if weight - stone >= 0:
                    dp[weight] = max(dp[weight], stone + dp[weight-stone])

        return total - 2*dp[-1]