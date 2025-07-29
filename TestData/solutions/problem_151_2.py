class Solution:
    def solution_151_2(self, nums: List[int]) -> int:
        nums = [1] + nums + [1] # augmented 
        n = len(nums)
        
        dp = [[0]*n for _ in range(n)]
        for i in reversed(range(n)): 
            for j in range(i, n): 
                for k in range(i+1, j): 
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        return dp[0][-1]