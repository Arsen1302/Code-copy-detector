class Solution:
    def solution_1021_5(self, numBottles: int, numExchange: int) -> int:
        empty=numBottles
        fill=numBottles
        while True:
            if empty//numExchange>0:
                fill+=empty//numExchange
                empty=empty%numExchange+empty//numExchange
            else:
                return fill