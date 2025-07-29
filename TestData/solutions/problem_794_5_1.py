class Solution:
    def solution_794_5_1(self, n: int, a: int, b: int, c: int) -> int:
        [a,b,c] = sorted([a,b,c])
        if a == 1: return n
        def solution_794_5_2(x,y): return x*y//math.gcd(x,y)
        AB, BC, AC, ABC, r, s = solution_794_5_2(a,b), solution_794_5_2(b,c), solution_794_5_2(a,c), solution_794_5_2(solution_794_5_2(a,b),c), n*a//3, n*a+1
        def solution_794_5_3(x): return x//a + x//b + x//c - x//AB - x//BC - x//AC + x//ABC
        while solution_794_5_3(s-1) - n > 0:
            m = (r+s)//2
            if solution_794_5_3(m) - n > 0: s = m
            else: r = m
        return max(i*((s-1)//i) for i in [a,b,c])
				
				
- Junaid Mansuri
(LeetCode ID)@hotmail.com