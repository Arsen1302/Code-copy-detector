class Solution:
    def solution_489_5_1(self, poured: int, query_row: int, query_glass: int) -> float:
        
        @lru_cache(None)
        def solution_489_5_2(i, j):
            """Return wine poured into glass (i, j)."""
            if i == j == 0: return poured # boundary condition
            if j < 0 or j > i: return 0 # boundary condition 
            return max(0, solution_489_5_2(i-1, j-1)-1)/2 + max(0, solution_489_5_2(i-1, j)-1)/2
        
        return min(1, solution_489_5_2(query_row, query_glass))