class Solution:
    def solution_1565_3(self, num: int, k: int) -> int:
        num_str = str(num)
        temp = ''
        w_s, c = 0, 0
        for w_e in range(len(num_str)):
            r_c = num_str[w_s:w_e+1]
            temp = r_c
            if len(temp) == k:
                if int(temp) != 0 and num % int(temp) == 0:
                    c += 1
                w_s += 1
        return c