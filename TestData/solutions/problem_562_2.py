class Solution:
    def solution_562_2(self, piles: List[int], h: int) -> int:
        k = ceil(sum(piles)/h)
        while True:
            total_time = 0
            for i in piles:
                total_time += ceil(i/k)
                if total_time > h:
                    break # as time exceeds H
            if total_time <= h:
                return k # answer found as time is in the given limits.
            k += 1