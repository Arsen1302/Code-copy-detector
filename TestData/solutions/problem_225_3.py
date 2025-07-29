class Solution:
    def solution_225_3(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&amp;1:
            return False
        dp = [True]+[False]*(s>>1)
        for num in nums:
            for curr in range(s>>1, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]
        return dp[-1]