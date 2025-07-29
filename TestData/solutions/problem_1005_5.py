class Solution:
    def solution_1005_5(self, path):
        point, points = (0,0), {(0,0)}
        
        for dir in path:
            match dir:
                case "N": point = (point[0]+1, point[1])
                case "S": point = (point[0]-1, point[1])
                case "E": point = (point[0], point[1]+1)
                case "W": point = (point[0], point[1]-1)
            
            if point in points: return True
            else: points.add(point)
        
        return False