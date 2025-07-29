class Solution:
    def solution_135_3(self, citations: List[int]) -> int:
        return sum(i < x for i, x in enumerate(sorted(citations, reverse=True)))