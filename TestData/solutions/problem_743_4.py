class Solution:
    def solution_743_4(self, str1: str, str2: str) -> str:
        a=str1
        b=str2
        m=len(a)
        n=len(b)
        dp =([[0 for i in range(n + 1)] for i in range(m + 1)])
        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1]==b[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        i=m 
        j=n
        sr=""
        while i>0 and j>0:
            if a[i-1]==b[j-1]:
                sr+=a[i-1]
                i-=1
                j-=1
            else:
                if dp[i][j-1]>dp[i-1][j]:
                    sr+=b[j-1]
                    j-=1
                else:
                    sr+=a[i-1]
                    i-=1
        while i>0:
            sr+=a[i-1]
            i-=1
        while j>0:
            sr+=b[j-1]
            j-=1
        return sr[::-1]