class Solution:
    def solution_350_4_1(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = list(sorted([p1, p2, p3, p4]))
        def solution_350_4_2(a, b):
            return points[b][0] - points[a][0], points[b][1] - points[a][1]
        length = lambda solution_350_4_2: math.sqrt(solution_350_4_2[0]**2 + solution_350_4_2[1]**2)
        
        l, b, t, r = solution_350_4_2(0, 1), solution_350_4_2(0, 2), solution_350_4_2(3, 1), solution_350_4_2(3, 2)
        sides = length(t) == length(b) == length(t) == length(r) > 0
        angles = l[0] * b[0] + l[1] * b[1] == t[0] * r[0] + t[1] * r[1] == 0
        return sides and angles