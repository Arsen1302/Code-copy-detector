class Solution:
    def solution_184_3(self, nums: List[int]) -> int:
        # tuition: dp[i] represents the length of the longest strictly increasing subsequence ending with nums[i]. recursive formula: dp[i]=max(dp[j]+1, dp[i]) with 0 < j < i. This takes O(n^2) time. 
        n = len(nums)
        if n <= 1: return n
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]: # strictly increasing 
                    dp[i] = max(dp[i], dp[j] + 1) 
        return max(dp)