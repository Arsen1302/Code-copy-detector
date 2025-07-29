class Solution:
    def solution_1042_4(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        i = 1
        s = '0'
        while i < n:
            z = s + '1'
            s = s.replace('0',',').replace('1','0').replace(',','1')
            z += s[::-1]
            i += 1
            s = z
        return s[k-1]