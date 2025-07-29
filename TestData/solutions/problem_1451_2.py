class Solution:
    def solution_1451_2(self, left: int, right: int) -> str:
        #Step1: count the num of trailing zeros
        factor_two, factor_five = 0, 0
        curr_factor = 2
        while curr_factor <= right:
            factor_two += (right // curr_factor) - ((left - 1) // curr_factor)
            curr_factor *= 2
        curr_factor = 5
        while curr_factor <= right:
            factor_five += (right // curr_factor) - ((left - 1) // curr_factor)
            curr_factor *= 5
        trailing_zeros = min(factor_two, factor_five)
        
        #Step2: Multiply until it gets too big, while dividing 2 and 5
		divide_two_so_far, divide_five_so_far = 0, 0
        curr_num = 1
        for i in range(left, right + 1):
            multiply = i
            while multiply % 2 == 0 and divide_two_so_far < trailing_zeros:
                multiply //= 2
                divide_two_so_far += 1
            while multiply % 5 == 0 and divide_five_so_far < trailing_zeros:
                multiply //= 5
                divide_five_so_far += 1
            curr_num *= multiply
            if curr_num >= 10 ** 10:
                break
        
        #if the number doesn't get too large (less than or equal to 10 digits)
        if curr_num < 10 ** 10:
            return str(curr_num) + 'e' + str(trailing_zeros)
        
        #Step2: if the number exceeds 10 ** 10, then keep track of the first and last digits
        first_digits, last_digits = int(str(curr_num)[:12]), int(str(curr_num)[-5:])
        start = i + 1
        for i in range(start, right + 1):
            multiply = i
            while multiply % 2 == 0 and divide_two_so_far < trailing_zeros:
                multiply //= 2
                divide_two_so_far += 1
            while multiply % 5 == 0 and divide_five_so_far < trailing_zeros:
                multiply //= 5
                divide_five_so_far += 1
            first_digits = int(str(first_digits * multiply)[:12])
            last_digits = int(str(last_digits * multiply)[-5:])
        
		#output
        return str(first_digits)[:5] + '...' + '{:>05d}'.format(last_digits) + 'e' + str(trailing_zeros)