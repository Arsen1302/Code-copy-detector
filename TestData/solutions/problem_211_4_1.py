class Solution:
    def solution_211_4_1(self, k):
	    """
		Auxiliary/helper function to return a count of the number of k digit numbers
		This would be 10**k - 10**(k-1) but with some algebra it reduces to the formula below
		"""
		# optimized alternative to 10**k - 10**(k-1)
		#           =    10**([1 + k-1]) - 10**(k-1)
		#           =    [10*(10**(k-1)] - [1*(10**(k-1))]
		#           = [10-1]*(10**(k-1))
        return             9*(10**(k-1))
    
    def solution_211_4_2(self, n: int) -> int:
	    """
		Find the nth digit in the series 123456789101112...
		We start by determining what portion of the series n lives in (i.e. what size of k for k digit numbers)
		Then we determine which k-digit number n and which digit i of the number to return
		Then we isolate and return that digit
		"""
        k = 1
        while n>k*self.solution_211_4_1(k):
			# n is big enough to bypass the k-digit numbers
            n -= k*self.solution_211_4_1(k)
            k += 1

        # digit appears in a k-digit number
        # get the ith digit of the nth k-digit number
        n -= 1             # to simplify modular arithmetic
        n, i = n//k, n%k   # find i and n-1
        n  += 10**(k-1)    # n is now the nth k-digit number
        n //= 10**(k-i-1)  # get rid of all digits after the ith
        return n % 10      # return the ith digit