class Solution:
    def solution_798_4(self, s: str, t: str, maxCost: int) -> int:
        window=[]
        maxy=0
        for i in range(len(s)):
            
            if s[i]==t[i]:#if they are equal append 0 diff
                window.append(0)
                continue
                
            diff=abs(ord(s[i])-ord(t[i]))
            if len(window)>maxy:
                maxy=len(window)
                
            while window and diff>maxCost:
                maxCost+=window.pop(0)
            
            if maxCost>=diff:
                maxCost-=diff
                window.append(diff)
                
                
        if len(window)>maxy:#Last check
            maxy=len(window)
        return maxy