class Solution:
    def solution_191_4_1(self, nums: List[int], target: int) -> int:
        dp = {}
        def solution_191_4_2(nums, target,  asf):
            if asf in dp:
                return dp[asf]
            if asf<0:
                return 0
            if asf == 0:
                return 1
            ans = 0
            for i in nums:
                ans += solution_191_4_2(nums, target, asf-i)
            dp[asf] = ans
            
            return ans
        return solution_191_4_2(nums,target,target)