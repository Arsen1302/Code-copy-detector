class Solution:
    def solution_378_1(self, n: int) -> int:
        
        dp = [float('inf')] * (n+1)	
		## Intialize a dp array to store the solutions of sub problems i.e. number of steps needed
	
        dp[1] = 0
		## Intially first element of dp array with 0 as 'A' is already present and we haven't consumed any steps yet. 
		## As the value of n is from [1,3000] and initally 'A' is already present so we don't need to bother about the dp[0]
        
        divisors = []
		## This is to store the divisors of N
		
        for i in range(1, n//2 + 1):
            if n % i == 0:
                divisors.append(i)
		## We have stored all the divisors. For n = 10, divisors = [1,2,5]
        
        for j in divisors:
            dp[j] += 1
			##To copy the current number of A's, we add one step
			
            for i in range(j+1, n+1):
                if i % j == 0:
				## We can only form the string length which is divisible by j 
                    dp[i] = min(dp[i], dp[i-j] + 1)
					## Compare with previous number of steps and update with the minimum
        return dp[-1]
		#Return last value of dp i.e. N