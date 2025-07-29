class Solution:
    def solution_955_1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        q = deque()

        for i, num in enumerate(nums):
            if i > k and q[0] == dp[i-k-1]:
                q.popleft()
            dp[i] = max(q[0] if q else 0, 0)+num

            while q and q[-1] < dp[i]:
                q.pop()
            q.append(dp[i])
        return max(dp)