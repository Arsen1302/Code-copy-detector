class Solution:
    def solution_1488_3(self, num: int) -> int:
        if num ==0 : return 0
        res , zero = '',''

        for i in str(num):
            if i != '-':
                if i=='0':
                    zero += i
                else:
                    res += i
                
        res = ''.join(sorted(res))
        
        if num < 0:
            return '-'+ res[::-1] + zero
        elif res and zero:
            return res[0] + zero + res[1:]
        else:
            return res