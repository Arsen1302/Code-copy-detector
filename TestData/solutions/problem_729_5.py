class Solution:
    def solution_729_5(self, c: List[int], g: List[int], k: int) -> int:
        s = 0 ; res = 0
        n = len(c)
        for i in range(n):
            if g[i]==0:
                s += c[i]
        i,j = 0,0
        while j<n:
            if g[j]==1:
                s += c[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                res = max(res,s)
                if g[i]==1:
                    s-=c[i]
                i+=1
                j+=1
        return res