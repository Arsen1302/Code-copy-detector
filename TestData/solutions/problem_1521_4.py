class Solution:
    def solution_1521_4(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        dp=[[0 for i in range(numCarpets+1)] for j in range(len(floor)+1)]

        for i in range(1,len(floor)+1):
            if floor[i-1]=='1':
                dp[i][0]=dp[i-1][0]+1
            else:
                dp[i][0]=dp[i-1][0]

        for j in range(1,numCarpets+1):
            for i in range(1,len(floor)+1):
                dp[i][j]=min(dp[max(0,i-carpetLen)][j-1],dp[i-1][j]+(floor[i-1]=='1'))
        return dp[-1][numCarpets]