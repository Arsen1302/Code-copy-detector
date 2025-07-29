class Solution:
    def solution_211_2(self, n: int) -> int:
        """
        imagine the number you need to find have 4 digit
        so you need to go throught all num have 1 digit, 2 digit, 3 digit
        number have 1 digit:  10 ** 1 - 1 = 9 => 9 * 1 = 9 digit
        number have 2 digit:  10 ** 2 - 1 = 90 => 90 * 2 = 180 digit
        number have 3 digit:  10 ** 3 - 1 = 900 => 900 * 3 = 2700 digit
        ...
        just subtract until you find how many digit of the number you need to find
        when you got the number of digit 
        """
        if n < 10:
            return n
        
        number_of_digit = 0 # check how many digit of the number you need to find
        while n > 0:
            number_of_digit += 1
            n -= 9 * 10 ** ((number_of_digit - 1)) * number_of_digit
        n += 9 * 10 ** ((number_of_digit - 1)) * number_of_digit
        
        """ 
        print(n , number_of_digit) if you dont understand 
        after subtract you will find number of digit
        all you need to do now is find exactly number by just a little bit of math
        """ 
        tmp_num = 0
        
        if n % number_of_digit == 0:
            n //= number_of_digit 
            tmp_num += 10 ** ((number_of_digit - 1)) - 1
            return int(str(tmp_num + n)[-1])
        else:
            n /= number_of_digit
            digit = int((n * number_of_digit) % number_of_digit)
            tmp_num += 10 ** ((number_of_digit - 1)) - 1
            return int(str(int(tmp_num + n) + 1)[digit - 1])