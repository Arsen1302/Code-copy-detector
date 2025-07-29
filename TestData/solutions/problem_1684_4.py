class Solution:
    def solution_1684_4(self, a: int, b: int) -> int:
        result = ""
        a_bin, b_bin = bin(a).lstrip('0b'), bin(b).lstrip('0b')
        ones_in_b = b_bin.count('1')

        if len(a_bin) < len(b_bin):
            a_bin = abs(len(b_bin) - len(a_bin)) * ('0') + a_bin
        elif len(b_bin) < len(a_bin):
            b_bin = abs(len(b_bin) - len(a_bin)) * ('0') + b_bin
        
        zeroes_in_b = len(b_bin) - ones_in_b

        for i in range(len(a_bin)):
            if a_bin[i] == '0':
                if zeroes_in_b > 0:
                    result += '0'
                    zeroes_in_b -= 1
                elif ones_in_b > 0:
                    result += '1'
                    ones_in_b -= 1
            elif a_bin[i] == '1':
                if ones_in_b > 0:
                    result += '1'
                    ones_in_b -= 1
                elif zeroes_in_b > 0:
                    result += '0'
                    zeroes_in_b -= 1

        ans = int(result, 2)
        return ans