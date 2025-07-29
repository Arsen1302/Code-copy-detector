class Solution:
    def solution_1528_5_1(self, piles: List[List[int]], k: int) -> int:
        # sort by the maximum prefix sum
        p = sorted([list(accumulate(x[:k], initial=0)) for x in piles], key=lambda x: -x[-1])
        
        @lru_cache(None)
        def solution_1528_5_2(i, k):
            if i == len(p):
                return 0
            ans = 0
            for j in range(min(len(p[i]), k+1)):
                ans = max(ans, p[i][j] + solution_1528_5_2(i+1, k-j))
            return ans

        return solution_1528_5_2(0, k)