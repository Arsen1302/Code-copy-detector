class Solution:
    def solution_1563_1_1(self, pressedKeys: str) -> int:
        MOD = 1_000_000_007 
        
        @cache 
        def solution_1563_1_2(n, k): 
            """Return number of possible text of n repeated k times."""
            if n < 0: return 0
            if n == 0: return 1
            ans = 0
            for x in range(1, k+1): ans = (ans + solution_1563_1_2(n-x, k)) % MOD
            return ans 
        
        ans = 1
        for key, grp in groupby(pressedKeys): 
            if key in "79": k = 4
            else: k = 3
            ans = (ans * solution_1563_1_2(len(list(grp)), k)) % MOD 
        return ans