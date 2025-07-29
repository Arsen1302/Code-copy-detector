class Solution:
    def solution_837_5(self, n: int) -> int:
        plus = 0
        product = 1
        n = str(n)
        for i in n:
            plus = plus + int(i)
            product = product * int(i)
        return product - plus