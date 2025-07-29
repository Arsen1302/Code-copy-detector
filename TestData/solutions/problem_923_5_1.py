class Solution:
    def solution_923_5_1(self, lo: int, hi: int, k: int) -> int:
        d={}
        def solution_923_5_2(num):
            c=0
            while num != 1:
                if num % 2 == 0:
                    num=num//2
                    c+=1
                else:
                    num=num*3 + 1
                    c+=1   
            return c
        
        for i in range(lo,hi+1):
            #Function to get the power
            a=solution_923_5_2(i)
            d[i]=a
        
        di=sorted(d.items(),key = lambda x:x[1])
        
        ans=list(di)
        return ans[k-1][0]