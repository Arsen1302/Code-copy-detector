class Solution:
    def solution_1105_2(self, points: List[List[int]]) -> int:
        return max([t - s for s, t in zip(sorted([r[0] for r in points]), sorted([r[0] for r in points])[1:])])