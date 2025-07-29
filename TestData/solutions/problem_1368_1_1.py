class Solution:
    def solution_1368_1_1(self, s: str) -> int:
        subs = []
        n = len(s)
        def solution_1368_1_2(curr, ind, inds):
            if ind == n:
                if curr == curr[::-1]:
                    subs.append((curr, inds))
                return
            solution_1368_1_2(curr+s[ind], ind+1, inds|{ind})
            solution_1368_1_2(curr, ind+1, inds)
        
        solution_1368_1_2('', 0, set())
        
        res = 0
        n = len(subs)
        for i in range(n):
            s1, i1 = subs[i]
            for j in range(i+1, n):
                s2, i2 = subs[j]
                if len(i1 &amp; i2) == 0:
                    res = max(res, len(s1)*len(s2))
        return res