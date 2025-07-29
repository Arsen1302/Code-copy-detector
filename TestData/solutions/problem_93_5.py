class Solution:
    def solution_93_5(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [0]*n
        for i in range(2,int(n**0.5)+1):
            for j in range(i**2,n,i):
                isPrime[j] = 1
        return n - sum(isPrime) - 2