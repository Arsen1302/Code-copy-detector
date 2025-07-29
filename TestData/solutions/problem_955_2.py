class Solution:
    def solution_955_2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp, mono_dec_q, res = [nums[0]] * n, deque([0]), nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(0, dp[mono_dec_q[0]])
            while mono_dec_q and dp[i] >= dp[mono_dec_q[-1]]:
                mono_dec_q.pop()
            if mono_dec_q and i - mono_dec_q[0] == k:
                mono_dec_q.popleft()
            mono_dec_q.append(i)
            res = max(res, dp[i])
        return res