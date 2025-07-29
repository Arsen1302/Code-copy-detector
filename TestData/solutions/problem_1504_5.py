class Solution:
    def solution_1504_5(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 0, max(time) * totalTrips
        while lo < hi: 
            mid = lo + hi >> 1
            if sum(mid//x for x in time) < totalTrips: lo = mid + 1
            else: hi = mid 
        return lo