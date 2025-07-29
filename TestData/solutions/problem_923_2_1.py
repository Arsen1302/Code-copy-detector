class Solution:
    def solution_923_2_1(self,x):
        if(x==1):
            return(0)
        a=0
        if(x%2==0):
            a=self.solution_923_2_1(x//2)
        else:
            a=self.solution_923_2_1(x*3+1)
        return(a+1)
    def solution_923_2_2(self, lo: int, hi: int, k: int) -> int:
        ot=[]
        for i in range(lo,hi+1):
            ot.append([i,self.solution_923_2_1(i)])
        newara=sorted(ot, key = lambda x:x[1])
        return(newara[k-1][0])