class Solution:
    def solution_1105_1(self, points: List[List[int]]) -> int:
        l = []
        for i in points:
            l.append(i[0])
        a = 0
        l.sort()
        for i in range(len(l)-1):
            if l[i+1] - l[i] > a:
                a = l[i+1] - l[i]
        return a