class Solution:
    def solution_1488_4(self, num: int) -> int:
        
        # no digits contained, can return zero
        if not num:
            return 0
        
        # make an array to count the digits
        digits = [0]*10
        
        # check whether number is negative
        negative = num < 0
        num = abs(num)
        
        # find the digits and the smallest number not beeing zero
        # if we have a positive number (no leading zeros)
        starting_number = 9
        while num:
            # get the digits
            num, res = divmod(num, 10)
            
            # track digit frequency
            digits[res] += 1
            
            # save the smallest number in case we have a positive number
            if not negative and res:
                starting_number = min(starting_number, res)
        
        # initialize the result (for positive numbers we already put the smallest number)
        result = 0
        if not negative:
            result = starting_number
            digits[starting_number] -= 1
        
        if negative:
            
            # go through the numbers in reverse and attach them
            for index, amount in enumerate(reversed(digits)):

                # attach the digit amount times
                while amount:
                    result = result*10 - (9-index)
                    amount -= 1
            
        else:
            
            # go through the numbers and attach them
            for index, amount in enumerate(digits):

                # attach the digit amount times
                while amount:
                    result = result*10 + index
                    amount -= 1
            
        return result