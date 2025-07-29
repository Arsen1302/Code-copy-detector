class Solution:
    def solution_83_5(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
                
        dp_cost = [float('inf')] * k
        dp_profit = [0] * k
        
        for price in prices:
            for i in range(k):
                if i == 0:
                    dp_cost[i] = min(dp_cost[i], price)
                    dp_profit[i] = max(dp_profit[i], price-dp_cost[i])
                else:
                    dp_cost[i] = min(dp_cost[i], price - dp_profit[i-1])
                    dp_profit[i] = max(dp_profit[i], price - dp_cost[i])
        
        return dp_profit[-1]