class Solution:
    def solution_208_3_1(self, n: int) -> int:
        dp={}
        dp[0]=0
        dp[1]=0
        moves=0
        def solution_208_3_2(n):
            if n in dp:
                return dp[n]
            if n%2==0:
                dp[n]=1+solution_208_3_2(n//2)
            else:
                dp[n]=1+min(solution_208_3_2(n-1),solution_208_3_2(n+1))
            return dp[n]
        return solution_208_3_2(n)