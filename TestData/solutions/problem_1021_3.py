class Solution:
    def solution_1021_3(self, numBottles: int, numExchange: int) -> int:
        bottles , empty = numBottles , numBottles
        
        while empty >= numExchange:
            empty -= numExchange - 1
            bottles += 1
        
        return bottles