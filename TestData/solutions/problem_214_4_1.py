class Solution:
    def solution_214_4_1(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        lastStone = stones[-1]
        stones = set(stones)
        
        @lru_cache(None)
        def solution_214_4_2(stone, k):
            if stone == lastStone:
                return True
            
            return ((k != 1 and stone + k - 1 in stones and solution_214_4_2(stone + k - 1, k - 1)) or
                    (stone + k in stones and solution_214_4_2(stone + k, k)) or
                    (stone + k + 1 in stones and solution_214_4_2(stone + k + 1, k + 1)))
        
        return solution_214_4_2(1, 1)