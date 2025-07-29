class Solution:
    def solution_254_2(self, g: List[int], s: List[int]) -> int: 
        if len(s)==0:
            return 0
        i=0
        j=0
        c=0
        g.sort()
        s.sort()
        while(i!=len(g) and len(s)!=j):
            if g[i]<=s[j]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        return c