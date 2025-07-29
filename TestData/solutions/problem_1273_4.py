class Solution:
    def solution_1273_4(self, dist: List[int], hour: float) -> int:
        lo, hi = 1, 10_000_001
        while lo < hi: 
            mid = lo + hi >> 1
            tm = sum((dist[i]+mid-1)//mid for i in range(0, len(dist)-1)) + dist[-1]/mid
            if tm <= hour: hi = mid
            else: lo = mid + 1
        return lo if lo < 10_000_001 else -1