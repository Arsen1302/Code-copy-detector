class Solution:
    def solution_1612_3(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        heap = [-abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        total = k1 + k2
        if -sum(heap) <= total:
            return 0

        heapq.heapify(heap)
        
        while total > 0:
            val = heapq.heappop(heap) 
            diff = max(min(heap[0] - val, total), 1)
            heapq.heappush(heap, val + diff)
            total -= diff
        
        return sum(pow(e,2) for e in heap)