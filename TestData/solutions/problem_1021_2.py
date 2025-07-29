class Solution:
    def solution_1021_2(self, numBottles: int, numExchange: int) -> int:
        drank , left = [numBottles] * 2
        
        while left >= numExchange:
            left -= numExchange - 1
            drank += 1
        
        return drank