class Solution:
    def solution_955_3(self, nums: List[int], k: int) -> int:
        q = deque()
        for i, v in enumerate(nums):
            if len(q): 
                nums[i] += nums[q[0]]
            if q and i - q[0] >= k:
                q.popleft()
            if nums[i] > 0:
                while q and nums[q[-1]] <= nums[i]:
                    q.pop()
                q.append(i)
        return max(nums)