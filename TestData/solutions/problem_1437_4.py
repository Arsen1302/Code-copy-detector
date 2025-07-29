class Solution:
    def solution_1437_4(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        for i, n in enumerate(nums):
            heappush(min_heap, (n, i))
            if len(min_heap) > k:
                heappop(min_heap)
        min_heap.sort(key = lambda x: x[1])
        return [i[0] for i in min_heap]