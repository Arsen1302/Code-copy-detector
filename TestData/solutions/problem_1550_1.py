class Solution:
    def solution_1550_1(self, circles: List[List[int]]) -> int:
        points = set()
        for x, y, r in circles:
            for dx in range(-r, r + 1, 1):
                temp = math.floor(math.sqrt(r ** 2 - dx ** 2))
                for dy in range(-temp, temp + 1):
                    points.add((x + dx, y + dy))
        return len(points)