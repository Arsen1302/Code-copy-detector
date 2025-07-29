class Solution:
    def solution_135_5(self, citations: List[int]) -> int:
        return max((i+1 for i, x in enumerate(sorted(citations, reverse=True)) if i < x), default=0)