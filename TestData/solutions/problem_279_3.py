class Solution:
     def solution_279_3(self, nums: List[int]) -> bool:
         n = len(nums)
         dp = nums[:]
       
         for s in range(1, n):
             newdp = [0] * n
             for j in range(s, n):
                 i = j - s
                 newdp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
                
             dp = newdp
         return dp[-1] >= 0