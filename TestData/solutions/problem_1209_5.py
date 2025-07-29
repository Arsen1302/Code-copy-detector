class Solution:
    def solution_1209_5(self, x: int, y: int, points: List[List[int]]) -> int:
        ind = -1
        man = -1
        for i in points:
            if i[0] == x or i[1] == y:
                if man == -1 or (abs(i[0] - x) + abs(i[1] - y)) < man:
                    man = abs(i[0] - x) + abs(i[1] - y)
                    ind = points.index(i)
        return ind