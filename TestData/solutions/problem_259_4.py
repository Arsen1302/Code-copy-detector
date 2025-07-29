class Solution:
    def solution_259_4(self, x: int, y: int) -> int:

        # String solution
		# TC O(n) SC O(1)
        longer = len(bin(y))-2 
        if x > y: longer = len(bin(x))-2
		 # 2 lines above for padding 0's
            
        # turn both x and y to binary, keep count of mismatches with count variable
        x, y, count = format(x, '0b').zfill(longer), format(y, '0b').zfill(longer), 0 
        for i in range(len(x)):
            if x[i] != y[i]: count += 1
        return count

        # bit manipulation solution
		# TC O(n) SC O(1)
        xor = x ^ y # XOR your two integers
        ham = 0 # store number of 1's from the XOR operation
        while xor != 0: # while you have bits to check
            ham += xor % 2 # increase ham when a 1 is seen
            xor >>= 1 # right shift
        return ham