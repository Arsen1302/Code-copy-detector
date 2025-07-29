class Solution:
    def solution_207_5(self, nums):
        n, total = len(nums), sum(nums)

        dp = [0]*n  

        dp[0] = sum([i*j for i,j in enumerate(nums)])

        for i in range(1,n):
            dp[i] = dp[i-1] + (total - nums[n-i]*n)

        return max(dp)