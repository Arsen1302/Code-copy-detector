class Solution:
    def solution_148_4_1(self, num: str) -> bool:
        n = len(num)
        def solution_148_4_2(a, b, i):
            nonlocal n, num
            c, c_str = a+b, str(a+b)                   # sort of do-while loop
            c_l = len(c_str)
            while i+c_l <= n and num[i:i+c_l] == c_str:
                a, b = b, c
                c, c_str = a+b, str(a+b)
                i, c_l = i+c_l, len(c_str)
            return i == n                              # when index reach to the end
                
        for i in range(1, n):                          # try out all first value possibilities
            if i > 1 and num[0] == '0': break          # leading zero non-zero number, like '02'
            first = int(num[:i])
            for j in range(i+1, n):                    # try out all second value possibilities
                if j > i+1 and num[i] == '0': break    # leading zero non-zero number, like '02'
                second = int(num[i:j])
                if solution_148_4_2(first, second, j):       # given first &amp; second str, see if it can reach to the end
                    return True 
        return False