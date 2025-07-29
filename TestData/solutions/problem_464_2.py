class Solution:
    def solution_464_2(self, jewels: str, stones: str) -> int:
        occ=dict()
        for i in stones:
            if i in occ.keys():
                occ[i]+=1
            else:
                occ.update({i:1})
        res=0
        for i in jewels:
            if i in occ.keys():
                res+=occ[i]
            
        return res