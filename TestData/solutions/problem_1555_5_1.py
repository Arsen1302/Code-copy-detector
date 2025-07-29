class Solution:    
    def solution_1555_5_1(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        amt = (m * n) - len(walls)
        walls_x, walls_y = defaultdict(list), defaultdict(list)
        ranges_x, ranges_y = defaultdict(list), defaultdict(list)
        for x, y in walls:
            insort_left(walls_x[x], y)
            insort_left(walls_y[y], x)
        def solution_1555_5_2(a, i, lim):
            if not a:
                return (0, lim)
            j = bisect_left(a, i)
            if j == len(a):
                return (a[-1]+1, lim)
            if j == 0:
                if a[j] < i:
                    return (a[0]+1, lim)
                return (0, a[0])
            return (a[j-1]+1, a[j])
        for x, y in guards:
            insort_left(ranges_x[x], solution_1555_5_2(walls_x[x], y, n))
            insort_left(ranges_y[y], solution_1555_5_2(walls_y[y], x, m))
        for d in ranges_x, ranges_y:
            for s in d:
                d[s] = self.solution_1555_5_3(d[s])
        y_list = sorted(ranges_y)
        for ranges in ranges_x, ranges_y:
            amt -= sum((c2 - c1) for cs in ranges.values() for c1, c2 in cs)
        for x, ys in ranges_x.items():
            for y1, y2 in ys:
                for y in y_list[bisect_left(y_list, y1):bisect_left(y_list, y2)]:
                    ip = min(bisect_left(ranges_y[y], (x,)), len(ranges_y[y])-1)
                    if x in range(*ranges_y[y][ip]) or (ip > 0 and x in range(*ranges_y[y][ip-1])):
                        amt += 1
        return amt
    
    def solution_1555_5_3(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for start, end in intervals:
            if not out:
                out.append((start, end))
            elif out[-1][1] >= start:
                out[-1] = out[-1][0], max(end, out[-1][1])
            else:
                out.append((start, end))
        return out