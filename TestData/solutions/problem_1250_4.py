class Solution:
    def solution_1250_4(self, n: int, k: int) -> int:
        return (x:=lambda y: 0 if not y else y%k + x(y//k))(n)