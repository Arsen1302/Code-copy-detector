class Solution:
    def solution_1665_2(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        for interval in intervals:
            if not pq or interval[0] <= pq[0]:
                heapq.heappush(pq, interval[1])
            else:
				heapq.heappop(pq)
				heapq.heappush(pq, interval[1])
        return len(pq)