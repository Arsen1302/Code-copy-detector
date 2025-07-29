class Solution:
    def solution_390_3(self, n: int, k: int) -> List[int]:
        m=k//2
        ans=[0 for _ in range(n)]
        i=(n-m)
        j=(n-m+1)
        t=n-1
        if(k%2!=0):
            ans[t]=i
            i-=1
            t-=1
        while(m!=0):
            ans[t]=i
            t-=1
            i-=1
            ans[t]=j
            j+=1
            t-=1
            m-=1
        while(i>0):
            ans[t]=i
            i-=1
            t-=1
        return ans