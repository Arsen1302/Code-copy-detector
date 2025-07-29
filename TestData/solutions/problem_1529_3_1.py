class Solution:
    def solution_1529_3_1(self, start: int, goal: int) -> int:
        def solution_1529_3_2( i):
            s=""
            while i!=0:
                s+="0"
                i-=1
            return s
        s=bin(start).replace("0b",'')
        g=bin(goal).replace('0b','')
        if len(s)<len(g):
            s=solution_1529_3_2(len(g)-len(s))+s
        
        if len(g)<len(s):
            g=solution_1529_3_2(len(s)-len(g))+g
        c=0
        for i in range(len(s)):
            if s[i]!=g[i]:
                c+=1
        return c