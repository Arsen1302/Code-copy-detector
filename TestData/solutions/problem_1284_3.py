class Solution:
    def solution_1284_3(self, n: int) -> int:
        return ceil((sqrt(1 + 8*n)-1)/2)