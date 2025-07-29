class Solution:
    def solution_771_5(self, s: str) -> int:
        n=len(s)
        a,b=0,0
        x,y=n-1,n-1
        k=0
        temp_b,temp_x=0,10
        while b<x:
            if s[a:b+1]==s[x:y+1]:
                k+=2
                temp_b,temp_x=b,x
                a=b+1
                b=a
                y=x-1
                x=y
            else:
                b+=1
                x-=1
        return k if temp_b+1==temp_x else k+1