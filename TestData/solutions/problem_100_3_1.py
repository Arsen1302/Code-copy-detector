class Solution:
    def solution_100_3_1(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        # step 1 or 2
        if n<=2:
            return max(nums)
        
        
        return max(self.solution_100_3_2(nums[:-1]),self.solution_100_3_2(nums[1:]))
    
    
    def solution_100_3_2(self,nums):
        
        
        dp=[0]*len(nums)
        
        
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return max(dp)