class Solution:
    def solution_893_5(self, s: str, t: str) -> int:
        dt, ds = dict(), dict() #frequency table 
        for tt, ss in zip(t, s): 
            dt[tt] = 1 + dt.get(tt, 0)
            ds[ss] = 1 + ds.get(ss, 0)
        
        return len(s) - sum(min(v, ds.get(k, 0)) for k, v in dt.items())