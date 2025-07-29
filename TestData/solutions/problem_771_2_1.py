class Solution:
    def solution_771_2_1(self, text: str) -> int:
        n=len(text)-1
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        def solution_771_2_2(start,end):
            if start>end:
                return 0
            if dp[start][end]!=-1:
                return dp[start][end]
            best=1
            l,r=start,end
            mid=(r+l)//2
            while r>mid:
                chunk=end-r+1
                if text[l:l+chunk]==text[r:end+1]:
                    val=solution_771_2_2(l+chunk,r-1)+2
                    best=max(best,val)
                r-=1
            dp[start][end]=best
            return dp[start][end]
        return solution_771_2_2(0,n)