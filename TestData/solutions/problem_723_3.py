class Solution:
    def solution_723_3(self, s: str) -> str:
        n = len(s)
        res = ''
        for g in range(n):
            i = 0
            seen = set()
            for j in range(g, n):
                if s[i:j+1] in seen:
                    res = s[i:j+1]
                else:
                    seen.add(s[i:j+1])
                i += 1
        return res