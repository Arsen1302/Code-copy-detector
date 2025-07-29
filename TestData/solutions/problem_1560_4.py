class Solution:
    def solution_1560_4(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        hashmap = {s[0]: 0}
        for i in range(1, n):
            if s[i] not in hashmap:
                dp[i] = dp[i - 1] + (i + 1)
                hashmap[s[i]] = i
            else:
                dp[i] = dp[i - 1] + (i - hashmap[s[i]])
                hashmap[s[i]] = i
        return sum(dp)