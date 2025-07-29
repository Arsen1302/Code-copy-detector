class Solution:
    def solution_214_2(self, stones: List[int]) -> bool:
        L = len(stones)
        
        if stones[1] != 1: return False
        
        @cache
        def solution_214_2(stone, k):
            if stone == stones[-1]:
                return True

            jumps = [k, k+1]
            if k > 1: jumps.append(k-1)
            
            for jump in jumps:
                nextStone = stone + jump
                found = bisect_left(stones, nextStone)
                if found < L and stones[found] == nextStone and solution_214_2(nextStone, jump):
                    return True
                
            return False
        
        return solution_214_2(1, 1)