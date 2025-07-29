class Solution:
    def solution_254_4(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0
        j = 0
        countCookie = 0
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                countCookie += 1
                j += 1
                i += 1
            elif s[j] <= g[i]:
                j += 1         
        return countCookie