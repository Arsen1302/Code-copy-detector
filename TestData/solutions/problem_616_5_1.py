class Solution:
    def solution_616_5_1(self, n: int) -> int:
        mp = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 
              5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        
        @lru_cache(None)
        def solution_616_5_2(n, k): 
            """Return """
            if n == 1: return 1
            ans = 0
            for kk in mp[k]: ans += solution_616_5_2(n-1, kk)
            return ans % 1_000_000_007
        
        return sum(solution_616_5_2(n, k) for k in range(10)) % 1_000_000_007