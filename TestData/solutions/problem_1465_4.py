class Solution:
    def solution_1465_4(self, nums):
        n, k, ans = len(nums), nums.count(1), float('inf')
        c = nums[:k].count(1)
        for i in range(n):
            ans = min(ans, k - c)
            c += nums[(i + k) % n] - nums[i]
        return ans