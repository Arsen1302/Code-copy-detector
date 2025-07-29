class Solution:
    def solution_1169_4(self, rectangles: List[List[int]]) -> int:
        maxLength = 0
        maxes = []
        for rect in rectangles:
            minimum = min(rect)
            maxes.append(minimum)
        maxLength = max(maxes)
        return maxes.count(maxLength)