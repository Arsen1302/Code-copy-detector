class Solution:
    def solution_254_3(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        i=0
        j=0
        c=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                c+=1
                i+=1
            j+=1
        return c