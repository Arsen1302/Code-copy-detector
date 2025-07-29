class Solution:
    def solution_91_4_1(self, n: int) -> bool:
        if n == 1: return True
        l = []
        def solution_91_4_2(n):
            c = 0
            for i in str(n):
                c += int(i) ** 2
            return c
        
        while n != 1:
            n = solution_91_4_2(n)
            if n in l:
                return False
            l.append(n)
        return True