class Solution:
    def solution_1684_3(self, num1: int, num2: int) -> int:

        # find the numbers of ones in nums
        two_ones = bin(num2).count("1")

        # now count the number of ones in num1 we want to
        # delete
        ones_bin = bin(num1)[2:]

        # find the highest bit in ones
        highest_bit = (1 << (len(ones_bin)-1)) if len(ones_bin) > 1 or ones_bin[0] == '1' else 0

        # set all ones that are included in num1 so we minimize the xor
        # as 1^1 = 0
        result = 0
        for ch in ones_bin:

            # guard clause
            if not two_ones:
                break

            if ch == '1':
                result |= highest_bit
                two_ones -= 1
            highest_bit = highest_bit >> 1
        
        # now go through binary one and set the leftover ones
        comp = 1
        while two_ones:
            if not result&amp;comp:
                result |= comp
                two_ones -= 1
            comp = comp << 1
        return result