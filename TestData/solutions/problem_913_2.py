class Solution:
    def solution_913_2(self, n: int) -> str:
        return "a"*n if n%2 == 1 else "a"*(n-1)+"b"