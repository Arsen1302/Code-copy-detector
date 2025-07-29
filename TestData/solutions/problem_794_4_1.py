class Solution:
    def solution_794_4_1(self, n: int, a: int, b: int, c: int) -> int:
        ab = a*b//math.gcd(a,b)
        ac = a*c//math.gcd(a,c)
        bc = b*c//math.gcd(b,c)
        abc = a*bc//math.gcd(a,bc)
        
        def solution_794_4_2(m):
            tot = m//a + m//b + m//c - m//ab - m//bc -m//ac +m//abc
            return tot>=n

        l,r = 1,10**10
        while l<r:
            m=(l+r)//2
            if solution_794_4_2(m): r=m
            else: l=m+1
        return l