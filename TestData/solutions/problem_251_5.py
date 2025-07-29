class Solution:
    def solution_251_5(self, points: List[List[int]]) -> int:
        # Line Sweep
        points = sorted(points, key = lambda x:x[0])
        start = points[0][0]
        end = points[0][1]
        ans = len(points)
        for i in range(1,len(points)):
            if points[i][0] > end:
                start = points[i][0]
                end = points[i][1]
            else:
                start = points[i][0]
                ans -= 1
                if end > points[i][1]:
                    end = points[i][1]
        return ans