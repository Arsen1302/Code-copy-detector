class Solution:
    def solution_762_4_1(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        def solution_762_4_2(start,end):
            if (start,end) in d: return d[(start,end)]
            maxx = start
            for i in range(start+1,end+1):
                if arr[maxx] < arr[i] : maxx = i
            d[(start,end)] = arr[maxx]
            return arr[maxx]
        
        dp = [[float('inf') for i in range(n)] for j in range(n)]
        for gap in range(n):
            for row in range(n - gap):
                col = row + gap
                if gap == 0:
                    dp[row][col] = 0
                elif gap == 1:
                    dp[row][col] = arr[row] * arr[col]
                else:
                    for k in range(row,col):
                        val = dp[row][k] + solution_762_4_2(row,k) * solution_762_4_2(k+1,col) + dp[k+1][col]
                        if val < dp[row][col]: dp[row][col] = val
                

        return dp[0][-1]