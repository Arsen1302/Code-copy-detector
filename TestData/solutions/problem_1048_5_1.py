class Solution:
def solution_1048_5_1(self, n: int) -> int:
    
    def solution_1048_5_2(n):
        nonlocal dp
        if n<=1:
            return 1
        if n in dp:
            return dp[n]
        dp[n] = 1 + min(n%2 + solution_1048_5_2(n//2), n%3 + solution_1048_5_2(n//3))
        return dp[n]
    
    dp = defaultdict(int)
    return solution_1048_5_2(n)