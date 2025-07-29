class Solution:
    def solution_100_4_1(self, houses: List[int]) -> int:
        if len(houses) == 1:
            return houses[0]
        if len(houses) == 2 or len(houses) == 3:
            return max(houses)
        
        def solution_100_4_2(nums):
            n = len(nums)
        
            dp = [0] * n
            dp[0], dp[1], dp[2] = nums[0], nums[1], nums[2] + nums[0]
        
            for i in range(3, n):
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        
       
            return max(dp[-1], dp[-2])
    
        return max(solution_100_4_2(houses[1:]), solution_100_4_2(houses[:-1]))