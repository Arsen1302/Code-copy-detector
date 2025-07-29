class Solution:
    def solution_1184_5(self, s: str) -> bool:
        n=len(s)
        pal=[[False]*n for i in range(n)]
        for i in range(n):
            pal[i][i]=True

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if i+1==j and s[i]==s[j]:
                    pal[i][j]=True
                if pal[i+1][j-1] and s[i]==s[j]:
                    pal[i][j]=True

        dp=[[False for i in range(4)] for j in range(n+1)]
        dp[n][3]=True     
        for ind in range(n-1,-1,-1):
            for i in range(ind,n):
                if pal[ind][i]:
                    dp[ind][2] |= dp[i+1][3]
                    dp[ind][1] |= dp[i+1][2]
                    dp[ind][0] |= dp[i+1][1]
        return dp[0][0]