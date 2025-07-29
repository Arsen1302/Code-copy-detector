class Solution:
    def solution_1427_4(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        row_cost = sum(rowCosts[min(startPos[0], homePos[0]):max(startPos[0], homePos[0]) + 1]) - rowCosts[startPos[0]]
        col_cost = sum(colCosts[min(startPos[1], homePos[1]):max(startPos[1], homePos[1]) + 1]) - colCosts[startPos[1]]
        return row_cost + col_cost