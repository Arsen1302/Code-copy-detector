class Solution:
    def solution_403_4(self, a: str, b: str) -> int:
        if b in a:
            return 1
        c,n=1,len(b)
        t=a
        while b!=t and len(t)<=n:
            c+=1
            t=a*c
        if b in t:
            return c
        if b in a*(c+1):
            return c+1
        return -1