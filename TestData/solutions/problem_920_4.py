class Solution:
    def solution_920_4(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        c = 0
        ans = 0
        for i,j in sorted(zip(efficiency,speed),reverse=True):
            c += j
            heapq.heappush(heap,j)
            if len(heap)>k:
                d = heapq.heappop(heap)
                c -= d
            ans = max(ans,i*c)
        return ans%(10**9+7)