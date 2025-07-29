class Solution:
    def solution_1665_1(self, intervals: List[List[int]]) -> int:
        pq = []
        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heappop(pq)
            heappush(pq, right)
        return len(pq)