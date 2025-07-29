class Solution:
    def solution_1180_4_1(self, m: int) -> int:
        def solution_1180_4_2(x):
            return x**(1. / 3)

        # Find the first tetrahedral number greater than
        # or equal to m.
        x = solution_1180_4_2(sqrt(3)*sqrt(243*(m**2) - 1) + 27*m)
        n = ceil(x/solution_1180_4_2(9) + 1/(solution_1180_4_2(3)*x) - 1)
        
        # If m is the nth tetrahedral number, return the
        # nth triangular number (the base).
        t_n =n*(n+1)*(n+2) // 6 
        if m == t_n:
            return n*(n+1)//2

        # Otherwise, we must adjust the answer.
        ans = n*(n+1)//2
        j = t_n + 1
        while m < j:
            j -= n
            ans -= 1
            n -= 1

        return ans + 1