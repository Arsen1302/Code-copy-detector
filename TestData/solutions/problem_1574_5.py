class Solution:
	def solution_1574_5(self, stockPrices: List[List[int]]) -> int:
		n = len(stockPrices)
		if n == 2: return 1
		if n == 1: return 0

		day, price = [],[]
		for d, p in stockPrices:
			day.append(d)
			price.append(p)
		stocks = sorted(zip(day,price))
		line = 1
		for i in range(1,n-1):
			p1, p2, p3 = stocks[i-1], stocks[i], stocks[i+1]        
			if (p1[1]-p2[1])*(p2[0]-p3[0]) != (p2[1]-p3[1])*(p1[0]-p2[0]): 
				line += 1
		return line