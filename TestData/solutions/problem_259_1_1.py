class Solution:
    def solution_259_1_1(self, x: int, y: int) -> int:
        def solution_259_1_2(num):
            res = []
            while num > 0:
                res.append(num % 2)
                num //= 2
            return ''.join(str(num) for num in res[::-1])
        
        if x < y:
            x, y = y, x
        
        bin_x, bin_y = solution_259_1_2(x), solution_259_1_2(y)
        res = 0
        s1, s2 = len(bin_x), len(bin_y)
        bin_y = '0' * (s1 - s2) + bin_y
        
        return sum(bin_x[i] != bin_y[i] for i in range(s1))