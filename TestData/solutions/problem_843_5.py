class Solution:
    def solution_843_5(self, ma: List[List[int]]) -> int:
        n = len(ma)
        m = len(ma[0])
        l = []
        for i in range(m):
            l.append([ma[n-1][i],i])
        l.sort()
        for i in range(n-2,-1,-1):
            t = []
            for j in range(len(ma[0])):
                if l[0][1] == j:
                    ma[i][j] += l[1][0]
                else:
                    ma[i][j] += l[0][0]
                t.append([ma[i][j],j])
            t.sort()
            l = t.copy()
        return min(ma[0])