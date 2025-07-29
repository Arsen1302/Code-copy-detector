class Solution:
    def solution_991_2(self, prices: List[int]) -> List[int]:
        stack = [] # taking a empty stack. 
        for i in range(len(prices)): # traversing through the provided prices list. 
            while stack and (prices[stack[-1]] >= prices[i]): # comparing the previous element with current element as descibed in the question to calculate the discount. 
                prices[stack.pop()] -= prices[i] # reducing the price of the current elem from previous. 
            stack.append(i) # In stack we`ll just stores the index of the prices. Using those indexes will make changes in the prices list itself. 
        return prices # returing the updated prices as we made changes in the provided list itself.