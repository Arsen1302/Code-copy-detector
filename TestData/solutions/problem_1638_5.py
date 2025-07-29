class Solution:
    def solution_1638_5(self, s: str, k: int) -> int:
        n=len(s)
		
		# Memoization
        # dp=[[-1]*(n+1) for i in range(n+1)]
        # def helper(ind, prev_ind):
        #     if ind==n:
        #         return 0
        #     if dp[ind][prev_ind]!=-1:
        #         return dp[ind][prev_ind]
        #     notTake=helper(ind+1, prev_ind)
        #     take=0
        #     if prev_ind==-1 or abs(ord(s[ind])-ord(s[prev_ind]))<=k:
        #         take=1+helper(ind+1, ind)
        #     dp[ind][prev_ind] = max(take, notTake)
        #     return dp[ind][prev_ind]
        # return helper(0, -1)
		
		# Tabulation
        dp=[1]*(n+1)
        maxi=0
        for ind in range(1, n):
            for prev_ind in range(ind):
                if abs(ord(s[ind])-ord(s[prev_ind]))<=k and dp[ind]<dp[prev_ind]+1:
                    dp[ind]=dp[prev_ind]+1
            maxi=max(maxi, dp[ind])
        return maxi