class Solution:
    def solution_1311_4_1(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n==1:
            return x
        if n<0:
            n = -1 * n
            return 1/(self.solution_1311_4_1(x,n))
        elif n%2 == 0:
            halfvalue = self.solution_1311_4_1(x,n//2)
            return halfvalue * halfvalue
        else:
            oddhalfvalue = self.solution_1311_4_1(x,(n-1)//2)
            return oddhalfvalue * oddhalfvalue * x
    def solution_1311_4_2(self, n: int) -> int:
        MOD = 10**9 + 7
        primes = 4
        evens = 5
        ans = 1 
        if n%2 == 0:
            odd_indexes = even_indexes = n//2
        else:
            odd_indexes = n//2
            even_indexes = odd_indexes + 1
        ans1 = (pow(primes,odd_indexes,1_000_000_007)) % MOD
        ans2 = (pow(evens,even_indexes,1_000_000_007)) % MOD
        ans = (ans1 * ans2) % MOD
        return int(ans)