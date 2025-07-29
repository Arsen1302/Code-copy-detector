class Solution:
    def solution_728_3(self, heights: List[int]) -> int:
        return sum(sorted(heights)[i] != heights[i] for i in range(len(heights)))