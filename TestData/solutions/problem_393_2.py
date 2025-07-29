class Solution:
    def solution_393_2(self, num: int) -> int:
        # larger digit to swap, digit position of this digit
        high_digit = high_pos = 0
        
        # smaller digit to swap, digit position of this digit
        low_digit = low_pos = 0
        
        # greatest digit seen so far, digit postion of this digit
        cur_high_digit, cur_high_pos = -1, 0
        
        # current digit position
        pos = 1
        
        res = num
        while num: # iterate through digits from right to left
            digit = num % 10
            
            # if digit is greatest digit yet
            if digit > cur_high_digit:
                cur_high_digit, cur_high_pos = digit, pos
            
            # if digit is less than greatest digit yet
            elif digit < cur_high_digit:
                # set the digits to swap as the greatest digit yet, and this digit
                high_digit, high_pos = cur_high_digit, cur_high_pos
                low_digit, low_pos = digit, pos
            
            pos *= 10
            num //= 10
        
        # swap the digits
        res += high_digit*(low_pos - high_pos) + low_digit*(high_pos - low_pos)
        return res