class Solution:
    def solution_1046_5(self, n: int) -> int:
        return (n+1)*(n-1)//4 if n % 2 else n*n//4