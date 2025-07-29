class Solution:
    def solution_1188_3_1(self, events: List[List[int]], k: int) -> int:
		events.sort()
		starts = [x[0] for x in events]
		@lru_cache(None)
		def solution_1188_3_2(i, k):
			if k == 0 or i >= len(events):
				return 0
			return max(events[i][-1] + solution_1188_3_2(bisect.bisect_right(starts, events[i][1]), k - 1), solution_1188_3_2(i+1, k))
		return solution_1188_3_2(0, k)