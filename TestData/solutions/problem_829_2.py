class Solution:
    def solution_829_2(self, points: List[List[int]]) -> int:
        d=0
        for i in range(len(points)-1):
            d+=max(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        return d