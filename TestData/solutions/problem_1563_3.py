class Solution:
    def solution_1563_3(self, pressedKeys):
        n = len(pressedKeys)

        dp = [0]*(n+1)

        dp[0], dp[1] = 1, 1

        for i in range(2,n+1):
            dp[i] += dp[i-1]

            if i > 1 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] += dp[i-2]

            if i > 2 and pressedKeys[i-1] == pressedKeys[i-2] == pressedKeys[i-3]:
                dp[i] += dp[i-3]

            if pressedKeys[i-1] == "7" or pressedKeys[i-1] == "9":
                if i > 3 and pressedKeys[i-1] == pressedKeys[i-2] == pressedKeys[i-3] == pressedKeys[i-4]:
                    dp[i] += dp[i-4]

        return dp[-1]%(10**9+7)