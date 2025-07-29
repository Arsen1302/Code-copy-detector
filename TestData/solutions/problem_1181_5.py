class Solution:
    def solution_1181_5(self, lowlimit: int, highlimit: int) -> int:
        a=[]
        a=[0 for i in range(highlimit+1)]

        for i in range(lowlimit,highlimit+1):
            sum=0
            while(i>0):
                b=i%10
                i=i//10
                sum+=b
            a[sum]=a[sum]+1
        
        c=max(a)
        return(c)