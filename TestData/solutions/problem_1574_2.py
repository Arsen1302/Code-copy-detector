class Solution:
    def solution_1574_2(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        stockPrices.sort(key = lambda x: x[0])
        ans = 1
        for i in range(1,len(stockPrices)-1):
            if (stockPrices[i+1][1]-stockPrices[i][1])*(stockPrices[i][0]-stockPrices[i-1][0]) != (stockPrices[i+1][0]-stockPrices[i][0])*(stockPrices[i][1]-stockPrices[i-1][1]):
                ans += 1
        return ans