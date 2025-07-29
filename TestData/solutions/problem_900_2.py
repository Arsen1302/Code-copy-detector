class Solution:
    def solution_900_2(self, n: int) -> int:
        return (math.factorial(n * 2) >> n) % (10**9 + 7)