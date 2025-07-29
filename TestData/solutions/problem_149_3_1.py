class Solution:
    def solution_149_3_1(self,ind,buy,n,price,dp):
        if ind>=n:
            return 0
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        
        if (buy==1):
            dp[ind][buy]=max(-price[ind]+self.solution_149_3_1(ind+1,0,n,price,dp),0+self.solution_149_3_1(ind+1,1,n,price,dp))
            
        else:    #if ind=n-1 so ind+2 will go out of bound base case is if ind>=n: return 0
            dp[ind][buy]=max(price[ind]+self.solution_149_3_1(ind+2,1,n,price,dp),0+self.solution_149_3_1(ind+1,0,n,price,dp))
            
        return dp[ind][buy]
    
    def solution_149_3_2(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1 for i in range(2)]for j in range(n)]
        return self.solution_149_3_1(0,1,n,prices,dp)