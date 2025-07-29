class Solution:
    def solution_985_1(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        
        hc.sort()
        vc.sort()
        
        maxh = hc[0]
        maxv = vc[0]
        
        for i in range(1, len(hc)):
            maxh = max(maxh, hc[i] - hc[i-1])
        maxh = max(maxh, h - hc[-1])
        
        for i in range(1, len(vc)):
            maxv = max(maxv, vc[i] - vc[i-1])
        maxv = max(maxv, w - vc[-1])
        
        return maxh*maxv % (10**9 + 7)