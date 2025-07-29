class Solution:
    def solution_422_4(self, s1: str, s2: str) -> int:
        m=len(s1)
        n=len(s2)
        dp=[]
        for i in range (m+1):
            dp.append([0]*(n+1))
        asc=0
        for i in range (1,m+1):
            asc+=ord(s1[i-1])
            dp[i][0]=asc
        asc=0
        for j in range (1,n+1):
            asc+=ord(s2[j-1])
            dp[0][j]=asc
        #print(dp)
        for i in range (1,m+1):
            for j in range (1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
        return dp[-1][-1]