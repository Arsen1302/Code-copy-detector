class Solution:
    def solution_1527_2_1(self, queries: List[int], intLength: int) -> List[int]:
	
        ans = []
			
        # number of palindromic numbers in base k with n digits can be found by the formulas: 
		# k, if n == 1 and (k - 1) * (k ** floor((n - 1) / 2)), if n > 1
		# we accumulate numbers for each possible length, starting with 1. 
		# for example: [10, 19, 109, 199, 1099...]
		
        limit = [10, 19]

        for i in range(3, intLength + 1):
            limit.append(limit[-1] + 9 * (10 ** int((i - 1) / 2)))
        
        def solution_1527_2_2(num):
            left = str(num)
            
            if intLength % 2 == 0:
                right = str(num)[::-1]
            else:
                right = str(num)[:-1][::-1]
            
            return int(left + right)
        
		# now we form our palindrome if the serial number is less or equal to the limit,
		# else we append -1 to our answer.
		# left part of the desired palindrome can be computed by following:
		# 10 ** digits + serial_number - 1 
		         
        if intLength % 2 == 0:
            digits = intLength // 2 - 1
        else:
            digits = intLength // 2
		
        for i in queries:
            if i <= limit[intLength - 1]:
                half = 10 ** digits + i - 1
                tmp = solution_1527_2_2(half)
                
                if len(str(tmp)) <= intLength:
                    ans.append(tmp)
                else:
                    ans.append(-1)
            else:
                ans.append(-1)
            
        return ans