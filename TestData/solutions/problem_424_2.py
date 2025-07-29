class Solution:
    def solution_424_2(self, prices: List[int]) -> int:
        buy, sell = inf, 0
        for x in prices: 
            buy = min(buy, x - sell)
            sell = max(sell, x - buy)
        return sell