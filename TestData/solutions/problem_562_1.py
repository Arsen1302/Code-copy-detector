class Solution:
    def solution_562_1(self, piles: List[int], h: int) -> int:
        k = 1
        while True:
            total_time = 0
            for i in piles:
                total_time += ceil(i / k)
            if total_time > h:
                k += 1
            else:
                return k