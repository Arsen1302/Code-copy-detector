class Solution:
    def solution_710_5(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[i,j] for i in range(rows) for j in range(cols)] , key = lambda x: abs(x[0]-rCenter)+abs(x[1]-cCenter))