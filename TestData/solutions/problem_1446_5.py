class Solution:
    def solution_1446_5(self, prices: List[int]) -> int:
	    #initiate res which will store the subsequent sum, 
		# and count which will keep a count of adjacent values who have a difference on '1' 
		# (Basically keeping in mind that we need to find the longest possible period)
        res,count = 0,1
        for i in range(1,len(prices)):
            if prices[i] + 1 == prices[i-1]:
                count += 1  #Hint 2 being used
            else:
                res += (count * (count+1))//2 #Finding that formula, a bit of brainstorming helps reach this
                count = 1 #resetting count as the next longest subbarrays with each subsequent elements that differ by '1' will be counted again from the beginning
        res += (count * (count+1))//2
        return res