class Solution:
    def solution_1062_4(self, s: str) -> int:
        n = len(s)
        
        ones = s.count('1')
                
        if ones % 3 != 0:
            return 0
        if ones == 0:
            return (n-1)*(n-2)//2 % (10**9+7)
        
        # now ones % 3 ==0, ones >= 3
        k = ones//3
        idx = []
        total_idx = []
        t = 0
        for i in range(n):
            if s[i] == '1':
                t += 1
                total_idx.append(i)
                if t == k or t == 2*k or t == ones:
                    idx.append(i)
       
        res = 1
        idx.pop()
        idx = set(idx)
        for i in range(len(total_idx)):
            if total_idx[i] in idx:
                res = res * (total_idx[i+1]-total_idx[i]) % (10**9+7)
        return res % (10**9+7)