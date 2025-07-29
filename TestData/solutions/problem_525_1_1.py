class Solution:
    def solution_525_1_1(self, N: int, K: int, W: int) -> float:
        
        @lru_cache(None)
        def solution_525_1_2(n): 
            """Return prob of of points between K and N given current point n."""
            if N < n: return 0
            if K <= n: return 1
            if n+1 < K: return (1+W)/W*solution_525_1_2(n+1) - 1/W*solution_525_1_2(n+W+1)
            return 1/W*sum(solution_525_1_2(n+i) for i in range(1, W+1))
        
        return solution_525_1_2(0)