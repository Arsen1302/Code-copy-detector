class Solution:
    def solution_731_3(self, barcodes: List[int]) -> List[int]:
        n = len(barcodes)
        count = Counter(barcodes)
        heap = []
        for i in count:
            heap.append((-count[i],i))
        heapq.heapify(heap)
        idx = 0
        ans =[0]*n
        while heap:
            times,val = heapq.heappop(heap)
            times = -times
            for i in range(times):
                ans[idx] = val
                idx += 2
                if idx >=n : idx = 1
        return ans