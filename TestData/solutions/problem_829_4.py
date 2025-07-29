class Solution:
    def solution_829_4(self, points: List[List[int]]) -> int:
        answer =0
        for i in range(len(points)-1):
            x, y = points[i]
            x1, y1 = points[i+1]
            answer += max(abs(x1-x), abs(y1-y))
        return answer