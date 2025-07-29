class Solution:
    def solution_1448_1(self, ss: List[str]) -> int:
        return max(s.count(" ") for s in ss) + 1