class Solution:
    def solution_1147_3(self, nums: List[int], k: int) -> int:
        dp=[nums[0]]+[0]*(len(nums)-1)
        for i in range(1,len(nums)): dp[i]=nums[i]+max(dp[max(0,i-k):i])
        return dp[-1]