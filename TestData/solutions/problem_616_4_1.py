class Solution:
    def solution_616_4_1(self, n: int) -> int:
        
        MOD = 10**9 + 7
        
        adj = {
            0: [6, 4], 
            1: [6, 8], 
            2: [9, 7], 
            3: [4, 8], 
            4: [9, 3, 0], 
            5: [], 
            6: [7, 1, 0], 
            7: [6, 2], 
            8: [3, 1], 
            9: [4, 2]
        }
        
        @cache
        def solution_616_4_2(k, num):
            if k == 1:
                return 1
            else:
                ret = 0
                for i in adj[num]:
                    ret = (ret + solution_616_4_2(k - 1, i)) % MOD
                return ret
        
        ans = 0
        for i in range(10):
            ans = (ans + solution_616_4_2(n, i)) % MOD
        
        return ans