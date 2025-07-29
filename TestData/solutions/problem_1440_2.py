class Solution:
    def solution_1440_2(self, rings: str) -> int:
        d = dict()
        ct = 0
        l = 0
        r=1
        while r<len(rings):
            if rings[r] in d:
                d[rings[r]].add(rings[l])
            else:
                d[rings[r]] = set()
                d[rings[r]].add(rings[l])
                
            l=r+1
            r+=2
            
        for i in d:
            if len(d[i]) == 3:
                ct+=1
                
        return ct