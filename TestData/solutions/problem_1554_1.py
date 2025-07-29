class Solution:
    def solution_1554_1(self, a: List[int]) -> int:
        l=0
        r=sum(a)
        z=100001
        y=0
        n=len(a)
        
        for i in range(n-1):
            l+=a[i]
            r-=a[i]
        
            d=abs((l//(i+1))-(r//(n-i-1)))
            if d<z:
                z=d
                y=i
        
        if sum(a)//n<z:
            y=n-1
        
        return y