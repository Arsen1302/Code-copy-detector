class Solution:
    def solution_1332_2(self, m: List[int]) -> int:
        return min(sum(m), 2 * (sum(m) - max(m)) + 1)