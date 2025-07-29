class Solution:
    def solution_787_5(self, arr):
        n = len(arr)

        dp0, dp1, max_val = [0]*n, [0]*n, arr[0]

        dp0[0] = arr[0]

        for i in range(1,n):
            dp0[i] = max(dp0[i-1] + arr[i],arr[i])
            dp1[i] = max(dp1[i-1] + arr[i],arr[i],dp0[i-1])
            max_val = max(max_val,dp0[i],dp1[i])

        return max_val