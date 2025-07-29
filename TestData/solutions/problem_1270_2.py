class Solution:
    def solution_1270_2(self, s: str) -> int:
        ans = n = len(s)
        zero, one = 0, 0
        for c in s:                                    # count number of 0 &amp; 1s
            if c == '0':
                zero += 1
            else:
                one += 1
        if abs(zero - one) > 1: return -1              # not possible when cnt differ over 1  
        if zero >= one:                                # '010101....' 
            s1 = '01' * (n // 2)                       # when zero == one
            s1 += '0' if n % 2 else ''                 # when zero > one 
            cnt = sum(c1 != c for c1, c in zip(s1, s))
            ans = cnt // 2
        if zero <= one:                                # '101010....'
            s2 = '10' * (n // 2)                       # when zero == one
            s2 += '1' if n % 2 else ''                 # when one > zero 
            cnt = sum(c2 != c for c2, c in zip(s2, s))
            ans = min(ans, cnt // 2)
        return ans