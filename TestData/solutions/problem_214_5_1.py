class Solution:
    def solution_214_5_1(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        loc = set(stones)
        
        @cache
        def solution_214_5_2(x, step): 
            """Return True if it is possible to cross river at stones[i]."""
            if x == stones[-1]: return True 
            ans = False 
            for ss in (step-1, step, step+1): 
                if 0 < ss and x + ss in loc: ans = ans or solution_214_5_2(x + ss, ss)
            return ans 
        
        return solution_214_5_2(1, 1)