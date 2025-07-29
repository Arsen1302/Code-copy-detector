class Solution:
    def solution_553_3_1(self, n: int) -> int:
        if 8 <= n <= 11: return 11 # edge case 
        
        def solution_553_3_2(n): 
            """Return next palindromic number greater than x."""
            digits = [int(x) for x in str(n)]
            for i in reversed(range(len(digits)//2+1)): 
                if digits[i] < 9: break 
            else: return 10*n + 11
            digits[i] = digits[~i] = digits[i] + 1
            for ii in range(i): 
                digits[~ii] = digits[ii]
            for ii in range(i+1, len(digits)//2+1): 
                digits[ii] = digits[~ii] = 0
            return int("".join(map(str, digits)))
        
        def solution_553_3_3(x): 
            """Return True if x is prime."""
            if x <= 1: return False 
            if x % 2 == 0: return x == 2
            for k in range(3, int(sqrt(x))+1, 2): 
                if x % k == 0: return False
            return True 
        
        nn = n 
        k = 0
        while nn: 
            nn //= 10
            k += 1
            
        if not k&amp;1: n = 10**k + 1
        elif str(n) != str(n)[::-1]: n = solution_553_3_2(n)
        
        while True: 
            if solution_553_3_3(n): return n
            n = solution_553_3_2(n)