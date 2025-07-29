class Solution:
    def solution_1385_3(self, s: str) -> int:
        sl=list(s)
        out=0
        for i in range(0,len(sl)-2):
            if sl[i]=="X":
                sl[i]="O"
                sl[i+1]="O"
                sl[i+2]="O"
                out+=1
            elif sl[i]=="O":
                continue
        if sl[-1]=="X" or sl[-2]=="X":
            out+=1
        return out