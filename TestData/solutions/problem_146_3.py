class Solution:
    def solution_146_3(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [sys.maxsize] * len(nums)
        for x in nums:
            dp[bisect.bisect_left(dp, x)] = x
        return bisect.bisect(dp, max(nums))