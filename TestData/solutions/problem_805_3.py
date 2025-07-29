class Solution:
    def solution_805_3(self, s: str) -> int:
        c=out=0
        for i in s:
            if i=='R':
                c+=1
            else:
                c-=1
            if c==0:
                out+=1
        return out