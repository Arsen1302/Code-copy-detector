class Solution:
    def solution_80_3(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]: return 0
        m,n=len(dungeon),len(dungeon[0])
        dp=[]
        for row in dungeon:
            dp.append([0]*len(row))
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[i][j]=max(1,1-dungeon[i][j])
                elif i==m-1:
                    dp[i][j]=max(1,dp[i][j+1]-dungeon[i][j])
                elif j==n-1:
                    dp[i][j]=max(1,dp[i+1][j]-dungeon[i][j])                
                else:
                    dp[i][j]=max(1,min(dp[i][j+1],dp[i+1][j])-dungeon[i][j])
        return dp[0][0]