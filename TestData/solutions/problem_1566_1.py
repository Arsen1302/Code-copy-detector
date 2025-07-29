class Solution:
    def solution_1566_1(self, n: List[int]) -> int:
        n = list(accumulate(n))
        return sum(n[i] >= n[-1] - n[i] for i in range(len(n) - 1))