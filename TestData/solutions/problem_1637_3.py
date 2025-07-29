class Solution:
    def solution_1637_3(self, nums):
        n = len(nums)

        dp = [False]*(n+1)
        dp[0] = True

        for i in range(2,n+1):
            dp[i] |= nums[i-1] == nums[i-2] and dp[i-2]
            dp[i] |= i>2 and nums[i-1] == nums[i-2] == nums[i-3] and dp[i-3]
            dp[i] |= i>2 and nums[i-1] - nums[i-2] == nums[i-2] - nums[i-3] == 1 and dp[i-3]

        return dp[-1]