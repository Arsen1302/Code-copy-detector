class Solution:
    def solution_1571_1(self, candidates: List[int]) -> int:
        return max(sum(n &amp; (1 << i) > 0 for n in candidates) for i in range(0, 24))