class Solution:
    def solution_1331_1(self, n: int) -> bool:
        return sum(n%i == 0 for i in range(1, n+1)) == 3