class Solution:
    def solution_118_1(self, n: int) -> int:
        
        #O(logn) mathematical solution
        #intervals of new 1s: 0-9, 10-99, 100-999, 1000,9999... 
            #each interval yields 1,10,100,etc. new '1's respectively
		#first and foremost, we want to check how many of each interval repeats 
        #conditions for FULL yield when curr%upper bound+1: 1 <=, 19 <=, 199 <=...
        #conditions for PARTIAL yielf when curr%upper bound+1: None, 10 <= < 19,  100 <= < 199, 1000 <= < 1999 ... 
        
        ans = 0
        for i in range(len(str(n))):
            curr = 10**(i+1)
            hi,lo = int('1'+'9'*i), int('1'+'0'*i)
            ans += (n//curr) * 10**i
            if (pot:=n%curr) >= hi: ans += 10**i
            elif lo <= pot < hi: 
                ans += pot - lo + 1
        return ans