class Solution:
    def solution_1665_5(self, intervals: List[List[int]]) -> int:
        A = []
        for a,b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        y = x = 0
        for a, diff in sorted(A):
            x += diff
            y = max(y,x)
        return y