class Solution:
    def solution_124_2(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # decreasing queue 
        ans = []
        for i, x in enumerate(nums): 
            while queue and queue[-1][1] <= x: queue.pop()
            queue.append((i, x))
            if queue and queue[0][0] <= i-k: queue.popleft()
            if i >= k-1: ans.append(queue[0][1])
        return ans