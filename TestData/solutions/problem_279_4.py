class Solution:
    def solution_279_4(self, nums: List[int]) -> bool:
        """
        O(n^2) time complexity
        O(n) space complexity
        """
        dp = [0]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                m, n = nums[i] - dp[j], nums[j] - dp[j - 1]
                dp[j] = max(m, n)
        return dp[-1] >= 0