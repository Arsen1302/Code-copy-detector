class Solution:
    def solution_1046_1(self, n: int) -> int:
        if(n%2!=0):
            n=n//2
            return n*(n+1)
        else:
            n=n//2
            return n**2