class Solution(object):
    def solution_78_2(self, n):
        # Negative Number Edge Case
        if(n < 0):
            return -1
        # Initialize output...
        output = 0
        # Keep dividing n by 5 &amp; update output...
        while(n >= 5):
            n //= 5
            output += n
        return output    # Return the output...