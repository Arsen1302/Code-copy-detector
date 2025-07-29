class Solution:
    def solution_295_4(self, num):
        primes = {2, 3, 5, 7, 13, 17, 19, 31}
        for item in primes:
            if (2**(item-1))*((2**item)-1) == num:
                return True
        return False