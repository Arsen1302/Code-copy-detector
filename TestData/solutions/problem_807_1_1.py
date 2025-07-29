class Solution:
    def solution_807_1_1(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def solution_807_1_2(idx, prevNum, prevNumFreq):
            if idx == n:
                return 1
            
            ans = 0
            for i in range(1, 7):
                if i == prevNum:
                    if prevNumFreq < rollMax[i - 1]:
                        ans += solution_807_1_2(idx + 1, i, prevNumFreq + 1)
                        
                else:
                    ans += solution_807_1_2(idx + 1, i, 1)
            
            return ans % MOD
        
        return solution_807_1_2(0, 0, 0)