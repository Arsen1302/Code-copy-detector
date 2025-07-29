class Solution:
    def solution_123_5(self, nums: List[int]) -> List[int]:
        dp=[]
        product=1
        for i in nums:
            dp.append(product)
            product*=i
        product=1
        for i in range(len(nums)-1,-1,-1):
            dp[i]=dp[i]*product
            product*=nums[i]
        return dp