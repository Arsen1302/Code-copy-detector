class Solution:
    def solution_1574_4_1(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def solution_1574_4_2(self, p1, p2):
        slope_x, slope_y = p2[0] - p1[0], p2[1] - p1[1]
        g = self.solution_1574_4_1(slope_x, slope_y)
        return (slope_x // g, slope_y // g)
        
    def solution_1574_4_3(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        slope = (0, 0)
        for i in range(1, len(points)):
            new_slope = self.solution_1574_4_2(points[i-1], points[i])
            if new_slope != slope:
                ans += 1
            slope = new_slope
        return ans