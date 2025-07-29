class Solution:
    def solution_1372_1(self, n: int, rides: List[List[int]]) -> int:
        
        d = {}
        for start,end,tip in rides:
            if end not in d:
                d[end] =[[start,tip]]
            else:
                d[end].append([start,tip])
        
       
        dp = [0]*(n+1)
        dp[0] = 0
        
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            if i in d:
                temp_profit = 0
                for start,tip in d[i]:
                    if (i-start)+tip+dp[start] > temp_profit:
                        temp_profit = i-start+tip+dp[start]
                dp[i] = max(dp[i],temp_profit)
                
                
        return dp[-1]