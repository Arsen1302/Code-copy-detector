class Solution:
    def solution_135_4(self, citations: List[int]) -> int:
        return next((len(citations)-i for i, x in enumerate(sorted(citations)) if len(citations)-i <= x), 0)