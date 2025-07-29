class Solution:
    def solution_172_2(self, n: int) -> bool:
        # Solution 1 using recursion
        while n % 4 == 0 and n > 0:
            return self.solution_172_2(n/4)
        return n == 1
        
        # Solution 2 iteration
        if n == 1:
            return True
        if n % 4:
            return False
        while n > 1:
            if n % 4:
                return False
            n //= 4
        return n == 1
        
        # Solution 3 using bit manipulation
        '''
        Once we write numbers in it's binary representation, from there we can observe:=>
        i. 000001 , power of 2 and 4
        ii. 000010, power of only 2
        iii. 000100 , power of 2 and 4
        iv. 001000, power of only 2
        v. 010000 , power of 2 and 4
        vi. 100000, power of only 2
        We can see if the set bit is at an odd position and is a power of 2, it's also power of 4.
        '''
        return n.bit_length() &amp; 1 and not(n &amp; (n-1))