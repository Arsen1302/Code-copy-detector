class Solution:
    def solution_1276_5(self, s: str) -> int:
        c,n=0,len(s)
        for i in range(n-2):
            t=set(s[i:i+3])
            if len(t)==3:
                c+=1
        return c