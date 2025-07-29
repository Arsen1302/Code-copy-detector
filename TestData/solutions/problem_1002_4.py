class Solution:
    def solution_1002_4(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        try:
            return factors[k-1]
        except:
            return -1