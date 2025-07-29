class Solution:
    def solution_1550_5(self, circles: List[List[int]]) -> int:
        intervals = [[] for _ in range(201)]
        for x, y, r in circles: 
            intervals[x].append((y-r, y+r))
            for dx in range(1, r+1): 
                dy = int(sqrt(r**2 - dx**2))
                intervals[x+dx].append((y-dy, y+dy))
                intervals[x-dx].append((y-dy, y+dy))
        
        ans = 0 
        for interval in intervals: 
            if interval: 
                end = -inf
                for i, (lo, hi) in enumerate(sorted(interval)): 
                    if end < lo: 
                        if i: ans += end - start + 1
                        start, end = lo, hi 
                    else: end = max(end, hi)
                ans += end - start + 1
        return ans