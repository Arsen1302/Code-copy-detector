class Solution:
     def solution_279_2(self, nums: List[int]) -> bool:
         dp[i][j] the person's effective score when pick, facing nums[i..j]
         dp = [[0] * len(nums) for _ in range(len(nums))]
         for s in range(len(nums)):
             for i in range(len(nums)-s):
                 j = i + s
                 if i == j:
                     dp[i][i] = nums[i]
                 else:
                     dp[i][j] = max(nums[j] - dp[i][j-1], nums[i] - dp[i+1][j])
         return dp[0][-1] >= 0