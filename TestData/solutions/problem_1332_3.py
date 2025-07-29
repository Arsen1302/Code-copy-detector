class Solution:
    def solution_1332_3(self, milestones: List[int]) -> int:
        m, s = max(milestones), sum(milestones)
        return s - max(0, 2*m - s - 1)