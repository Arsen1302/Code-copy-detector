class Solution:
    def solution_1656_4_1(self, n: int) -> bool:

        BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        def solution_1656_4_2(n, b): 
            return "0" if not n else solution_1656_4_2(n//b, b).lstrip("0") + BS[n%b]
        
        res = False
        for i in range(2,n-1):
            i_base = solution_1656_4_2(n, i)
            if i_base[::-1] == i_base:
                res = True
            else:
                return False
        
        return res