class Solution:
    def solution_807_3_1(self, n: int, rollMax: List[int]) -> int:
        @lru_cache(maxsize=None)
        def solution_807_3_2(n, i, k):
            if not n: return 1
            ans = 0
            for j in range(6):
                if i != j: ans += solution_807_3_2(n-1, j, 1)
                elif k+1 <= rollMax[j]: ans += solution_807_3_2(n-1, j, k+1)
            return ans    
        return sum(solution_807_3_2(n-1, i, 1) for i in range(6)) % 1000000007