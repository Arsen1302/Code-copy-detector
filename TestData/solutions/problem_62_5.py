class Solution:
    def solution_62_5(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        sets = {}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                a = None
                b = None
                if x2 == x1:
                    a = x1
                else:
                    a = (y2-y1)/(x2-x1)
                    b = y1-a*x1
                if (a,b) not in sets:
                    sets[(a,b)] = set()
                sets[(a,b)].add((x1, y1))
                sets[(a,b)].add((x2, y2))
        return max([len(v) for v in sets.values()])