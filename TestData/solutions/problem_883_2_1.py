class Solution1: # Memoized Solution
    def solution_883_2_1(self, arr: List[int], d: int) -> int:
        if d>len(arr): return -1
        n = len(arr)
        dp = [[-1 for i in range(d+1)] for j in range(n)]
        def solution_883_2_2(ind,d):
            if ind==n: return float('inf')
            if d==1:   # if we have only one day then we just take max of all remaining jobs
                return max(arr[ind:])
            if dp[ind][d]!=-1: return dp[ind][d]
            ans = float('inf')
            mx = float('-inf')
            s = 0
            for i in range(ind,n):
                mx = max(mx,arr[i])
                s=mx+solution_883_2_2(i+1,d-1)
                ans = min(ans,s)
            dp[ind][d] = ans
            return dp[ind][d]
        return solution_883_2_2(0,d)
class Solution:  # Tabulation version
    def solution_883_2_1(self, arr: List[int], d: int) -> int:
        if d>len(arr): return -1
        n = len(arr)
        dp = [[0 for i in range(d+1)] for j in range(n+1)]
        for i in range(d+1):                   # Base Cases
            dp[n][i] = float('inf')
        for i in range(n):                       # Base Case
            dp[i][1]=max(arr[i:])
        for ind in range(n-1,-1,-1):
            for days in range(2,d+1):
                ans = float('inf')
                mx = float('-inf')
                s = 0
                for i in range(ind,n):
                    mx = max(mx,arr[i])
                    s=mx+dp[i+1][days-1]
                    ans = min(ans,s)
                dp[ind][days] = ans
        return dp[0][d]