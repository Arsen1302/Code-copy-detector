class Solution:
    def solution_1323_3(self, s: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        t=d[s[0]]
        for v in d.values():
            if v!=t:
                return False
        return True