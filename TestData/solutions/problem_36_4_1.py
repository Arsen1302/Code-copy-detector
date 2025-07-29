class Solution:
    def solution_36_4_1(self,ind,buy,cap,n,price,dp):
        if ind==n:
            return 0
        if cap==0:
            return 0
        if dp[ind][buy][cap]!=-1:
            return dp[ind][buy][cap]
        if buy:
            profit=max(-price[ind]+self.solution_36_4_1(ind+1,0,cap,n,price,dp),0+self.solution_36_4_1(ind+1,1,cap,n,price,dp))
        else:
            profit=max(price[ind]+self.solution_36_4_1(ind+1,1,cap-1,n,price,dp),0+self.solution_36_4_1(ind+1,0,cap,n,price,dp))
        dp[ind][buy][cap]=profit
        return dp[ind][buy][cap]
    
    def solution_36_4_2(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1 for i in range(3)]for j in range(2)]for k in range(n)]
        return self.solution_36_4_1(0,1,2,n,prices,dp)