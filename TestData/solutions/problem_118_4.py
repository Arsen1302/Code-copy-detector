class Solution:
    def solution_118_4(self, n: int) -> int:
        if n < 0: return 0 #edge case 
        ans = d = tr = 0
        m = 1 # magnitude
        while n: 
            tr += d*m//10 #trailing digit
            n, d = divmod(n, 10) #leading &amp; current digit 
            ans += n * m
            if d == 1: ans += tr + 1
            elif d > 1: ans += m 
            m *= 10 
        return ans