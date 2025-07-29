class Solution:
    def solution_937_3(self, s: str) -> int:
        s=int(s,2);k=0
        while s!=1:
            k+=1
            if s%2==1:
                s+=1
            else:
                s//=2
        return k