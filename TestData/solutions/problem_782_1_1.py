class Solution:
    def solution_782_1_1(self, n: int) -> int:
        # find number of prime indices
        # ways to arrange prime indices
        # is prime indices solution_782_1_3
        # amount of non-prime indices is
        # n - prime indices 
        # the solution_782_1_3 of non - prime indices
        # times the solution_782_1_3 of prime indices
        # is the amount of ways to arrange the 
        # prime numbers and i be valid 
        # use helper to find solution_782_1_3 of a number
        # use helper to see if a number is prime
        # time O(n ^ 2) space O(1)

        def solution_782_1_2(num):
            if num <= 1:
                return False
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    return False
            return True

        def solution_782_1_3(num):
            res = 1
            for i in range(1, num + 1):
                res *= i
            return res
        
        primes = 0
        for num in range(1, n + 1):
            if solution_782_1_2(num):
                primes += 1
        return int(solution_782_1_3(primes) * solution_782_1_3(n - primes) % (10**9 + 7))