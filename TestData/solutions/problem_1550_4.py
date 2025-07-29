class Solution:
    def solution_1550_4(self, circles: List[List[int]]) -> int:
        points = set()
        for cx, cy, r in circles:
            r2 = r * r
            for x in range(-r, r + 1):
                y_05 = int(pow(r2 - x * x, 0.5))
                for y in range(-y_05, y_05 + 1):
                    points.add((cx + x, cy + y))
        return len(points)