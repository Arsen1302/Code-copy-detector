class Solution:
    def solution_716_4(self, points: List[List[int]]) -> bool:
        x_diff_01 = points[0][0] - points[1][0]
        y_diff_01 = points[0][1] - points[1][1]

        x_diff_12 = points[1][0] - points[2][0]
        y_diff_12 = points[1][1] - points[2][1]

        return (x_diff_01*y_diff_12) != (x_diff_12*y_diff_01)