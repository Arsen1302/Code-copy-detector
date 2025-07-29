class Solution:
    def solution_939_3(self, num: List[int]) -> str:
        dp=[0]*(len(num)+1)
        i=len(num)-1
        
        while i>=0:
            ans=-1001
            ans=max(ans,num[i]-dp[i+1])
            
            if i+1<len(num):
                ans=max(ans,num[i]+num[i+1]-dp[i+2])
            
            if i+2<len(num):
                ans=max(ans,num[i]+num[i+1]+num[i+2]-dp[i+3])
            dp[i]=ans
            i-=1
            
            
        alice=dp[0]
        if alice>0:
            return "Alice"
        elif alice<0:
            return "Bob"
        else:
            return "Tie"