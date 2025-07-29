class Solution:
    def solution_782_2(self, n: int) -> int:
        if n <= 2:
            return 1

        primesList = [False]*2 + [True]*(n - 1)
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if not primesList[i]:
                continue
            for j in range(i * i, n + 1, i):
                primesList[j] = False
        
        primes = sum(primesList)    
        return (math.factorial(primes) * math.factorial(n - primes)) % (10 ** 9 + 7)