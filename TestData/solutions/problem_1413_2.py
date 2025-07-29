class Solution:
    def solution_1413_2(self, n: int, quantities: List[int]) -> int:

        l, r = 1, max(quantities)
        while l <= r:
            mid = (l+r)//2
            # count the number of stores needed if the max distribution is mid
            # one store can has max one product only and we need to distribute all the quantities
            cnt = 0
            for x in quantities:
                # if 0<=x<=mid, cnt = 1, if mid<x<=2mid, cnt = 2
                cnt += (x+mid-1)//mid
            
            # if with max distribution is mid, but number of stores needed is larger than actual stores n, then will need to increase the distribution, else we can further lower down the distribution.
            if cnt > n:
                l = mid + 1
            else:
                r = mid - 1
        
        return l