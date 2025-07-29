class Solution:
    def solution_1209_2(self, x: int, y: int, points: List[List[int]]) -> int:
        result = None
        maximumDistance = float("inf")
        
        for index,point in enumerate(points):
            a,b = point
            distance = abs(x-a) + abs(y-b)
            if distance < maximumDistance and (x == a or y == b):
                maximumDistance = distance
                result = index
        
        return result if result != None else -1