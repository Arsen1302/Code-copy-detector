class Solution:
    def solution_924_2_1(self, slices: List[int]) -> int:
        m=len(slices)//3
        def solution_924_2_2(slices,m):
            n=len(slices)
            dp=[[0 for i in range(m+1)] for j in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if i==1:
                        dp[i][j]=slices[0]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+slices[i-1])
            return dp[n][m]
        return max(solution_924_2_2(slices[:-1],m),solution_924_2_2(slices[1:],m))