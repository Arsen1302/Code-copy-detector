class Solution:
    def solution_1025_5(self, low, high):
        odds = 0
        
        for i in range(low,high+1):
            odds += i % 2
        
        return odds