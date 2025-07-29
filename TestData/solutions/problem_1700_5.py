class Solution:
    def solution_1700_5(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        pairs = sorted(zip(nums, cost))
        if pairs[0][0] == pairs[-1][0]:
            return 0
        
        post_sum = [0] * (n + 1)
        res = 0
        for i in range(n - 1, -1, -1):
            post_sum[i] = pairs[i][1] + post_sum[i + 1]
            res += (pairs[i][0] - pairs[0][0]) * pairs[i][1]
        
        pre_sum = pairs[0][1]
        for i in range(1, n):
            if pre_sum > post_sum[i]:
                return res
            diff = pairs[i][0] - pairs[i - 1][0]
            res -= (post_sum[i] - pre_sum) * diff
            pre_sum += pairs[i][1]
        
        return res