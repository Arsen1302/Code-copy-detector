class Solution:
    def solution_1428_3(self, grid: List[List[int]]) -> int:
        f_ans=0
        def solution_1428_3(grid):
            r,c=len(grid),len(grid[0])
            dp=copy.deepcopy(grid)
            ans=0
            for i in range(r-2,-1,-1):
                for j in range(1,c-1):
                    if dp[i][j]:
                        dp[i][j]=min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])+1
                        ans+=dp[i][j]-1
            return ans
        f_ans+=solution_1428_3(grid)
        f_ans+=solution_1428_3(grid[::-1])
        return f_ans