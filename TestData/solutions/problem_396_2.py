class Solution:
    def solution_396_2(self, nums):
        n = len(nums)

        dp, cnt, max_val = [1]*n, [1]*n, 1

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i], cnt[i] = 1 + dp[j], cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]

            max_val = max(max_val,dp[i])

        return sum([j for i,j in zip(dp,cnt) if i == max_val])