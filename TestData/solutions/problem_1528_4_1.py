class Solution:
    def solution_1528_4_1(self, piles: List[List[int]], k: int) -> int:
        
        @cache
        def solution_1528_4_2(i, k): 
            """Return """
            if i == len(piles) or k == 0: return 0 
            ans = solution_1528_4_2(i+1, k)
            prefix = 0 
            for j in range(min(k, len(piles[i]))): 
                prefix += piles[i][j]
                ans = max(ans, prefix + solution_1528_4_2(i+1, k-j-1))
            return ans 
        
        return solution_1528_4_2(0, k)