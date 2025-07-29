class Solution:
    def solution_480_4(self, n: int) -> int:
        #edge case
        if n == 1:
            return 1
        
        mod = 10 ** 9 + 7
        dp_full = [0 for _ in range(n)]
        dp_incomp = [0 for _ in range(n)]
        
        dp_full[0] = 1
        dp_full[1] = 2
        dp_incomp[1] = 2
        
        for i in range(2, n):
            dp_full[i] = dp_full[i - 2] + dp_full[i - 1] + dp_incomp[i - 1]
            dp_incomp[i] = dp_full[i - 2] * 2 + dp_incomp[i - 1]
        
        return dp_full[-1] % mod