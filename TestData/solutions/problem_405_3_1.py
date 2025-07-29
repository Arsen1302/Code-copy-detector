class Solution:
    def solution_405_3_1(self, N: int, K: int, r: int, c: int) -> float:
        
        @lru_cache(None)
        def solution_405_3_2(k, i, j): 
            """Return probability in chessboard at (i, j) with k moves left."""
            if not (0 <= i < N and 0 <= j < N): return 0
            if k == 0: return 1 
            return 1/8*sum(solution_405_3_2(k-1, i+ii, j+jj) for ii, jj in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)))
            
        return solution_405_3_2(K, r, c)