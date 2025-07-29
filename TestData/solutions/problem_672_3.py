class Solution:
    def solution_672_3(self, nums: List[int], k: int) -> int:
        ans = ii = 0 
        freq = defaultdict(int)
        queue = deque()
        for i, x in enumerate(nums): 
            freq[x] += 1
            queue.append(i)
            if len(freq) > k: 
                ii = queue[0]+1
                freq.pop(nums[queue.popleft()])
            while freq[nums[queue[0]]] > 1: freq[nums[queue.popleft()]] -= 1
            if len(freq) == k: ans += queue[0] - ii + 1
        return ans