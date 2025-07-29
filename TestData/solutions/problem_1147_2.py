class Solution:
    def solution_1147_2(self, nums: List[int], k: int) -> int:
        queue = deque()
        for i in reversed(range(len(nums))): 
            while queue and queue[0][1] - i > k: queue.popleft()
            ans = nums[i]
            if queue: ans += queue[0][0]
            while queue and queue[-1][0] <= ans: queue.pop()
            queue.append((ans, i))
        return ans