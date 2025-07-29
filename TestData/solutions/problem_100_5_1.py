class Solution:
    def solution_100_5_1(self,nums):
        dp=nums.copy()    #memo table

        dp[1]=max(dp[0],dp[1])
        #this loop stores the values in memo table as : highest amount that can be stolen upto that house
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return max(dp)

    def solution_100_5_2(self, nums: List[int]) -> int:
        if len(nums)<3:     #if less than 3 numbers are present in array then no need to loop
            return max(nums)
        # as first element and last element cant be used at the same time we can consider one at time and run the process
        return max(self.solution_100_5_1(nums[1:]),self.solution_100_5_1(nums[:-1]))