class Solution:
    def solution_1656_5_1(self, n: int) -> bool:

        def solution_1656_5_2(n, base):
            ans = ''
            while n >= 1:
                ans = str(n % base) + ans
                n //= base 
            return ans
        
        for i in range(2, n - 1):
            res = solution_1656_5_2(n, i)
            if res != res[::-1]:
                return False

        return True