class Solution:
    def solution_149_4(self, prices: List[int]) -> int:
        buy, sell = inf, 0
        for x in prices:
            buy = min(buy, x)
            sell = max(sell, x - buy)
        return sell