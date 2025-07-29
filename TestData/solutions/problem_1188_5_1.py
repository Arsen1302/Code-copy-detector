class Solution:
    def solution_1188_5_1(self, events: List[List[int]], k: int) -> int:
        n=len(events)
        events.sort()
        @lru_cache(None)
        def solution_1188_5_2(ind,k):
            if ind==n or k==0:
                return 0
            ans=solution_1188_5_2(ind+1,k)
            nextInd=bisect.bisect_left(events,[events[ind][1]+1])
            ans=max(ans,events[ind][2]+solution_1188_5_2(nextInd,k-1))
            return ans
        return solution_1188_5_2(0,k)