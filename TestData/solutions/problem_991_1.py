class Solution:
    def solution_991_1(self, prices: List[int]) -> List[int]:
        len_prices = len(prices)
        i = 0
        while i <= len_prices-2:
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j] and j > i:
                    prices[i] = prices[i] - prices[j]
                    break
            
            i += 1
        
        return prices