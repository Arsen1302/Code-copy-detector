class Solution:
    def solution_798_3(self, s: str, t: str, maxCost: int) -> int:
        x=len(s)
        diff=[0]*x

        for i in range(x):
            diff[i]=abs(ord(s[i])-ord(t[i]))

        i,j=0,0
        maxx,summ=0,0

        while(j<x):
            while(summ>maxCost):
                summ-=diff[i]
                i+=1

            summ+=diff[j]
            if summ<=maxCost:
                #print('hi',j,i,summ,maxCost)
                maxx=max(j-i+1,maxx)
            j+=1

        return maxx