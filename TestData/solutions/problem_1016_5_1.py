class Solution:
    def solution_1016_5_1(self, n):
        
        @lru_cache(None)
        def solution_1016_5_2(state):
            if state == 0: 
                return False
            for i in range(1, int(math.sqrt(state))+1):
                if not solution_1016_5_2(state - i*i): 
                    return True
            return False
        
        return solution_1016_5_2(n)