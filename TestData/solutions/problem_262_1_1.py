class Solution:
    def solution_262_1_1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0: return True # edge case 1
        if maxChoosableInteger * (maxChoosableInteger+1)//2 < desiredTotal: return False # edge case 2
        
        @lru_cache(None)
        def solution_262_1_2(mask, total): 
            """Return True if there is a winning strategy given mask &amp; total."""
            if total <= 0: return False # already lost 
            for i in range(maxChoosableInteger): 
                if mask &amp; (1 << i): # integer i+1 is not used yet 
                    if not solution_262_1_2(mask ^ (1 << i), total - (i + 1)): return True 
            return False 
        
        return solution_262_1_2(int("1"*maxChoosableInteger, 2), desiredTotal)