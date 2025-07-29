class Solution:
    def solution_985_4_1(self, cuts: List[int], end: int) -> int:
        maxSpace = max(cuts[0], end-cuts[-1])
        for i in range(1,len(cuts)):
            maxSpace = max(maxSpace, cuts[i] - cuts[i-1])
        return maxSpace
    def solution_985_4_2(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        return self.solution_985_4_1(sorted(horizontalCuts), h) * self.solution_985_4_1(sorted(verticalCuts), w) % (10**9+7)