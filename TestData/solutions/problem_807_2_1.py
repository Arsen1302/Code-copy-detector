class Solution:
    def solution_807_2_1(self, n: int, rollMax: List[int]) -> int:
        
        @cache
        def solution_807_2_2(n, x, r):
            """Return number of sequences with n rolls left with r occurrences of x."""
            if n == 0: return 1
            ans = 0
            for xx in range(6): 
                if xx != x: ans += solution_807_2_2(n-1, xx, 1)
                elif xx == x and r < rollMax[x]: ans += solution_807_2_2(n-1, x, r+1)
            return ans 
        
        return sum(solution_807_2_2(n-1, x, 1) for x in range(6)) % 1_000_000_007