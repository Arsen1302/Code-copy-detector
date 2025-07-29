class Solution:
    def solution_659_4(self, arr: List[int]) -> int:
        # [inc, dec]
        N = len(arr)

        dp = [[1, 1] for _ in range(N)]
        
        for i in range(1, N):
            j = i - 1
            if arr[i] > arr[j]:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)
            elif arr[i] < arr[j]:
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            else:
                dp[i] = [1, 1]
        
        ret = -math.inf
        for pair in dp:
            for item in pair:
                ret = max(ret, item)
        
        return ret