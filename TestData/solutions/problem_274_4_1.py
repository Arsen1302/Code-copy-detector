class Solution:
    def solution_274_4_1(self, nums: List[int], k: int) -> List[float]:
        result = deque([])
        minheap = []
        maxheap = []
        # ----------------------------------------------------------------
        def solution_274_4_2():
            if (maxheap and minheap) and (maxheap[0] * -1) > minheap[0]:
                val = -1 * heapq.heappop(maxheap)
                heapq.heappush(minheap, val)
            if len(maxheap) > len(minheap) + 1:
                val = -1 * heapq.heappop(maxheap)
                heapq.heappush(minheap, val)
            if len(minheap) > len(maxheap) + 1:
                val = heapq.heappop(minheap)
                heapq.heappush(maxheap, -1 * val)
        # ----------------------------------------------------------------
        def solution_274_4_3():
            if len(maxheap) > len(minheap):
                return (maxheap[0] * -1)
            if len(minheap) > len(maxheap):
                return (minheap[0])
            return ((maxheap[0] * -1) + minheap[0]) / 2
        # ----------------------------------------------------------------
        back = 0
        for front in range(len(nums)):
            heapq.heappush(maxheap, -1 * nums[front])
            solution_274_4_2()
            if (front - back + 1) >= k:
                median = solution_274_4_3()
                result.append(median)
                if nums[back] in minheap:
                    minheap.remove(nums[back])
                    heapq.heapify(minheap)
                else:
                    maxheap.remove(-1 * nums[back])
                    heapq.heapify(maxheap)
                back += 1
        return result