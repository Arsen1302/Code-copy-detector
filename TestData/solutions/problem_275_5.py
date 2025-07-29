class Solution:
    def solution_275_5(self, n: int) -> int:
        if n == 0: return 0 # edge case 
        
        S = [1,2,2]
        i = 2
        while len(S) < n: 
            S.extend(S[i] * [3 ^ S[-1]])
            i += 1
        return S[:n].count(1)