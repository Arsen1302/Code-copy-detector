class Solution:
    def solution_158_2_1(self, coins: List[int], amount: int) -> int:            
        def solution_158_2_2(rem, cache):
            if rem < 0:
                return math.inf
            if rem == 0:                    
                return 0       
            if rem in cache:
                return cache[rem]
            
            cache[rem] = min(solution_158_2_2(rem-x, cache) + 1 for x in coins)                         
            return cache[rem]      
        
        ans = solution_158_2_2(amount, {})
        return -1 if ans == math.inf else ans