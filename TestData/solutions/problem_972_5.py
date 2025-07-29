class Solution:
    def solution_972_5(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s<=queryTime<=e for s,e in zip(startTime, endTime))