class Solution:
    def solution_1304_2(self, nums: List[int]) -> int:
        n = len(nums)   
        dp = [[0,0] for _ in range(n)] # initialize dp
        dp[0][0] = nums[0] # pre-define
        dp[0][1] = 0 # pre-define

        for i in range(1, n): # iterate through nums starting from index 1
            dp[i][0] = max(nums[i] + dp[i-1][1], dp[i-1][0]) # find which value is higher between choosing or not choosing when the last value is plus.
            dp[i][1] = max(-nums[i] + dp[i-1][0], dp[i-1][1]) # find which value is higher between choosing or not choosing when the last value is minus.
        
        return max(dp[-1]) # find the maximum of the last array of dp of whether the last value is plus or minus, this will be our answer.