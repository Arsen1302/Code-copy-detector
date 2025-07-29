class Solution:
    def solution_806_3(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = [[inf]*2 for _ in range(8)]
        xx, yy = king
        fn = lambda x: max(abs(x[0]-xx), abs(x[1]-yy))
        for x, y in queens: 
            if x == xx: # same row 
                if y < yy: ans[0] = min(ans[0], (x, y), key=fn)
                else: ans[1] = min(ans[1], (x, y), key=fn)
            elif yy == y: # same column
                if x < xx: ans[2] = min(ans[2], (x, y), key=fn)
                else: ans[3] = min(ans[3], (x, y), key=fn)
            elif xx-yy == x-y: # same diagonoal
                if x < xx: ans[4] = min(ans[4], (x, y), key=fn)
                else: ans[5] = min(ans[5], (x, y), key=fn)
            elif xx+yy == x+y: # same anti-diagonal
                if x < xx: ans[6] = min(ans[6], (x, y), key=fn)
                else: ans[7] = min(ans[7], (x, y), key=fn)
        
        return [[x, y] for x, y in ans if x < inf]