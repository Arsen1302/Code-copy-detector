class Solution:
    def solution_118_3(self, n: int) -> int:
        return sum(str(i).count("1") for i in range(1, n+1))