class Solution:
    def solution_1427_2(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        if startPos[0] < homePos[0]:
            cost += sum(rowCosts[r] for r in range(startPos[0] + 1,
                                                   homePos[0] + 1))
        elif startPos[0] > homePos[0]:
            cost += sum(rowCosts[r] for r in range(startPos[0] - 1,
                                                   homePos[0] - 1, -1))
        if startPos[1] < homePos[1]:
            cost += sum(colCosts[c] for c in range(startPos[1] + 1,
                                                   homePos[1] + 1))
        elif startPos[1] > homePos[1]:
            cost += sum(colCosts[c] for c in range(startPos[1] - 1,
                                                   homePos[1] - 1, -1))
        return cost