class Solution:
    def solution_924_3_1(self, slices: List[int]) -> int:
        n=len(slices)
        @lru_cache(None)
        def solution_924_3_2(ind,pick,start):
            if ind<start or pick==0:return 0
            return max(solution_924_3_2(ind-1,pick,start),solution_924_3_2(ind-2,pick-1,start)+slices[ind])
        m=n//3
        return max(solution_924_3_2(n-1,m,1),solution_924_3_2(n-2,m,0))