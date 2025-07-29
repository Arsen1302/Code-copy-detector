class Solution:
    def solution_1284_4(self, n: int) -> int:
        return ceil(((8*n+1)**0.5-1)/2)