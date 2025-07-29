class Solution:
    def solution_1715_3_1(self, low: int, high: int, zero: int, one: int) -> int:
        
        ans=[0]
        mod=10**9+7
        def solution_1715_3_2(s):
            if s>high:
                return 0
            if dp[s]!=-1:
                return dp[s]
            p=solution_1715_3_2(s+zero)+solution_1715_3_2(s+one)
            if s>=low and s<=high:
                p+=1
            dp[s]=p%mod
            return dp[s]
        dp=[-1]*(high+1)
        return solution_1715_3_2(0)%mod