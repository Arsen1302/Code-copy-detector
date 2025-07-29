class Solution:
    def solution_837_1(self, n: int) -> int:
        p,s=1,0
        while n!=0:
            p*=(n%10)
            s+=(n%10)
            n//=10
        return p-s