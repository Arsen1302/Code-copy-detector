class Solution:
    def solution_424_5(self, prices: List[int]) -> int:
        buy, cooldown, sell = inf, 0, 0
        for x in prices: 
            buy = min(buy, x - cooldown)
            cooldown = sell 
            sell = max(sell, x - buy)
        return sell