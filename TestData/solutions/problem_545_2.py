class Solution:
    def solution_545_2(self, p: int, q: int) -> int:
        # L*G = p*q  <=> L/q = p/G <=> L/p = q/G

        G = gcd(p,q)
        p//= G
        q//= G
        
        if p%2 == 0:
            return 2

        return q%2