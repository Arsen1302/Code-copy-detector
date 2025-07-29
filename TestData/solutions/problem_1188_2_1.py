class Solution:
    def solution_1188_2_1(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [i for i, _, _ in events]
        
        @cache
        def solution_1188_2_2(i, k): 
            """Return max score of attending k events from events[i:]."""
            if i == len(events) or k == 0: return 0 
            ii = bisect_left(starts, events[i][1]+1)
            return max(solution_1188_2_2(i+1, k), events[i][2] + solution_1188_2_2(ii, k-1))
        
        return solution_1188_2_2(0, k)