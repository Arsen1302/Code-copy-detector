class Solution:
    def solution_782_5(self, n: int) -> int:
	
        count, fact1, fact2, g = 1, 1, 1, 1000000007
        
    #calculate number of prime and non-prime numbers
        
        for i in range(3,n+1):
            count += 1
            for j in range(2,i-1):
                if i % j == 0:
                    count -= 1
                    break
        m = n - count
        if m > count:
            m, count = count, m
    
    #calculate the factorials
    
        for i in range(1,count+1):
            fact1 *= i
            if i == m:
                fact2 = fact1
                
    #mod operation
    
        return ((fact2 * fact1) % g)