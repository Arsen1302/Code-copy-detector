class Solution:
    def solution_782_3_1(self, n: int) -> int:
        if n==1:
            return 1
        def solution_782_3_2(num):
            sqrt=int(num**(1/2))
            for j in range(2,sqrt+1):
                if num%j==0:
                    return False
            return True
        prime=0
        composite=1# Keeping 1 in composite, though it is neither prime nor comp.
        mod=10**9+7
        for i in range(2,n+1):
            if solution_782_3_2(i):
                prime+=1
            else:
                composite+=1
        def solution_782_3_3(x):
            if x==1:
                return 1
            return x*solution_782_3_3(x-1)
        return solution_782_3_3(prime)*solution_782_3_3(composite)%mod