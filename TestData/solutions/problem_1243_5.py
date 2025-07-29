class Solution:
    def solution_1243_5(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x,y,r in queries:
            count = 0
            for a,b in points:
                if (x-a)*(x-a) + (y-b)*(y-b) <= r*r:
                    count += 1
            res.append(count)
        return res