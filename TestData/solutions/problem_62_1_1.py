class Solution:
    def solution_62_1_1(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def solution_62_1_2(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return inf
            return (y1-y2)/(x1-x2)
        
        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i+1:]):
                slope = solution_62_1_2(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans+1