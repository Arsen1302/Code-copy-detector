class Solution:
    def solution_707_4(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {x:{} for x in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                tmp = dp[i][nums[j]-nums[i]] if nums[j]-nums[i] in dp[i] else 1
                dp[j][nums[j]-nums[i]] = tmp + 1
        ans = 0
        for i in dp:
            for j in dp[i]:
                if dp[i][j] > ans: ans = dp[i][j]
        return ans