class Solution:
    def solution_1648_3(self, num: str) -> str:
        dict_frequency = {}
        for char in num:
            if char in dict_frequency:
                dict_frequency[char] += 1
            else:
                dict_frequency[char] = 1
        left_str = ''
        right_str = ''
        # For placing the number at the middle.
        odd_digit = 0
        for i in range(10, 0, -1):
            digit = str(i-1)
            if digit not in dict_frequency:
                continue
            count = dict_frequency[digit]
            if count % 2 == 0:
                freq = count // 2
                for j in range(freq):
                    left_str += digit
                    right_str = digit + right_str
                dict_frequency[digit] = 0
            
            else:
                # checking if it is not already assisgned           then assigned the largest one.
                if odd_digit == 0:
                    odd_digit = digit
                freq = count // 2
                
                for j in range(freq):
                    left_str += digit
                    right_str = digit + right_str
                dict_frequency[digit] = 1
        # Concating the left one to the right one.
        final = ''
        if odd_digit:
            final = left_str + odd_digit + right_str
        else:
            final = left_str + right_str
        # if leading '0' and trailing '0' is present then removing it.
        final = final.strip('0')
        # if only '0' is present then we are left with only empty string, so assigning one '0' char and returning it.
        if not len(final):
            final = '0'
        return str(int(final))