class Solution:
    def solution_1453_2_1(self, n: int, startPos: List[int], s: str) -> List[int]:
        d = {'U':(-1, 0),'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
        m = len(s)
        ans = [0]*m
        
        def solution_1453_2_2(start, end):
            return (0<= start < n and 0<= end < n)
                
        for i in range(m):
            x, y = startPos
            for j in range(i, m):
                dx, dy = d[s[j]]
                x += dx; y += dy
                
                if not solution_1453_2_2(x, y):
                    break
                ans[i] += 1
        return ans