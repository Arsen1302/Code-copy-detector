class Solution:
    def solution_1437_2(self, nums: List[int], k: int) -> List[int]:
        import heapq
        
        h = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(h, (-nums[i], i))
            
        res = []
        for _ in range(k):
            v, idx = heapq.heappop(h)
            res.append(idx)
        res.sort()
        return [nums[idx] for idx in res]