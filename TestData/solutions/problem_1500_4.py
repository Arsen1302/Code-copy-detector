class Solution:
    def solution_1500_4(self, s: str, l: int) -> str:
        C=[list(x) for x in sorted(Counter(s).items(),reverse=True)] ; ans=''
        if len(C)==1: return C[0][0]*l
        while len(C)>1:
            ans+=C[0][0]*min(C[0][1],l)
            C[0][1]-=min(C[0][1],l)
            if C[0][1]>0: ans+=C[1][0] ; C[1][1]-=1
            C=[c for c in C if c[1]>0]
        return ans+C[0][0]*min(C[0][1],l)