class Solution:
    def solution_1601_3_1(self, n: int) -> int:
        
        M = 10**9 + 7
        @lru_cache()
        def solution_1601_3_2(i, prev, prevOfPrev):
            if i == n:
                return 1
            
            res = 0
            for dice in [1, 2, 3, 4, 5, 6]:
                if dice != prev and dice != prevOfPrev and (prev == -1 or math.gcd(prev, dice) == 1):
                    res += (solution_1601_3_2(i+1, dice, prev) % M)
            return res
        
        return solution_1601_3_2(0, -1, -1) % M